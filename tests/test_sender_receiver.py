import unittest
import sender
import receiver
import json


class TestSenderReceiverMethods(unittest.TestCase):
    """Tests the different methods in receiver and sender class"""

    def test_list_content(self):
        sender.Sender().json_list('commute_test.json')
        self.assertTrue(all(p['name'] == "longitude" or p['name'] == "latitude" or p['name'] == "vehicle_speed") for p in sender.Sender().json_data)








