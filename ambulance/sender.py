import socket
import time
import json

class Sender:

    def __init__(self):
        # List of IP addresses to iterate through
        self.cars = []

        # Add hardcoded IP addresses
        self.cars.append('localhost')
        self.cars.append('10.24.7.121')
        self.cars.append('78.91.4.127')

        # Add starting port
        self.port = 10000

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # JSON objects containing longitude, latitude and speed data
        self.json_data = []

    def json_list(self, file_path):
        '''Open file and fill json_data with JSON
        objects corresponding to our filter

        Keyword arguments:
        file_path -- file containing JSON objects
        '''
        with open(file_path) as f:
            for line in f:  # Loops through lines in file
                j_content = json.loads(line)  # Deserialize json string
                # Filters relevant content
                if j_content.get('name') == 'longitude'\
                    or j_content.get('name') == 'latitude'\
                    or j_content.get('name') == 'vehicle_speed':
                            # Add content to json_data
                            self.json_data.append(j_content)

    def send(self):
        '''Send JSON data to all nearby cars'''

        for message in self.json_data:
            # Send message to all the cars on the hardcoded list
            for car in self.cars:
                # Print for easier debug
                print(car)
                try:
                    # Send a test message
                    # First convert message to bytes
                    # self.sock.send(str(i).encode())
                    self.sock.sendto(str(message).encode(encoding='UTF-8'), (car, self.port))
                except socket.error as e:
                    print('Error code: ' + str(e[0]) + ' Message ' + str(e[1]))
                    sys.exit()
            # Waits for 0.25 seconds before sending the next line
            time.sleep(0.25)

if __name__ == "__main__":
    amb = Sender()
    amb.json_list('commute.json')
    amb.send()
    amb.sock.close()
