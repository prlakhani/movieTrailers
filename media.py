''' Define Movie class and backend code to get attributes '''

import webbrowser
from tmdb3 import set_key
from tmdb3 import Movie as theMovie
import os
import datetime

set_key(os.getenv('TMDB_API_KEY'))

class Movie(object):
    
    # VALID_RATINGS=["G","PG","R"]
    def __init__(self, movie_ID):
        self.title = theMovie(movie_ID).title
        self.tagline = theMovie(movie_ID).tagline
        self.release_year = theMovie(movie_ID).releasedate.strftime("%Y")
        self.poster_image_url = theMovie(movie_ID).poster.geturl()
        self.trailer_youtube_url = theMovie(movie_ID).youtube_trailers[0].geturl()
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)