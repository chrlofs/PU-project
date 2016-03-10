from car.process_data import ProcessData
import unittest

class TestIsRelevant(unittest.TestCase):

    def test_same_coordinates(self):
        print('\nTesting: ' + 'test_same_coordinates')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_south(self):
        print('\nTesting: ' + 'test_car_ahead_going_south')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_south(self):
        print('\nTesting: ' + 'test_car_behind_going_south')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.9998, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.9997, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_north(self):
        print('\nTesting: ' + 'test_car_ahead_going_north')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.9999, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_north(self):
        print('\nTesting: ' + 'test_car_behind_going_north')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0002, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0003, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_east(self):
        print('\nTesting: ' + 'test_car_ahead_going_east')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 37.9999, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_east(self):
        print('\nTesting: ' + 'test_car_behind_going_east')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.0002, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.0003, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_west(self):
        print('\nTesting: ' + 'test_car_ahead_going_west')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.0003, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.0002, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_west(self):
        print('\nTesting: ' + 'test_car_behind_going_west')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 37.9999, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 37.9998, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_opposite_directions_longitude(self):
        print('\nTesting: ' + 'test_opposite_directions_longitude')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.0001, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_opposite_directions_latitude(self):
        print('\nTesting: ' + 'test_opposite_directions_latitude')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_too_far_behind(self):
        print('\nTesting: ' + 'test_car_too_far_behind')
        pd = ProcessData(None)
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.0001, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.0001, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()