from receiver import Receiver
from process_data import ProcessData
from exit import Exit

class Main:
	
	def __init__(self):
		self.exit = Exit()
		self.receiver = Receiver(self.exit)
		self.process_data = ProcessData(self.receiver)

	def run(self):
		while True: 
			self.receiver.update()
			self.process_data.update()



main = Main()
main.run()
