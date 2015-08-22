# Define movies to be included on site

import media
import fresh_tomatoes

dune = media.Movie(876)

children_of_dune = media.Movie(192936)

movies=[dune,children_of_dune,]

# Generate html website
fresh_tomatoes.open_movies_page(movies)