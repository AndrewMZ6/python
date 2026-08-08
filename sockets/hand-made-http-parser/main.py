"""
Демонстрация: как читать и парсить сырой HTTP-запрос напрямую из TCP-сокета,
без aiohttp/Flask/FastAPI и т.п.

Запуск:
    python raw_http_parser.py

Проверка (в другом терминале):
    curl -X POST http://127.0.0.1:8080/api/users \
         -H "Content-Type: application/json" \
         -d '{"username":"alex","password":"12345"}'
"""

import socket


def recv_until_headers_end(conn: socket.socket) -> bytes:
    """
    Читаем байты из сокета маленькими порциями, пока не встретим
    разделитель между заголовками и телом: \r\n\r\n.

    Важно: TCP не гарантирует, что recv() вернёт весь запрос за один вызов.
    Данные могут прийти по частям (сегментами), особенно если запрос большой
    или сеть "тормозит". Поэтому читаем в цикле и копим буфер.
    """
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        chunk = conn.recv(4096)  # читаем что пришло, максимум 4096 байт за раз
        if not chunk:
            # соединение закрыто клиентом раньше времени
            raise ConnectionError("Клиент закрыл соединение до конца заголовков")
        buffer += chunk
    return buffer


def parse_request_line_and_headers(raw_head: bytes):
    """
    raw_head — это то, что мы уже прочитали (может включать кусок тела,
    если клиент отправил всё одним TCP-сегментом).
    """
    header_bytes, _, rest = raw_head.partition(b"\r\n\r\n")
    lines = header_bytes.split(b"\r\n")

    request_line = lines[0].decode("ascii")
    method, path, version = request_line.split(" ")

    headers = {}
    for line in lines[1:]:
        if not line:
            continue
        key, _, value = line.partition(b": ")
        headers[key.decode("ascii").lower()] = value.decode("ascii")

    return method, path, version, headers, rest  # rest — уже прочитанный кусок тела


def recv_body(conn: socket.socket, already_read: bytes, content_length: int) -> bytes:
    """
    Content-Length говорит нам, сколько байт тела ожидать.
    already_read — то, что случайно прилетело вместе с заголовками
    в том же TCP-сегменте (так бывает часто для маленьких запросов).
    """
    body = already_read
    while len(body) < content_length:
        chunk = conn.recv(4096)
        if not chunk:
            raise ConnectionError("Соединение оборвалось при чтении тела")
        body += chunk
    # На случай, если прочитали чуть больше, чем Content-Length
    # (например keep-alive и следом идёт следующий запрос) — обрезаем ровно по длине.
    return body[:content_length]


def handle_connection(conn: socket.socket, addr):
    print(f"\n=== Новое соединение от {addr} ===")

    raw_head = recv_until_headers_end(conn)
    method, path, version, headers, leftover = parse_request_line_and_headers(raw_head)

    print(f"Метод:   {method}")
    print(f"Путь:    {path}")
    print(f"Версия:  {version}")
    print("Заголовки:")
    for k, v in headers.items():
        print(f"    {k}: {v}")

    content_length = int(headers.get("content-length", 0))
    body = b""
    if content_length > 0:
        body = recv_body(conn, leftover, content_length)
        print(f"Тело ({content_length} байт): {body.decode('utf-8', errors='replace')}")
    else:
        print("Тела нет (Content-Length отсутствует или равен 0)")

    # Формируем и отправляем ответ вручную — тоже без фреймворка
    response_body = b'{"status":"ok"}'
    response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/json\r\n"
        b"Content-Length: " + str(len(response_body)).encode() + b"\r\n"
        b"Connection: close\r\n"
        b"\r\n" + response_body
    )
    conn.sendall(response)
    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    print("Слушаю на http://127.0.0.1:8080 (Ctrl+C для выхода)")

    try:
        while True:
            conn, addr = server.accept()
            try:
                handle_connection(conn, addr)
            except ConnectionError as e:
                print(f"Ошибка соединения: {e}")
    except KeyboardInterrupt:
        print("\nОстанавливаюсь...")
    finally:
        server.close()


if __name__ == "__main__":
    main()