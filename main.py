from receiver import Receiver
from process_data import ProcessData
from exit import Exit

class Main:
	
	def __init__(self):
		self.exit = Exit()
		self.receiver = Receiver(self.exit)
		self.process_data = ProcessData(self.receiver)

	def run(self):
		while self.exit.run: 
			self.receiver.update()
			if self.receiver.position_history.qsize() >= 2
			self.process_data.update()



main = Main()
main.run()
print(main.receiver.get_stack())
