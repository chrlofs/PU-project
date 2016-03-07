import unittest
import Sender
import Receiver
import json

class TestSenderReceiverMethods(unittest.TestCase):
    """Tests the different methods in receiver and sender class"""
    receiver = Receiver()
    sender = Sender()
    commute_test = ""

    sender.json_list("commute_test.json")

    print(sender.assertEquals(all(p == "longitude" or p == "latitude" or p == "vehicle_speed") for p in sender.json_data["name"]))









