''' Define movies to be included on site '''

import media
import fresh_tomatoes

# Add movies in this section by looking up ID as explained in README

dune = media.Movie(876)

imitation_game = media.Movie(205596)

blade_runner = media.Movie(78)

two_night_stand = media.Movie(286554)

fight_club = media.Movie(550)

gattaca = media.Movie(782)

movies = [dune, imitation_game, blade_runner,
          two_night_stand, fight_club, gattaca]

# Generate html website
fresh_tomatoes.open_movies_page(movies)
