import socket
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

        self.process_data = ProcessData()

        self.current_data = None

    def add_to_queue(self, dict_insert):
        '''Add received element to the receiver queue.

        Keyword arguments:
        dict_insert -- dict containing GPS data and timestamp
        '''
        print('add to queue')
        print(dict_insert)
        if len(self.position_history) >= 2:
            self.position_history.pop()
        self.position_history.append(dict_insert)
        print(self.position_history)
        self.notify_process_data()

    def notify_process_data(self):
        '''Notify when car receives message from ambulance'''
        if len(self.position_history) == 2:
            self.process_data.notify(self.position_history)

    def receive(self):
        '''Receive data and convert bytes to string.'''
        try:
        # Listen until terminated by user
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode(encoding='UTF-8')
                # print(data)
                self.add_to_queue(data)
                if not data:
                    break
        except(KeyboardInterrupt):
            print("Closing socket")
            self.sock.close()

if __name__ == '__main__':
    car = Receiver()
    car.receive()
