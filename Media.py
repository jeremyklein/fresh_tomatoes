class Movie():
    """
        This is the definition of the movie class
    """
    def __init__(self,movie_title, movie_storyline, trailer_youtube, poster_image):
        """
            This is the constructor of the Movie Class 
        """
        self.title=movie_title # This is the title of the movie
        self.storyline=movie_storyline # This is the description of the Movie
        self.poster_image_url=poster_image # This is the poster image
        self.trailer_youtube_url=trailer_youtube # This is a url to the youtube video
