from process_data import ProcessData
import unittest

class TestIsRelevant(unittest.TestCase):
    def test_car_ahead(self):
        '''Car going south, ambu going south. Car ahead of ambu''' 
        pd = ProcessData()
        res = pd.is_relevant(
                {'latitude' : 38.8888, 'longitude' : 71.1000, 'speed' : 80, 'time' : 20},
                {'latitude' : 38.8888, 'longitude' : 71.1100, 'speed' : 80, 'time' : 25},
                {'latitude' : 38.8888, 'longitude' : 71.0000, 'speed' : 200, 'time' : 20},
                {'latitude' : 38.8888, 'longitude' : 70.9998, 'speed' : 200, 'time' : 25},
        )
        self.assertTrue(res)

    def test_car_behind(self):
        '''Car going south, ambu going south. Car behind ambu''' 
        pd = ProcessData()
        res = pd.is_relevant(
                {'latitude' : 38.8888, 'longitude' : 71.0000, 'speed' : 80, 'time' : 20},
                {'latitude' : 38.8888, 'longitude' : 70.9998, 'speed' : 80, 'time' : 25},
                {'latitude' : 38.8888, 'longitude' : 71.1000, 'speed' : 200, 'time' : 20},
                {'latitude' : 38.8888, 'longitude' : 71.1100, 'speed' : 200, 'time' : 25},
        )
        self.assertFalse(res)

if __name__ == '__main__':
    print('main')
    unittest.main()
