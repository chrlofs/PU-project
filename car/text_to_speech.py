import subprocess
import os

class TextToSpeech():

    def __init__(self):
        self.path = '/support/messages/msg'

    def play(self, message_integer):
        if message_integer != 0:
            path = os.path.dirname(os.path.realpath(__file__))
            #os.system('mpg123 play ' + path + self.path + str(message_integer) + '.mp3')
            subprocess.Popen(['mpg123','play', path + self.path + str(message_integer) + '.mp3'], close_fds=True)


