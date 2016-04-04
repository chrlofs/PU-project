from car.vehicle import Vehicle
from car.process_data import ProcessData


class Main:

    def __init__(self):
        self.ambulance = Vehicle(speed=2)
        self.car = Vehicle(start_ahead=True)
        self.process_data = ProcessData(self.car,self.ambulance)

    def run(self):
        '''Check if receiver has got a new data point, if so process data'''
        print('=========== new run ===============')

        while len(self.car.position_history) > 1 and \
                len(self.ambulance.position_history) > 1:
            old_ambu, new_ambu = self.car.get_data()
            old_car, new_car = self.ambulance.get_data()
            self.process_data.is_relevant(new_car, old_car, new_ambu, old_ambu)

if __name__ == "__main__":
    main = Main()
    main.run()
