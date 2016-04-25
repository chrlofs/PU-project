import socket
import json
from collections import deque
from process_data import ProcessData

class Receiver:

    def __init__(self):
        # Symbolic name meaning all available interfaces
        self.host = ''
        # IP address for the ambulance
        self.ip = 'localhost'
        self.port = 10000

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind socket to local host and port
        self.sock.bind((self.host, self.port))

        # Queue with the two last data objects received
        self.position_history = deque()

        self.current_data = None
        self.format_dict = dict.fromkeys(['timestamp', 'longitude',
                                'latitude'])
        self.process_data = ProcessData()


    def add_to_queue(self, dict_insert):
        '''Add received element to the receiver queue.
        Keyword arguments:
        dict_insert -- dict containing GPS data and timestamp
        '''
        self.position_history.append(dict_insert)

    def notify_process_data(self):
        '''Notifies process_data when receiving data from sender'''
        if len(self.position_history) >1:
            self.process_data.notify(self.get_data())

    def get_data(self):
        '''Returns the two last datasets from position_history'''
        if len(self.position_history) > 1:
            new_amb = self.position_history.popleft()
            old_amb = self.position_history.popleft()
            self.position_history.appendleft(old_amb)
            return [new_amb, old_amb]

    def receive(self):
        '''Receive data and convert bytes to string.'''
        try:
        # Listen until terminated by user
            while True:
                rawdata, addr = self.sock.recvfrom(1024)
                data = rawdata.decode(encoding='UTF-8')
                # Convert data to dictionary
                acceptable_string = data.replace("'","\"")
                data = json.loads(acceptable_string)
                self.add_to_queue(data)
                self.notify_process_data()
                if not data:
                    break
        except(KeyboardInterrupt):
            print("Closing socket")
            self.sock.close()

if __name__ == '__main__':
    car = Receiver()
    car.receive()
