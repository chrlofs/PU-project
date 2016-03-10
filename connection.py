import socket

class Connection:

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '10.22.9.111'
    port = 6000
    server_socket.bind((host, port))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()

    def Connect(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.client_socket, self.address = self.server_socket.accept()

