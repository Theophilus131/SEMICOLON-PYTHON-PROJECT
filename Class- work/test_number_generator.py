import unittest

import numbers_generator

class MyTestCase(unittest.TestCase):

    def test_that_length_list_is_correct (self):
        self.assertEqual(numbers_generator.length_list([1, 2, 3]), 3)
        self.assertEqual(numbers_generator.length_list([1, 2, 3, 4]), 4)
        self.assertEqual(numbers_generator.length_list([1, 2, 3, 4, 5]), 5)


    def test_sum_element_even_position(self):
        self.assertEqual(numbers_generator.sum_element_even_position([1, 2, 3]), 4)
        self.assertEqual(numbers_generator.sum_element_even_position([1, 2, 3, 4, 6]), 10)

    def test_sum_element_odd_position(self):
        self.assertEqual(numbers_generator.sum_element_odd_position([1, 2, 3]), 2)
        self.assertEqual(numbers_generator.sum_element_odd_position([1, 2, 3, 4]), 6)
        self.assertEqual(numbers_generator.sum_element_odd_position([1, 2, 3, 4, 5]), 6)

    def test_multiply_element_third_position(self):
        self.assertEqual(numbers_generator.multiply_element_third_position([1, 2, 3]), 3)
        self.assertEqual(numbers_generator.multiply_element_third_position([1, 2, 3, 4]), 3)
        self.assertEqual(numbers_generator.multiply_element_third_position([1, 2, 3, 4, 5,7,8, 9, 10, 11]), 210)

    def test_average_element(self):
        self.assertEqual(numbers_generator.average_element([1, 2, 3]), 2)
        self.assertEqual(numbers_generator.average_element([1, 2, 3, 4, 5]), 3)
        self.assertEqual(numbers_generator.average_element([1, 2, 3, 4, 5, 6]), 3.5)

