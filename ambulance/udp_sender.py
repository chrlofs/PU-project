import socket
import sys

# List of IP addresses to iterate through
cars = []

# Add hardcoded IP addresses
cars.append('localhost')
cars.append('10.24.7.121')
cars.append('10.22.10.150')

print(cars)

# Add starting port
port = 10000

# Create a test message
message = 'This is a message sent with UDP'

# Send message to all the cars on the hardcoded list
for car in cars:
    ip = car

    # Print for easier debug
    print(ip)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    '''
    Send real data here

    Open JSON file
    Filter JSON data that is not relevant
    Send JSON data
    '''

    try:
        # Send a test message
        # First convert message to bytes
        sock.sendto(message.encode(encoding='UTF-8'), (ip, port))

    except socket.error as e:
        print('Error code: ' + str(e[0]) + ' Message ' + str(e[1]))
        sys.exit()

print('Program complete')
