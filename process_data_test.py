import process_data
import unittest

process = process_data.ProcessData()

class TestProcessDataMethods(unittest.TestCase): 

	def test_get_ambulance_data(self):
		dict1 = {longitude: 1010, altitude: 1010, time: 12123123, speed: 120}
		dict2 = {longitude: 1010, altitude: 1010, time: 12123123, speed: 120}
		process.receive.history.put(dict1)
		process.receive.history.put(dict1)
		self.assertEquals(process.receive.history.qsize() == 2)
		self.assertEquals(process.test_get_ambulance_data() == [dict1, dict2])
		self.assertEquals(process.receive.history.qsize() == 1)
