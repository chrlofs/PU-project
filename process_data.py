
from receiver import Receiver
from direction import Direction
from math import fabs



class ProcessData:

    def __init__(self, receiver):
        self.receiver = receiver

    def get_ambulance_data(self):
        """Return the two last data sets from Receiver

        Returns
        -------
        Array containing first and last
        first : dict containing GPS data, timestamp, speed
        last : dict containing GPS data, timestamp, speed
        """
        # TODO: Implement listener

        # When history stack has two elements
        # Pop elements
        first = self.receiver.history.get()  # Remove from history stack
        last = self.receiver.history.get()
        self.receiver.history.put(last)  # Put last element back to the history stack

        return [first, last]

        

    def is_relevant(self, new_car, old_car, new_ambu, old_ambu):
        new_car_pos = (new_car['latitude'], new_car['longitude'])
        new_car_speed = new_car['speed']
        new_car_time = new_car['time']

        old_car_pos = (old_car['latitude'], old_car['longitude'])
        old_car_speed = old_car['speed']
        old_car_time = old_car['time']

        new_ambu_pos = (new_ambu['latitude'], new_ambu['longitude'])
        new_ambu_speed = new_ambu['speed']
        new_ambu_time = new_ambu['time']

        old_ambu_pos = (old_ambu['latitude'], old_ambu['longitude'])
        old_ambu_speed = old_ambu['speed']
        old_ambu_time = old_ambu['time']


    def _find_direction(self, data1, data2):
        """Find direction for vehicle, returns Direction enum

        Keyword arguments:
        data1 -- tuple with latitude and longitude from newest data
        data2 -- tuple with latitude and longitude from oldest data
        """

        lat_change = data1[0] - data2[0]
        long_change = data1[1] - data2[1]

        if lat_change == 0 and long_change == 0:
            return Direction.standing_still
        if fabs(lat_change) > fabs(long_change):
            if lat_change > 0:
                return Direction.east
            return Direction.west
        if long_change > 0:
            return Direction.north
        return Direction.south
