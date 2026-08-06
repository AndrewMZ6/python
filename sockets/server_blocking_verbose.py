import socket

# <class 'socket.socket'>
# class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# Create a new socket using the given address family, socket type and protocol number
server_socket = socket.socket()

# <socket.socket fd=1068, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
# socket.setsockopt(level, optname, None, optlen: int)
# Set the value of the given socket option
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# socket.bind(address); address must be tuple in our case
# Bind the socket to address
server_socket.bind(("localhost", 5001))

# socket.listen([backlog])
# Enable a server to accept connections
server_socket.listen()

while True:
    print("while True")

    # socket.accept()
    # Accept a connection. The socket must be bound to an address and listening for connections
    # The return value is a pair (conn, address) where conn is a new socket object usable to send
    # and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

    # client_socket: <socket.socket fd=420, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001), raddr=('127.0.0.1', 52810)>
    # type(client_socket) -> <class 'socket.socket'>
    # addr: ('127.0.0.1', 52810)
    client_socket, addr = server_socket.accept()

    while True:
        print("while True 2")

        # socket.recv(bufsize[, flags])
        # Receive data from the socket. The return value is a bytes object representing the data received
        request = client_socket.recv(4096).decode("utf-8")
        print(f"request:\n{request}")

        if request == "\n":
            print("break oprion -----------------------")
            break
        else:
            # str.encode(encoding='utf-8', errors='strict')
            # Return an encoded version of the string as a bytes object. Default encoding is 'utf-8'
            response = f"RESPONSE FROM SERVER {server_socket}".encode()

            # socket.send(bytes[, flags])
            # Send data to the socket. The socket must be connected to a remote socket.
            client_socket.send(response)
            break
        break
    break
