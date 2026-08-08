"""
Демонстрация: WebSocket-сервер на голом socket, без библиотек websockets/aiohttp.

Показывает две вещи:
1. Handshake — как HTTP Upgrade превращается в WebSocket-соединение
   (вычисление Sec-WebSocket-Accept по RFC 6455).
2. Ручной парсинг бинарного формата WebSocket-фрейма (текстовые сообщения,
   маскирование от клиента, close-фрейм).

Запуск:
    python raw_ws_parser.py

Проверка (в браузере, DevTools Console, или Node):
    const ws = new WebSocket("ws://127.0.0.1:8080");
    ws.onopen = () => ws.send("привет");
    ws.onmessage = (e) => console.log("from server:", e.data);
"""

import base64
import hashlib
import socket
import struct

# Магическая константа из RFC 6455 — фиксированная строка,
# которую сервер обязан приклеить к Sec-WebSocket-Key клиента
WS_MAGIC_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


# ---------------------------------------------------------------------------
# ШАГ 1. HANDSHAKE (это ещё обычный HTTP, парсим так же, как в прошлый раз)
# ---------------------------------------------------------------------------

def recv_until_headers_end(conn: socket.socket) -> bytes:
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        chunk = conn.recv(4096)
        if not chunk:
            raise ConnectionError("Клиент закрыл соединение до конца заголовков")
        buffer += chunk
    return buffer


def parse_headers(raw: bytes):
    header_bytes, _, _ = raw.partition(b"\r\n\r\n")
    lines = header_bytes.split(b"\r\n")
    request_line = lines[0].decode("ascii")
    headers = {}
    for line in lines[1:]:
        if not line:
            continue
        key, _, value = line.partition(b": ")
        headers[key.decode("ascii").lower()] = value.decode("ascii")
    return request_line, headers


def do_handshake(conn: socket.socket):
    raw = recv_until_headers_end(conn)
    request_line, headers = parse_headers(raw)
    print(f"Handshake запрос: {request_line}")
    print(f"Upgrade: {headers.get('upgrade')}")
    print(f"Sec-WebSocket-Key: {headers.get('sec-websocket-key')}")

    client_key = headers["sec-websocket-key"]

    # Ядро handshake по RFC 6455:
    # accept = base64( sha1( client_key + magic_guid ) )
    # Это доказывает клиенту, что ответ пришёл от сервера, который
    # действительно понял, что это WebSocket-запрос (а не просто echo от прокси).
    accept_src = (client_key + WS_MAGIC_GUID).encode("ascii")
    accept_value = base64.b64encode(hashlib.sha1(accept_src).digest()).decode("ascii")

    response = (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Accept: {accept_value}\r\n"
        "\r\n"
    ).encode("ascii")
    conn.sendall(response)
    print("Handshake завершён, отправили 101 Switching Protocols\n")


# ---------------------------------------------------------------------------
# ШАГ 2. ФОРМАТ ФРЕЙМА (RFC 6455 §5.2)
# ---------------------------------------------------------------------------
#
#  0                   1                   2                   3
#  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-------+-+-------------+-------------------------------+
# |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
# |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
# |N|V|V|V|       |S|             |   (если payload len == 126/127)|
# | |1|2|3|       |K|             |                                |
# +-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
# |     Masking-key (если MASK=1), продолжение (32 бита всего)    |
# +-------------------------------+-------------------------------+
# |                     Полезная нагрузка (замаскирована XOR)      |
# +------------------------------------------------------------- -+
#
# Ключевые моменты:
# - Клиент ОБЯЗАН маскировать данные (MASK=1), сервер — НЕ должен маскировать
#   свои ответы клиенту. Это защита от cache-poisoning атак через прокси.
# - opcode: 0x1 = text, 0x2 = binary, 0x8 = close, 0x9 = ping, 0xA = pong
# - payload len 7 бит хватает до 125 байт; если нужно больше — там же лежит
#   126 (тогда следующие 2 байта — реальная длина) или 127 (следующие 8 байт).

OPCODE_TEXT = 0x1
OPCODE_BINARY = 0x2
OPCODE_CLOSE = 0x8
OPCODE_PING = 0x9
OPCODE_PONG = 0xA


def recv_exact(conn: socket.socket, n: int) -> bytes:
    """Читаем ровно n байт, склеивая несколько recv() при необходимости."""
    data = b""
    while len(data) < n:
        chunk = conn.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Соединение оборвалось при чтении фрейма")
        data += chunk
    return data


def recv_frame(conn: socket.socket):
    # --- первые 2 байта: флаги + opcode + mask-бит + короткая длина ---
    first_two = recv_exact(conn, 2)
    byte1, byte2 = first_two[0], first_two[1]

    fin = (byte1 & 0b10000000) != 0
    opcode = byte1 & 0b00001111

    is_masked = (byte2 & 0b10000000) != 0
    payload_len = byte2 & 0b01111111

    # --- расширенная длина, если короткого поля не хватило ---
    if payload_len == 126:
        payload_len = struct.unpack(">H", recv_exact(conn, 2))[0]
    elif payload_len == 127:
        payload_len = struct.unpack(">Q", recv_exact(conn, 8))[0]

    # --- маскирующий ключ (клиент обязан его присылать) ---
    mask_key = recv_exact(conn, 4) if is_masked else None

    # --- сама полезная нагрузка ---
    payload = recv_exact(conn, payload_len)

    if is_masked:
        # XOR каждого байта payload с соответствующим байтом ключа (по кругу)
        payload = bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload))

    return fin, opcode, payload


def send_text_frame(conn: socket.socket, text: str):
    payload = text.encode("utf-8")
    length = len(payload)

    byte1 = 0b10000000 | OPCODE_TEXT  # FIN=1, opcode=text

    if length <= 125:
        header = bytes([byte1, length])
    elif length <= 0xFFFF:
        header = bytes([byte1, 126]) + struct.pack(">H", length)
    else:
        header = bytes([byte1, 127]) + struct.pack(">Q", length)

    # Сервер НЕ маскирует данные — mask-бит остаётся 0
    conn.sendall(header + payload)


def send_close_frame(conn: socket.socket, code: int = 1000):
    payload = struct.pack(">H", code)
    byte1 = 0b10000000 | OPCODE_CLOSE
    conn.sendall(bytes([byte1, len(payload)]) + payload)


# ---------------------------------------------------------------------------
# ШАГ 3. ОСНОВНОЙ ЦИКЛ СОЕДИНЕНИЯ
# ---------------------------------------------------------------------------

def handle_connection(conn: socket.socket, addr):
    print(f"=== Новое соединение от {addr} ===")
    do_handshake(conn)

    try:
        while True:
            fin, opcode, payload = recv_frame(conn)

            if opcode == OPCODE_TEXT:
                text = payload.decode("utf-8")
                print(f"Получено текстовое сообщение: {text!r}")
                send_text_frame(conn, f"echo: {text}")

            elif opcode == OPCODE_BINARY:
                print(f"Получено бинарное сообщение: {len(payload)} байт")

            elif opcode == OPCODE_PING:
                print("Получен PING, отвечаем PONG")
                pong = bytes([0b10000000 | OPCODE_PONG, len(payload)]) + payload
                conn.sendall(pong)

            elif opcode == OPCODE_CLOSE:
                print("Получен CLOSE, закрываем соединение")
                send_close_frame(conn)
                break

    except ConnectionError as e:
        print(f"Соединение прервано: {e}")
    finally:
        conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    print("WS-сервер слушает на ws://127.0.0.1:8080 (Ctrl+C для выхода)")

    try:
        while True:
            conn, addr = server.accept()
            handle_connection(conn, addr)
    except KeyboardInterrupt:
        print("\nОстанавливаюсь...")
    finally:
        server.close()


if __name__ == "__main__":
    main()