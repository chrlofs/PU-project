import unittest
import sender
import receiver
import json

class TestSenderReceiverMethods(unittest.TestCase):
    '''Tests the different methods in receiver and sender class'''

    def test_list_content(self):
        '''Tests for valid content in the list'''

        self.sender = sender.Sender()
        self.sender.json_list('commute_test.json')
        self.assertTrue(all(p['name'] == "longitude" or p['name'] == "latitude"\
            or p['name'] == "vehicle_speed") for p in self.sender.json_data)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenderReceiverMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
