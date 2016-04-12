import time
import json
import copy
import itertools
from collections import deque
import collections

class Vehicle:
    '''modification choose if you wan't to drive normal, reversed or slow'''

    def __init__(self, start_ahead=False, speed=1, reversed=False):
        self.position_history = deque()
        self.json_list('start_ahead.json')


    def json_list(self, file_path):
        '''Opens file and fills json_data with json
        objects corresponding to our filter
        Keyword arguments:
        file_path -- file containing json objects
        '''
        with open(file_path) as f:
            for i, line in enumerate(f):  # Loops through lines in file
                j_content = json.loads(line)  # Deserialize json string
                self.position_history.append(j_content)


    def add_to_queue(self, dict):
            self.position_history.append(dict)


    def get_data(self):
        '''Returns the two last datasets from position_history'''
        if len(self.position_history) > 1:
            new_car = self.position_history.popleft()
            old_car = self.position_history.popleft()
            self.position_history.appendleft(old_car)
            return [new_car, old_car]

if __name__ == "__main__":
    r = Vehicle()
    print('#######################')
    n = Vehicle()
    if r.get_data() != n.get_data():
        print('riktig!!!!')
    print(r.get_data())
    print(r.get_data())
    print(r.get_data())
    time.sleep(0.30)
