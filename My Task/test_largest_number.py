import largest

from unittest import TestCase

class Testlargest(TestCase):



	def test_check_dat_function_exist(self):

		largest.find_max([2,3,4,5,6,7,8,9])



	def test_largest_number_is_correcct(self):

		actual = largest.find_max([2,3,4,5,6,7,8,9])
		
		expected = 9
		
		self.assertEqual(actual, expected)


	def test_largest_negative_number_is_correcct(self):

		actual = largest.find_max([-2,-3,-4,-5,-6,-7,-8,-9])
		
		expected = -2
		
		self.assertEqual(actual, expected)
	
	