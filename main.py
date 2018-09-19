from entertainment_center import favorite_movies
from fresh_tomatoes import open_movies_page

if __name__ == "__main__":
    movies = favorite_movies()
    open_movies_page(movies)
