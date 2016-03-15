import time
import json
from collections import deque

class Car:

    json_data = []
    json_reversed = []
    position_history = deque()
    format_dict = dict.fromkeys(['timestamp', 'longitude',
                                'latitude', 'vehicle_speed'])

    def __init__(self):
        self.json_list('GPS.json')

    def modify_json(self):
        '''Modifies a json file to be filled with garble every 5 lines.'''

        with open('GPS.json') as f:
            with open('data.json', 'w') as outfile:
                counter = 0
                for line in f:
                    if counter > 4:
                        counter = 0
                        json.dump(json.loads(line), outfile)
                        outfile.write('\n')
                        json.dump({"name":"longitude","value":0,"timestamp":0},
                                  outfile)
                        outfile.write('\n')
                    else:
                        json.dump(json.loads(line), outfile)
                        outfile.write('\n')
                        counter += 1

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
            self.format_dict['vehicle_speed'] = str(format_dict_insert['value'])
        if self.format_dict["longitude"] is not None and \
                self.format_dict["latitude"] is not None and \
                self.format_dict["timestamp"] is not None:
                    self.add_to_queue()
                    self.format_dict = dict.fromkeys(['timestamp',
                                                    'longitude', 'latitude'])

    def create_opposite(self, file_path):
        '''Reverses a json-file and returns it'''

        self.json_list(file_path)
        for i in reversed(self.json_data):
            self.json_reversed.append(i)
        return self.json_reversed

    def add_to_queue(self):
        self.position_history.appendleft(self.format_dict)

    def set_data(self):
        '''Adds entire trip to local variable position_history'''

        for i in self.json_data:
            self.set_dict(i)

        print(self.position_history)

    def get_data(self):
        '''Returns the two last datasets from position_history'''

        if len(self.position_history) > 1:
            old_car = self.position_history.pop()
            new_car = self.position_history.pop()
            self.position_history.append(new_car)
            return [new_car, old_car]

if __name__ == "__main__":
    car = Car()
    # print(car.create_opposite('GPS.json'))
    car.set_data()
    print('Resultat')
    print(car.get_data())
    print(car.get_data())
    print(car.get_data())
    time.sleep(0.30)
