from car.vehicle import Vehicle
from car.process_data import ProcessData
from car.mapview import MapView
import gmaps



class Main:

    def __init__(self):
# <<<<<<< HEAD
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
# =======
        self.vechicle1 = Vehicle(start_ahead=True)
        self.vechicle2 = Vehicle(speed=3)
        self.process_data = ProcessData(self.vechicle1,self.vechicle2)
        self.map = MapView()


    def run(self):
        '''Check if receiver has got a new data point, if so process data'''

        count = 0

        while len(self.vechicle1.position_history) >1 and len(self.vechicle2.position_history) > 1:
            old_ambu, new_ambu = self.vechicle1.get_data()
            self.map.plot_coordinates(old_ambu['longitude'],old_ambu['latitude'],'rs')
            old_car, new_car = self.vechicle2.get_data()
            self.map.plot_coordinates(old_car['longitude'], old_car['latitude'],'bs')
            self.process_data.is_relevant(new_car, old_car, new_ambu, old_ambu)
        self.map.show_map()
            # if count == 10:
            #     print(count)
            #     count = 0
            #
            #
            # count += 1
# >>>>>>> Mapview

if __name__ == "__main__":
    main = Main()
    main.run()
