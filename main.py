#!/usr/bin/env python3
from car.vehicle import Vehicle
from car.process_data import ProcessData
from car.mapview import MapView
import time
from car.text_to_speech import TextToSpeech

class Main:

    def __init__(self):
        self.amb = Vehicle(speed=10)
        self.car = Vehicle(start_ahead=True)
        self.process_data = ProcessData(self.amb,self.car)
        self.map = MapView()
        self.text_speech = TextToSpeech()

    def run(self):
        '''Check two vehicle objects against each other and process data, show a map with one plot'''

        while len(self.amb.format_position_history)>1 and len(self.car.format_position_history)>1:
            old_ambu, new_ambu = self.amb.get_data()
            self.map.plot_coordinates(old_ambu['longitude'],old_ambu['latitude'],'rs')
            old_car, new_car = self.car.get_data()
            self.map.plot_coordinates(old_car['longitude'], old_car['latitude'],'bs')
            message = self.process_data.pick_message(new_car, old_car, new_ambu, old_ambu)
            self.text_speech.play(message)
            self.map.show_map()
            time.sleep(2)


if __name__ == "__main__":
    main = Main()
    main.run()