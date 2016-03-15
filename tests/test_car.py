from car.car import Car
import unittest

class test_car(unittest.TestCase):

    def test_data(self):
        print('\nTesting: get and set data')
        self.car = Car()
        self.car.set_data()
        test_car1 = self.car.get_data()
        test_car2 = self.car.get_data()
        self.assertEqual(test_car1[1], test_car2[0])

suite = unittest.TestLoader().loadTestsFromTestCase(test_car)
unittest.TextTestRunner(verbosity=2).run(suite)