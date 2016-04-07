import os
import time

class TextToSpeech():

    def __init__(self):
        self.path = '/support/messages/msg'

    def play(self, message_integer):
        path = os.path.dirname(os.path.realpath(__file__))
        os.system('mpg123 play ' + path + self.path + str(message_integer) + '.mp3')

