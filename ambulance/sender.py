import socket
import time
import json

class Sender:

    # List of IP addresses to iterate through
    cars = []

    # Add hardcoded IP addresses
    cars.append('localhost')
    cars.append('10.24.7.121')

    # Add starting port
    port = 10000

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    json_data = []

    def json_list(self, file_path):
        '''Opens file and fills json_data with json
        objects corresponding to our filter

        Keyword arguments:
        file_path -- file containing json objects
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
        '''Sends json data through socket'''

        for message in self.json_data:
            # Send message to all the cars on the hardcoded list
            for car in cars:

                # Print for easier debug
                print(car)

                try:
                    # Send a test message
                    # First convert message to bytes
                    self.sock.sendto(message.encode(encoding='UTF-8'), (car, port))

                except socket.error as e:
                    print('Error code: ' + str(e[0]) + ' Message ' + str(e[1]))
                    sys.exit()

            # Waits for 0.25 seconds before sending the next line
            time.sleep(0.25)

if __name__ == "__main__":
    amb = Sender()
    amb.json_list('commute.json')
    amb.send('10.22.1.188')
