#!/usr/bin/env python3
from car.vehicle import Vehicle
from car.process_data import ProcessData


class Main:

    def __init__(self):
        self.vechicle2 = Vehicle(speed=2)
        self.vechicle1 = Vehicle(start_ahead=True)
        self.process_data = ProcessData(self.vechicle1,self.vechicle2)

    def run(self):
        '''Check if receiver has got a new data point, if so process data'''
        print('=========== new run ===============')

        while len(self.vechicle1.position_history) > 1 and \
                len(self.vechicle2.position_history) > 1:
            old_ambu, new_ambu = self.vechicle1.get_data()
            old_car, new_car = self.vechicle2.get_data()
            self.process_data.is_relevant(new_car, old_car, new_ambu, old_ambu)

if __name__ == "__main__":
    main = Main()
    main.run()
