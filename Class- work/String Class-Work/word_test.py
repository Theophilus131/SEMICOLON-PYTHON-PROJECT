import unittest

import word_replacement


class MyTestCase(unittest.TestCase):
    def test_word_can_be_replaced_in_the_middle(self):

        self.assertEqual("helloce", word_replacement.myFunction("hello","ce"))
        self.assertEqual("theopce", word_replacement.myFunction("theop","ce"))

    def test_when_length_of_word_is_not_equal_the_parameter_appear_at_the_end(self):
        self.assertEqual("testce", word_replacement.myFunction("test","ce"))


if __name__ == '__main__':
    unittest.main()
