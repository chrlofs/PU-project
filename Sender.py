import socket
import time
import json


class Sender:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '78.91.50.81'
    port = 12000
    sock.connect((host, port))
    json_data = []

    def json_list(self, filepath):
        with open(filepath) as f:
            index = 0
            for line in f:
                j_content = json.loads(line)
                if j_content.get('name') == 'longitude' or j_content.get('name') == 'latitude'\
                        or j_content.get('name') == 'vehicle_speed':
                            self.json_data.append(j_content)
                            index += 1

    def send(self):
        for i in self.json_data:
            self.sock.send(str(i).encode())
            time.sleep(0.25)

if __name__ == "__main__":
    amb = Sender()
    amb.json_list('commute.json')
    amb.send()

