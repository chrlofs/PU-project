from .vehicle import Vehicle
from .direction import Direction
from math import fabs
from .support.calculator import Calculator

class ProcessData:

    def __init__(self, vehicle1, vehicle2):
        self.vehicle1 = vehicle1
        self.vehicle2 = vehicle2
        self.minute_warning = False
        self.second_warning = False
        self.meter_message = False

        
    def pick_message(self, new_car, old_car, new_ambu, old_ambu):
        '''Checks if the current data is relevant, and returns a integer 
        for each case

        Keyword arguments:
        new_car -- A tuple containing the cars current position
        old_car -- A tuple containing the cars previous position
        new_ambu -- A tuple containing the ambulance current position
        old_ambu -- A tuple containing the ambulance previous position
        
        returns
        0 if the situation is not relevant
        1 if the ambulance is less than 20 sec behind
        2 if the ambulance is less than 2 minutes behind
        3 if the ambulance just passed the car and is less than 50 meters ahead
        '''

        new_car_pos = (new_car['latitude'], new_car['longitude'])
        new_car_time = new_car['timestamp']
        old_car_pos = (old_car['latitude'], old_car['longitude'])
        old_car_time = old_car['timestamp']
        car_speed = Calculator.speed(new_car_pos[1], new_car_pos[0], old_car_pos[1], old_car_pos[0], (new_car_time - old_car_time))
        print("Car speed: " + str(car_speed))
        new_ambu_pos = (new_ambu['latitude'], new_ambu['longitude'])
        new_ambu_time = new_car['timestamp']
        old_ambu_pos = (old_ambu['latitude'], old_ambu['longitude'])
        old_ambu_time = old_car['timestamp']
        ambu_speed = Calculator.speed(new_ambu_pos[1], new_ambu_pos[0], old_ambu_pos[1], old_ambu_pos[0], (new_ambu_time - old_ambu_time ))
        print("Ambu speed: " + str(ambu_speed))
        car_dir = self._find_direction(new_car_pos, old_car_pos)
        ambu_dir = self._find_direction(new_ambu_pos, old_ambu_pos)

        distance_km = Calculator.gps_to_kmeters(new_car_pos[1], new_car_pos[0],
               new_ambu_pos[1], new_ambu_pos[0])

        print("Distance is : " + str(distance_km  ))

        if not self._is_relevant(new_car_pos, car_speed, old_car_pos, 
            new_ambu_pos, ambu_speed, old_ambu_pos):

            #0.05km is 50 meters.
            if distance_km < 0.05\
                    and car_dir.name == ambu_dir.name:
                if not self.meter_message:
                    self.meter_message = True
                    self.minute_warning = False
                    self.second_warning = False
                    return 3
                else:
                    return 0
            return 0

        time_to_intersection = Calculator.time_to_intersection(
                distance_km, ambu_speed, car_speed)
        print ('The vehicles are: ' + str(distance_km) +
                ' kms Appart. Time to intersect: ' + str(time_to_intersection))

        #time to intersection is less than 20 sec, 1/3 of a minute
        if time_to_intersection <= (1/3):
            if not self.second_warning:
                self.second_warning = True
                return 1
            return 0

        if time_to_intersection <= 2:
            if not self.minute_warning:
                self.minute_warning = True
                self.meter_message = False
                return 2
            return 0

    def _is_relevant(self, new_car_pos, car_speed, old_car_pos, 
            new_ambu_pos, ambu_speed, old_ambu_pos):
        '''Takes in the car and the ambulances current and previous postition. 
        Returns whether the car should be notified or not, as a boolean

        Keyword arguments:
        new_car_pos -- A tuple containing the cars current position
                        latitude first, longitude second
        car_speed -- A float containing the cars current speed 
        old_car_pos -- A tuple containing the cars previous position
                        latitude first, longitude second
        new_ambu_pos -- A tuple containing the ambulance current position
                        latitude first, longitude second
        ambu_speed -- A float containing the ambulances current speed
        old_ambu_pos -- A tuple containing the ambulance previous position
                        latitude first, longitude second
        '''

        car_dir = self._find_direction(new_car_pos, old_car_pos)
        ambu_dir = self._find_direction(new_ambu_pos, old_ambu_pos)

        if ambu_speed <= 0:
            return False

        if car_dir != ambu_dir:
            print('Car not going the same direction as ambu')
            return False

        if not self._ambu_behind(new_car_pos, new_ambu_pos, car_dir):
            print ('Ambulance not behind car')
            return False

        distance_km = Calculator.gps_to_kmeters(float(new_car_pos[1]), float(new_car_pos[0]),
               float(new_ambu_pos[1]), float(new_ambu_pos[0]))

        time_to_intersection = Calculator.time_to_intersection(
                distance_km, ambu_speed, car_speed)
        print ('The vehicles are: ' + str(distance_km) +
                ' kms apart. Time to intersect: ' + str(time_to_intersection))

        if time_to_intersection == 0:
            return False

        if time_to_intersection > 2:
            print('Ambulance is too far behind: ' + str(time_to_intersection))
            return False
        return True

    def _find_direction(self, data1, data2):
        '''Find direction for vehicle, returns Direction enum

        Keyword arguments:
        data1 -- tuple with latitude and longitude from newest data
        data2 -- tuple with latitude and longitude from oldest data
        '''

        lat_change = float(data2[0]) - float(data1[0])
        long_change = float(data2[1]) - float(data1[1])

        if lat_change == 0 and long_change == 0:
            return Direction.standing_still
        if fabs(lat_change) > fabs(long_change):
            if lat_change > 0:
                return Direction.north
            return Direction.south
        if long_change > 0:
            return Direction.east
        return Direction.west

    def _ambu_behind(self, car_pos, ambu_pos, direction):
        '''Decide if the ambu is in front of, or behind the car

        Keyword arguments:
        car_pos -- tuple with latitude and longitude from newest data of car
        ambu_pos -- tuple with latitude and longitude from newest data of ambu
        direction -- Direction of the two vehicles. Must be the same after
                        comparing in _is_relevant
        '''

        if direction.name == 'north':
            return car_pos[0] > ambu_pos[0]
        if direction.name == 'south':
            return car_pos[0] < ambu_pos[0]
        if direction.name == 'east':
            return car_pos[1] > ambu_pos[1]
        if direction.name == 'west':
            return car_pos[1] < ambu_pos[1]
        return True
