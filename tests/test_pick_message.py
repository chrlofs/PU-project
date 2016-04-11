from car.process_data import ProcessData
import unittest

class TestPickMessage(unittest.TestCase):
    def test_not_relevant(self):
        print('Testing test_not_relevant')
        pd = ProcessData(None,None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 39.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 39.8889, 'timestamp' : 81}
            )
         
        self.assertEqual(res, 0)
        
    def test_ambu_20_sec_behind(self):
        print('Testing test_ambu_20_sec_behind')
        pd = ProcessData(None,None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 38.8886, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 81}
            )
         
        self.assertEqual(res, 1)

    def test_ambu_2_minutes_behind(self):
        print('Testing test_ambu_2_minutes_behind')
        pd = ProcessData(None, None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 38.8788, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8790, 'timestamp' : 81}
            )
         
        self.assertEqual(res, 2)

    def test_ambu_just_passed(self):
        print('Testing test_ambu_just_passed')
        pd = ProcessData(None, None)
        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 38.88881, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8890, 'timestamp' : 81}
            )
         
        self.assertEqual(res, 3)

    def test_double_message(self):
        print('Testing double message')
        pd = ProcessData(None, None)

        res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 38.8588, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8589, 'timestamp' : 81}
            )
        second_res = pd.pick_message(
                {'longitude' : 38.8888, 'latitude' : 38.8888, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8889, 'timestamp' : 81},
                {'longitude' : 38.8888, 'latitude' : 38.8588, 'timestamp' : 80},
                {'longitude' : 38.8888, 'latitude' : 38.8589, 'timestamp' : 81}
            )
         
        self.assertEqual(second_res, 0)

if __name__ == '__main__':
    unittest.main()
