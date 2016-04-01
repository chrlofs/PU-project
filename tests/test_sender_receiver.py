import unittest
from ambulance.sender import Sender
import car.receiver
import json

class TestSenderReceiverMethods(unittest.TestCase):
    '''Tests the different methods in receiver and sender class'''

    def test_list_content(self):
        '''Tests for valid content in the list'''

        self.sender = Sender()
        self.sender.json_list('ambulance/testdata/commute_test.json')
        self.assertTrue(all(p['name'] == "longitude" or p['name'] == "latitude"\
            or p['name'] == "vehicle_speed") for p in self.sender.json_data)
        self.sender.sock.close()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenderReceiverMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
