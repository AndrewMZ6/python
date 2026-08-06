import socket
from time import sleep

HOST = "localhost"
PORT = 12311

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((HOST, PORT))

print(f"connection is ready!:\n\n{sc}")


sleep(1)
sc.send("This is what we do".encode("utf-8"))
print(f"got response from server socket!\n\n{sc.recv(1024).decode('utf-8')}")

sc.send("\n".encode("utf-8"))

### output
# >>> I received your message. TY!


def f(a: int, b: int) -> int:
	return f'{a} + {b}'

