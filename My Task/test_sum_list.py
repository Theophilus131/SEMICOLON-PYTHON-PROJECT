import sum_list

from unittest import TestCase

class Testsum_list(TestCase):

	def test_function_exist(self):
		
		sum_list.sum_list([2,3,4,5,6,7,8,9])

	def test_sum_is_correct(self):
		actual = sum_list.sum_list([2,3,4,5,6,7,8,9])

		expected = 44	

		self.assertEqual(actual, expected) 

	def test_sum_of_floating_numbers_is_correct(self):
		actual = sum_list.sum_list([10.9 + 2.3 + 5.6 + 8.0])

		expected = 26.799999999999997
		self.assertEqual(actual, expected)
	
	def test_all_element_are_zero(self):
		actual = sum_list.sum_list([0, 0, 0, 0])
		
		expected = 0
		self.assertEqual(actual, expected)


	def test_larger_number(self):
		actual = sum_list.sum_list([7777, 88888,999999])
		
		expected = 1096664 
		self.assertEqual(actual, expected)


	def test_mix_of_positive_and_negative_number(self):
		actual = sum_list.sum_list([1, -1, 2, -2])
		
		expected = 0
		self.assertEqual(actual, expected)


	def test_larger_number(self):
		actual = sum_list.sum_list(["1", "2", "3"])
		
		expected = 20
		with self.assertRaises(TypeError)





