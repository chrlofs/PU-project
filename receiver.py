import socket
import exit
import queue

class Receiver:

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '10.22.8.14'
    port = 6000
    server_socket.bind((host, port))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    position_history = queue.Queue()
    current_dict = None
    temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude', 'vehicle_speed'])


    def __init__(self, exit):
        self.exit = exit

    def add_to_queue(self, dict_insert):
        """Add received element to the receiver queue."""
        if self.position_history.qsize() >= 2:
            self.position_history.get()
        self.position_history.put(dict_insert)

    def set_dict(self, temp_dict_insert):
        """Convert received data to a dictionary."""
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
        while True: #For continuous listening
            try:
                self.current_dict = eval(self.client_socket.recv(1024)) #Sets current_dict to the received elements from sender
                self.add_to_queue(self.current_dict) #Adds current_dict to the queue
                copy = []
                for elem in list(self.position_history.queue):
                    copy.append(elem)
                print(copy)
            except:
                # self.exit.quit()
                self.set_dict(self.current_dict)
                self.current_dict = None
                print(self.position_history)

    def update(self):
        self.receive()

if __name__ == "__main__":
    car = Receiver(exit)
    car.receive()
    print(car.position_history.get())
