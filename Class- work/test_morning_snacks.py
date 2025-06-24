import morning_snacks
import unittest


class MyTestCase(unittest.TestCase):
    def test_third_element_in_list_is_correct(self):
        self.assertEqual(morning_snacks.my_function([10, 20, 100, 40, 50]), 100)
        self.assertEqual(morning_snacks.my_function([1, 2, 3, 4, 5, 6]), 3)

    def test_that_element_in_the_last_index_is_chnaged(self):
        self.assertEqual(morning_snacks.my_function2(['red', 'green', 'blue']), ['red', 'green', 'yellow'])

    def test_that_element_removed_is_correct(self):
        self.assertEqual(morning_snacks.my_function4([1, 2, 3, 4, 5, 6, 7, 8]), None)

    def test_that_element_is_correct(self):
        self.assertEqual(morning_snacks.my_function5(['Alice']), 5)
        self.assertEqual(morning_snacks.my_function5(['Bob']), 3)
        self.assertEqual(morning_snacks.my_function5(['Theophilus']), 10)

    def test_that_asecnding_other_number_is_correct(self):
        self.assertEqual(morning_snacks.my_function6([4, 1, 3, 9, 2]), [1, 2, 3, 4, 9])
        self.assertEqual(morning_snacks.my_function6([90, 100, 200, 20, 60, 70]), [20, 60, 70, 90, 100, 200])

    def test_even_number_is_correct(self):
        self.assertEqual(morning_snacks.my_function7([1, 2, 3, 4, 5, 20]), None)



if __name__ == '__main__':
    unittest.main()
