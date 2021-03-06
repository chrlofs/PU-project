from car.vehicle import Vehicle
import unittest
import json

class test_car(unittest.TestCase):

    def test_data(self):
        '''Tests set_data & get_data'''

        print('\nTesting: get and set data')
        self.vehicle = Vehicle()
        self.vehicle.json_list('car/start_ahead.json')
        test_car1 = self.vehicle.get_data()
        test_car2 = self.vehicle.get_data()
        self.assertEqual(test_car1[1], test_car2[0])


suite = unittest.TestLoader().loadTestsFromTestCase(test_car)
unittest.TextTestRunner(verbosity=2).run(suite)