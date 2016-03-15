from car.receiver import Receiver
from car.process_data import ProcessData

class Main:

    def __init__(self):
        self.receiver = Receiver()
        self.process_data = ProcessData(self.receiver)
        self.messages = self.process_data.messages

    def run(self):
        '''Check if receiver has got a new data point, if so process data'''

        while self.exit.run:
            self.receiver.update()
            if self.receiver.position_history.qsize() >= 2:
                old_ambu, new_ambu = self.process_data.get_ambulance_data()
                old_car, new_car = old_ambu, new_car
                print(self.messages[self.process_data.pick_messages(
                    new_car, old_car, new_ambu, old_ambu)])

main = Main()
main.run()
print(main.receiver.get_stack())
