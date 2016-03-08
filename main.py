from receiver import Receiver
from process_data import ProcessData
from exit import Exit


class Main:

	def __init__(self):
		self.receiver = Receiver(exit)
		self.process_data = ProcessData(self.receiver)

	def run(self):
		'''Check if receiver has got a new data point, if so process data'''

		while self.exit.run:
			self.receiver.update()
			if self.receiver.position_history.qsize() >= 2:
				old_ambu, new_ambu = self.process_data.get_ambulance_data()
				old_car, new_car = old_ambu, new_car
				self.process_data.is_relevant(new_car, old_car, new_ambu, old_ambu)


main = Main()
main.run()
print(main.receiver.get_stack())
