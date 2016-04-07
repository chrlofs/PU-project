import time
import json
import copy
import itertools
from collections import deque
import collections

class Vehicle:
    '''modification choose if you wan't to drive normal, reversed or slow'''

    def __init__(self):
        self.json_data = []
        self.position_history = deque()
        self.format_dict = dict.fromkeys(['timestamp', 'longitude',
                                'latitude', 'vehicle_speed'])
        self.json_list('./car/GPS.json')
        self.set_data()
        self.format_position_history = deque()



    def json_list(self, file_path):
        '''Opens file and fills json_data with json
        objects corresponding to our filter
        Keyword arguments:
        file_path -- file containing json objects
        '''
        with open(file_path) as f:
            for i, line in enumerate(f):  # Loops through lines in file
                j_content = json.loads(line)  # Deserialize json string
                # Filters relevant content
                #if start_ahead:
                    #print('inside start aehad')
                if j_content.get('name') == 'longitude'\
                    or j_content.get('name') == 'latitude'\
                    or j_content.get('name') == 'vehicle_speed':
                            # Add content to json_data
                    self.json_data.append(j_content)


    def set_dict(self, format_dict_insert):
        '''Convert and merge received data to a dictionary.

        Keyword arguments:
        format_dict_insert -- dict containing longitude, latitude or timestamp
        '''

        if format_dict_insert['name'] == 'longitude':
            self.format_dict['longitude'] = str(format_dict_insert['value'])
            self.format_dict['timestamp'] = str(format_dict_insert['timestamp'])
        elif format_dict_insert['name'] == 'latitude':
            self.format_dict['latitude'] = str(format_dict_insert['value'])
        elif format_dict_insert['name'] == 'vehicle_speed':
            self.format_dict['vehicle_speed'] = format_dict_insert['value']
        if self.format_dict["longitude"] is not None and \
                self.format_dict["latitude"] is not None and \
                self.format_dict["timestamp"] is not None and \
                self.format_dict["vehicle_speed"] is not None:
                    self.add_to_queue()
                    self.format_dict = dict.fromkeys(['timestamp',
                                                    'longitude', 'latitude', 'vehicle_speed'])


    def set_data(self):
        '''Adds entire trip to local variable position_history
        & choose which way to drive the car'''

        for i in self.json_data:
            self.set_dict(i)

    def add_to_queue(self):
            self.position_history.append(self.format_dict)

    def set_modification(self, start_ahead=False, speed=1, reversed=False):
        #len(self.position_history)
        temp_list = copy.deepcopy(self.position_history)
        if start_ahead:
            self.format_position_history = collections.deque(itertools.islice(self.position_history, int(len(self.position_history)/2), len(self.position_history)))
            #print('her har jeg vært')
            #print(len(self.format_position_history))
        else:
            self.format_position_history = collections.deque(itertools.islice(self.position_history,0, len(self.position_history)))


    def get_data(self, start_ahead=False, speed=1, reversed=False):
        '''Returns the two last datasets from position_history'''
        self.set_modification(start_ahead,speed,reversed)

        if len(self.format_position_history) > 1:
            count= 0
            new_car = self.format_position_history.popleft()
            old_car = self.format_position_history.popleft()
            self.format_position_history.appendleft(old_car)
            return [new_car, old_car]

if __name__ == "__main__":
    r = Vehicle()
    #print(r.get_data())
    print('#######################')
    n = Vehicle()
    print(n.get_data(start_ahead=True))





    time.sleep(0.30)


