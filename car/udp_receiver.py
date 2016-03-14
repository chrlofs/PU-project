import socket

ip = 'localhost'
port = 10000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("", port))

while True:
    data, addr = sock.recvfrom(1024)

    if not data:
        break

    print(data)

sock.close()
