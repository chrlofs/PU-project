import socket
from exit import Exit

class Receiver:

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '197.0.0.1'
    port = 3000
    server_socket.bind((host, port))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    stack = []
    current_dict = None
    temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude', 'vehicle_speed'])

    def __init__(self, exit):
        self.exit = exit

    def set_stack(self, dict_insert):
        if len(self.stack) >= 2:
            self.stack.pop()
        self.stack.insert(0, dict_insert)

    def get_stack(self):
        return self.stack

    def set_dict(self, temp_dict_insert):
        if temp_dict_insert['name'] == 'longitude':
            self.temp_dict['longitude'] = str(temp_dict_insert['value'])
            self.temp_dict['timestamp'] = str(temp_dict_insert['timestamp'])
        elif temp_dict_insert['name'] == 'latitude':
            self.temp_dict['latitude'] = str(temp_dict_insert['value'])
        elif temp_dict_insert['name'] == 'vehicle_speed':
            self.temp_dict['vehicle_speed'] = str(temp_dict_insert['value'])
        if self.temp_dict["longitude"] is not None and self.temp_dict["latitude"] is not None and \
                self.temp_dict["timestamp"] is not None:
                    self.set_stack(self.temp_dict)
                    self.temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude'])

    def receive(self):
        try:
            self.current_dict = eval(self.client_socket.recv(1024))
        except:
            self.exit.quit()
        if(self.exit.run):
            self.set_dict(self.current_dict)
            self.current_dict = None
            print(self.get_stack())

    def update(self):
        self.receive()


if __name__ == "__main__":
    car = Receiver()
    car.receive()
    print(car.get_stack())
