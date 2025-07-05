import unittest

import movie_rating

class MyTestCase(unittest.TestCase):
    def test_movies_can_be_added_Succefully(self):
        movie_rating.add_movies("avater")
        self.assertEqual("avater", movie_rating.add_movies("avater"))
        movie_rating.add_movies("bingo")
        self.assertEqual("bingo", movie_rating.add_movies("bingo"))

    def test_movie_can_be_rated(self):
        self.assertEqual(movie_rating.add_ratings(1))







if __name__ == '__main__':
    unittest.main()