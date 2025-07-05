

lists = []
def add_movies(movies):
    lists.append(movies)
    return movies

def add_ratings(ratings):
    if ratings >= 1 and ratings <= 5:
        lists.append(ratings)

"""
def average_rating_for_a_movie(ratings):
    return ratings

def get_average_ratings_of_all_movie(ratings):
    for rating in ratings:
        return rating
"""
