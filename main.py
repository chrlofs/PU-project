#!/usr/bin/env python3
from car.vehicle import Vehicle
from car.process_data import ProcessData
from car.GPS_GUI import Carmap


class Main:

    def __init__(self):
        self.vechicle1 = Vehicle(start_ahead=True)
        self.vechicle2 = Vehicle(speed=3)
        self.process_data = ProcessData(self.vechicle1,self.vechicle2)
        self.map = Carmap()

    def run(self):
        '''Check if receiver has got a new data point, if so process data'''

        while len(self.vechicle1.position_history) >1 and len(self.vechicle2.position_history) > 1:
            old_ambu, new_ambu = self.vechicle1.get_data()
            self.map.plot(old_ambu['longitude'], old_ambu['latitude'], 'ro')
            old_car, new_car = self.vechicle2.get_data()
            self.map.plot(old_car['longitude'], old_car['latitude'], 'bo')
            self.process_data.is_relevant(new_car, old_car, new_ambu, old_ambu)
        self.map.show()

if __name__ == "__main__":
    main = Main()
    main.run()
