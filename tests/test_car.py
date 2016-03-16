from car.car import Car
import unittest
import json

class test_car(unittest.TestCase):

    def test_data(self):
        '''Tests set_data & get_data'''

        print('\nTesting: get and set data')
        self.car = Car()
        self.car.set_data()
        test_car1 = self.car.get_data()
        test_car2 = self.car.get_data()
        self.assertEqual(test_car1[1], test_car2[0])

    def test_opposite(self):
        '''Tests create_opposite'''

        print('\nTesting: reversed list')
        self.normalcar = Car()
        self.reversedcar = Car('reversed')
        print(self.normalcar.position_history[0])
        print(self.reversedcar.position_history[len(self.reversedcar.position_history)-1])

        #self.assertEqual(self.normalcar.position_history.pop(), self.reversedcar.position_history.popleft())




suite = unittest.TestLoader().loadTestsFromTestCase(test_car)
unittest.TextTestRunner(verbosity=2).run(suite)