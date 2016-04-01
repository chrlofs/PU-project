from car.process_data import ProcessData
from car.vehicle import Vehicle
import unittest

class TestIsRelevant(unittest.TestCase):

    def test_same_coordinates(self):
        print('\nTesting: ' + 'test_same_coordinates')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_south(self):
        print('\nTesting: ' + 'test_car_ahead_going_south')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_south(self):
        print('\nTesting: ' + 'test_car_behind_going_south')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.9998, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9997, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_north(self):
        print('\nTesting: ' + 'test_car_ahead_going_north')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_north(self):
        print('\nTesting: ' + 'test_car_behind_going_north')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0002, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0003, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_east(self):
        print('\nTesting: ' + 'test_car_ahead_going_east')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 37.9999, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_east(self):
        print('\nTesting: ' + 'test_car_behind_going_east')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.0002, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.0003, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_west(self):
        print('\nTesting: ' + 'test_car_ahead_going_west')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.0003, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.0002, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_west(self):
        print('\nTesting: ' + 'test_car_behind_going_west')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 37.9999, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 37.9998, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_opposite_directions_longitude(self):
        print('\nTesting: ' + 'test_opposite_directions_longitude')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_opposite_directions_latitude(self):
        print('\nTesting: ' + 'test_opposite_directions_latitude')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

    def test_car_too_far_behind(self):
        print('\nTesting: ' + 'test_car_too_far_behind')
        pd = ProcessData(Vehicle(), Vehicle())
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'vehicle_speed' : 80, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'vehicle_speed' : 80, 'timestamp' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'vehicle_speed' : 200, 'timestamp' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'vehicle_speed' : 200, 'timestamp' : 25},
        )
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
