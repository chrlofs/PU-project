import process_data
import unittest

process = process_data.ProcessData()

class TestProcessDataMethods(unittest.TestCase): 

	def test_get_ambulance_data(self):
		self.assert