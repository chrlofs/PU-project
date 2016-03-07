import socket
import time
import json


class Sender:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    json_data = []

    def establish_connection(self, ip_address):
        host = ip_address  # Receiver's IP-address, must change as needed
        port = 6000
        self.sock.connect((host, port))

    def json_list(self, file_path):
        """ Opens file and fills json_data with json objects corresponding to our filter

        :param file_path: file containing json objects
        """

        with open(file_path) as f:
            for line in f:  # Loops through lines in file
                j_content = json.loads(line)  # Deserialize json string
                if j_content.get('name') == 'longitude' or j_content.get('name') == 'latitude'\
                        or j_content.get('name') == 'vehicle_speed':  # Filters relevant content
                            self.json_data.append(j_content)  # Add content to json_data

    def send(self, ip_address):
        """Sends json data through socket."""
        self.establish_connection(ip_address)

        for i in self.json_data:
            self.sock.send(str(i).encode())  # Encodes string to UTF-8 and sends through socket
            time.sleep(0.25)  # Waits for 0.25 seconds before sending the next line

if __name__ == "__main__":
    amb = Sender()
    amb.json_list('commute.json')
    amb.send('10.22.1.188')
