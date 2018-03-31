# This is our Movie class and blueprint file.
# It allows us to create movie objects.


class Movie():
    """
    The Movie class creates Movies objects.
    It takes in key information about a movies, as a series of arguments.

    Args:
        movie_title (str): The name of the movie.
        movie_storyline (str): A short description of the movie's storyline.
        movie_poster_image (str): URL link to the movie's cover image.
        movie_trailer (str): Youtube URL link to the movie trailer.

    Attributes:
        title (str): The name of the moview.
        storyline (str): A short description of the storyline.
        poster_image_url (str): URL link to the movie's cover image.
        trailer_youtube_url (str):  Youtube shortlink tp the movie trailer.
    """
    def __init__(
            self,
            movie_title,
            movie_storyline,
            movie_poster_image,
            movie_trailer):

            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = movie_poster_image
            self.trailer_youtube_url = movie_trailer
