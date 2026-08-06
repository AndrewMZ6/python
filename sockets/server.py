import socket

HOST = "localhost"
PORT = 12311

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    comm, addr = server.accept()
    print(f"created socket {comm}")
    print(f"connected to client {addr}")
    message = comm.recv(1024).decode("utf-8")
    print(f"got message {message}")
    comm.send("I received your message. TY!".encode("utf-8"))
    comm.close()
    print(f"connection with client {addr} closed")

### output
# created socket <socket.socket fd=316, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.0.13', 12311), raddr=('192.168.0.13', 49719)>
# connected to client ('192.168.0.13', 49719)
# got message HELLO!
# connection with client ('192.168.0.13', 49719) closed
