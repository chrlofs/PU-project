from process_data import ProcessData
import unittest


class TestProcessDataMethods(unittest.TestCase):

	def test_get_data_from_stack(self):
		"""Add data to Receiver and get data with get_ambulance_data()"""
		process = ProcessData()
		dict1 = {longitude: 101010, altitude: 101010, time: 12123123, speed: 12}
		dict2 = {longitude: 101020, altitude: 101020, time: 12123123, speed: 30}
		process.receive.history.put(dict1)
		process.receive.history.put(dict2)
		self.assertEquals(process.receive.history.qsize() == 2)
		self.assertEquals(process.test_get_ambulance_data() == [dict1, dict2])
		self.assertEquals(process.receive.history.qsize() == 1)

	def test_empty_stack(self):
		process = process_data.ProcessData()
		self.assertEquals(process.receive.history.qsize() == 0)

if __name__ == "__main__":
	unittest.main()
