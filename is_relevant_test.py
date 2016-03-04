from process_data import ProcessData
import unittest

class TestIsRelevant(unittest.TestCase):
    
    def test_car_ahead_going_south(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_south(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_north(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_north(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 73.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 73.1000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)
        
    def test_car_ahead_going_east(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 37.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 37.1000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_east(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 39.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 39.1000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def test_car_ahead_going_west(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 39.1000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 39.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind_going_west(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 37.1000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 37.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def opposite_directions_longitude(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.0000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.1000, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

    def opposite_directions_latitude(self):
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
