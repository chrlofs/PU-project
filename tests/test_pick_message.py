from car.process_data import ProcessData
import unittest

class TestPickMessage(unittest.TestCase):
    def test_not_relevant(self):
        print('Testing test_not_relevant')
        pd = ProcessData(None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 39.8888, 'speed' : 200},
                {'longitude' : 38.8888, 'latitude' : 39.8889, 'speed' : 200}
            )
         
        self.assertEqual(res, 0)
        
    def test_ambu_20_sec_behind(self):
        print('Testing test_ambu_20_sec_behind')
        pd = ProcessData(None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8887, 'speed' : 200},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 200}
            )
         
        self.assertEqual(res, 1)

    def test_ambu_2_minutes_behind(self):
        print('Testing test_ambu_2_minutes_behind')
        pd = ProcessData(None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8588, 'speed' : 200},
                {'longitude' : 38.8888, 'latitude' : 38.8589, 'speed' : 200}
            )
         
        self.assertEqual(res, 2)

    def test_ambu_just_passed(self):
        print('Testing test_ambu_just_passed')
        pd = ProcessData(None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'speed' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.88881, 'speed' : 200},
                {'longitude' : 38.8888, 'latitude' : 38.8890, 'speed' : 200}
            )
         
        self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()
