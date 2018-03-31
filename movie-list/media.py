# This is our Movie class and blueprint file.
# It allows us to create movie objects.


class Movie():
    # This initializes the Movie object.
    # It takes movie information in as arguments.
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
