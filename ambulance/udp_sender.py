import socket
import sys

ip = '10.24.7.120'
port = 10000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

'''
Open JSON file
Filter JSON data that is not relevant
Send JSON data
'''

# Create a test message
message = 'This is a message sent with UDP'

try:
    # Send a test message
    # First convert message to bytes
    sock.sendto(message.encode(encoding='UTF-8'), (ip, port))

except socket.error as e:
    prrint('Error code: ' + str(e[0]) + ' Message ' + str(e[1]))
    sys.exit()

print('Program complete')
