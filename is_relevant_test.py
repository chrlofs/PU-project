from process_data import ProcessData
import unittest

class TestIsRelevant(unittest.TestCase):
    def test_car_ahead(self):
        '''Car going south, ambu going south. Car ahead of ambu''' 
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind(self):
        '''Car going south, ambu going south. Car behind ambu''' 
        pd = ProcessData()
        res = pd.is_relevant(
                {'longitude' : 38.8888, 'latitude' : 72.1000, 'speed' : 80, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 72.0000, 'speed' : 80, 'time' : 25},
                {'longitude' : 38.8888, 'latitude' : 71.1000, 'speed' : 200, 'time' : 20},
                {'longitude' : 38.8888, 'latitude' : 71.0000, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
