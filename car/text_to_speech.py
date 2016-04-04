import os

class TextToSpeech():

	def __init__(self):
		self.path = 'messages/msg'


	def play(self, message_integer):
		os.system('start ' + self.path + str(message_integer))
