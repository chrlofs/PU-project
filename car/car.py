import time
import json
from collections import deque

class Car:
    '''docstring for car'''

    json_data = []
    position_history = deque()
    format_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude', 'vehicle_speed'])

    def __init__(self):
        self.json_list('GPS.json')

    #def __init__(self, file_path):
    #    self.json_list(file_path)
    #    self.get_data()

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
        """Convert and merge received data to a dictionary.

        Keyword arguments:
        format_dict_insert -- dict containing longitude, latitude or timestamp
        """

        if format_dict_insert['name'] == 'longitude':
            self.format_dict['longitude'] = str(format_dict_insert['value'])
            self.format_dict['timestamp'] = str(format_dict_insert['timestamp'])
        elif format_dict_insert['name'] == 'latitude':
            self.format_dict['latitude'] = str(format_dict_insert['value'])
        elif format_dict_insert['name'] == 'vehicle_speed':
            self.format_dict['vehicle_speed'] = str(format_dict_insert['value'])
        if self.format_dict["longitude"] is not None and self.format_dict["latitude"] is not None and \
                self.format_dict["timestamp"] is not None:
                    self.add_to_queue()
                    self.format_dict = dict.fromkeys(['timestamp', 'longitude', 'latitude'])

    def add_to_queue(self):
        if len(self.position_history) >= 2:
            self.position_history.pop()
        self.position_history.appendleft(self.json_data)

    def get_data(self):
        for i in self.json_data:
            self.set_dict(i)
            print(self.format_dict)


if __name__ == "__main__":
    car = Car()
    car.get_data()
    time.sleep(0.30)
