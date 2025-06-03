
import even_numbers

from  unittest import TestCase

class TestEven(TestCase):


	def test_function_exist(self):

		even_numbers.count_even([2,3,4,5,6,7,8,9])


	def test_function_even_number_is_correct(self):

		actual = even_numbers.count_even([2,3,4,5,6,7,8,9])
		expected = 4

		self.assertEqual(actual, expected)


	def test_negative_and_positive_even_number_is_correct(self):

		actual = even_numbers.count_even([2,3,4,5, -6, 7, -8,9, -10])
		expected = 5

		self.assertEqual(actual, expected)




	
		
	
		