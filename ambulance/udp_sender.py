import socket
import sys

ip = 'localhost'
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
    sock.sendto(bytes(message, 'UTF-8'), (ip, port))
