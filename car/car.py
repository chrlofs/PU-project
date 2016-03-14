import time
import json

class Car:
    '''docstring for car'''

    json_data = []

    def __init__(self):
        self.json_list('commute.json')
        self.get_data()

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

    def get_data(self):
        for i in self.json_data:
            print(i)
            time.sleep(0.25)

if __name__ == "__main__":
    car = Car()
