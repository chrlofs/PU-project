import socket
from collections import deque

class Receiver:

    def __init__():
        self.host = ''  # Symbolic name meaning all available interfaces.
        self.ip = '78.91.4.127'
        self.port = 10000

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind socket to local host and port
        self.sock.bind((host, port))


    current_dict = None

    def add_to_queue(self, dict_insert):
        """Add received element to the receiver queue.

        Keyword arguments:
        dict_insert -- dict containing GPS data and timestamp
        """

        if self.position_history.count() >= 2:
            self.position_history.pop()
        self.position_history.appendleft(dict_insert)

    def set_dict(self, temp_dict_insert):
        """Convert and merge received data to a dictionary.

        Keyword arguments:
        temp_dict_insert -- dict containing longitude, latitude or timestamp
        """

        if temp_dict_insert['name'] == 'longitude':
            self.temp_dict['longitude'] = str(temp_dict_insert['value'])
            self.temp_dict['timestamp'] = str(temp_dict_insert['timestamp'])
        elif temp_dict_insert['name'] == 'latitude':
            self.temp_dict['latitude'] = str(temp_dict_insert['value'])
        elif temp_dict_insert['name'] == 'vehicle_speed':
            self.temp_dict['vehicle_speed'] = str(temp_dict_insert['value'])
        if self.temp_dict["longitude"] is not None and self.temp_dict["latitude"] is not None and \
                self.temp_dict["timestamp"] is not None:
                    self.add_to_queue(self.temp_dict)
                    self.temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude'])

    def receive(self):
        """Receive data and convert bytes to string."""

        # Listen until terminated by user
        while True:
            data, addr = self.sock.recvfrom(1024)
            self.current_dict = data.decode(encoding='UTF-8')
            if not data:
                break
            print(data)

if __name__ == "__main__":
    car = Receiver()
    car.receive()
    print(car.position_history)
