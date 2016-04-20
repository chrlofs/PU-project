from car.vehicle import Vehicle
from car.process_data import ProcessData
from car.mapview import MapView
import time
from car.text_to_speech import TextToSpeech

class Main:

    def __init__(self):
# <<<<<<< HEAD
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
# =======
        self.amb = Vehicle(speed=10)
        self.car = Vehicle(start_ahead=True)
        self.process_data = ProcessData(self.amb,self.car)
# >>>>>>> Mapview
        self.map = MapView()
        self.text_speech = TextToSpeech()

    def run(self):
        '''Check two vehicle objects against each other and process data, show a map with one plot'''

        while len(self.amb.format_position_history)>1 and len(self.car.format_position_history)>1:
            old_ambu, new_ambu = self.amb.get_data()
            self.map.plot_coordinates(old_ambu['longitude'],old_ambu['latitude'],'rs')
            old_car, new_car = self.car.get_data()
            self.map.plot_coordinates(old_car['longitude'], old_car['latitude'],'bs')
# <<<<<<< HEAD
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
# =======
            message = self.process_data.pick_message(new_car, old_car, new_ambu, old_ambu)
            self.text_speech.play(message)
            self.map.show_map()
            time.sleep(2)


if __name__ == "__main__":
    main = Main()
    main.run()
# >>>>>>> Mapview
