import socket
from collections import deque



class Receiver:

    current_dict = None

    def __init__(self):
        self.establish_connection()


    def establish_connection(self):
        """Set up a new socket connection."""

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 6000
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        self.client_socket, self.address = self.server_socket.accept()
        self.position_history = deque()
        self.temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude', 'vehicle_speed'])



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

        while True:  # For continuous listening
            try:
                self.current_dict = eval(self.client_socket.recv(1024))  # Sets current_dict to the received elements from sender
                self.add_to_queue(self.current_dict)  # Adds current_dict to the queue
                copy = []
                for elem in self.position_history:
                    copy.append(elem)
                print(copy)
            except:
                self.server_socket.close()
                break

if __name__ == "__main__":
    car = Receiver()
    car.receive()
    print(car.position_history)