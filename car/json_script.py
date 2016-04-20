'''This script copypasted some methods from the vehicle 
class that should have preferably been static initially.'''
from vehicle import Vehicle
import json

GPS_data = []

with open('car/GPS.json') as f:
    for line in f:  # Loops through lines in file
        j_content = json.loads(line)  # Deserialize json string
        if j_content.get('name') == 'longitude'\
            or j_content.get('name') == 'latitude'\
            or j_content.get('name') == 'timestamp':
            GPS_data.append(j_content)

temp_dict = dict.fromkeys(['timestamp', 'longitude','latitude'])
formated_data = []
for i in GPS_data:
    if i['name'] == 'longitude':
        temp_dict['longitude'] = i['value']
        temp_dict['timestamp'] = i['timestamp']
    elif i['name'] == 'latitude':
        temp_dict['latitude'] = i['value']
    if temp_dict['longitude'] is not None and \
            temp_dict["latitude"] is not None and \
            temp_dict["timestamp"] is not None:
                formated_data.append(temp_dict)
                temp_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude'])

def regular():
    with open('car/regular.json', 'a') as f:
        for data in formated_data:
            f.write(json.dumps(data))
            f.write('\n')

def reverse():
    with open('car/reversed.json', 'a') as f:
        for data in formated_data[::-1]:
            f.write(json.dumps(data))
            f.write('\n')

def start_ahead():
    with open('car/start_ahead.json', 'a') as f:
        for data in formated_data[len(formated_data)//2:]:
            f.write(json.dumps(data))
            f.write('\n')

def speed(n):
    with open('car/'+str(n)+'xspeed.json', 'a') as f:
        i = 1
        while i*n < len(formated_data):
            temp = formated_data[i]
            temp['latitude'] = formated_data[i*n]['latitude']
            temp['longitude'] = formated_data[i*n]['longitude']
            f.write(json.dumps(temp))
            f.write('\n')
            i+= 1
regular()
reverse()
start_ahead()
speed(2)

print('Script was successfully run')
