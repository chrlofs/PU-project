import time
import json
from collections import deque

class Vehicle:
    '''modification choose if you wan't to drive normal, reversed or slow'''

    def __init__(self, modification='normal', start_ahead=False, speed=1):
        self.json_data = []
        self.position_history = deque()
        self.format_dict = dict.fromkeys(['timestamp', 'longitude',
                                'latitude', 'vehicle_speed'])
        self.json_list('./car/GPS.json', start_ahead, speed)
        if modification == 'slow':
            self.modify_json()
        elif modification == 'reversed':
            self.set_data('false')

        else:
            self.set_data()


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

    def json_list(self, file_path, start_ahead=False, speed=1):
        '''Opens file and fills json_data with json
        objects corresponding to our filter

        Keyword arguments:
        file_path -- file containing json objects
        '''

        with open(file_path) as f:
            for i, line in enumerate(f):  # Loops through lines in file
                j_content = json.loads(line)  # Deserialize json string
                # Filters relevant content
                if start_ahead:
                    if i > len(f)/2:
                        if i % speed == 0:
                            if j_content.get('name') == 'longitude'\
                                or j_content.get('name') == 'latitude'\
                                or j_content.get('name') == 'vehicle_speed':
                                        # Add content to json_data
                                        self.json_data.append(j_content)
                else:
                    if i % speed == 0:
                        if j_content.get('name') == 'longitude'\
                            or j_content.get('name') == 'latitude'\
                            or j_content.get('name') == 'vehicle_speed':
                                    # Add content to json_data
                                    self.json_data.append(j_content)


    def set_dict(self, format_dict_insert, normal='true'):
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
                self.format_dict["timestamp"] is not None:
                    self.add_to_queue(normal)
                    self.format_dict = dict.fromkeys(['timestamp',
                                                    'longitude', 'latitude'])

    def add_to_queue(self, normal='true'):
        if normal == 'true':
            self.position_history.appendleft(self.format_dict)
        else:
            self.position_history.append(self.format_dict)

    def set_data(self, normal='true'):
        '''Adds entire trip to local variable position_history
        & choose which way to drive the car'''

        for i in self.json_data:
            self.set_dict(i,normal)


    def get_data(self):
        '''Returns the two last datasets from position_history'''

        if len(self.position_history) > 1:
            new_car = self.position_history.popleft()
            old_car = self.position_history.popleft()
            self.position_history.appendleft(old_car)
            return [new_car, old_car]

if __name__ == "__main__":
    r = Vehicle('reversed')
    print(r.get_data())
    n = Vehicle()
    print(n.position_history[0])
    print(r.position_history[len(r.position_history)-1])

    time.sleep(0.30)


