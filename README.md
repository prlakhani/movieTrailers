# Udacity Project 1:
## Movie Trailer Website

### Installation: 
1. Clone, or fork and clone, the repository: `git clone git@github.com:prlakhani/udacity_movieTrailers.git`
2. Create a new virtualenv, or simply in your system install, install the single requirement, tmdb3 (a wrapper for The Movie Database API), using the command `pip install -r requirements.txt`
3. If desired, edit the file entertainment_center.py to contain the TMDB IDs for each of the movies you want to display. You will have to manually look these up on the website, but it certainly beats having to manually copy and paste ALL of the relevant details for each movie. The ID can be deduced from the URL of the movie's page on TMDB: it is the number that comes before the first dash in the section of the URL after the last slash.
4. In the activate script for your virtualenv, or in your ~/.bashrc or ~/.bash_profile file, set an environment variable called TMDB_API_KEY containing your unique API key (from your account on the TMDB website), which will allow you to use this API. To do this, add the line `export TMDB_API_KEY = INSERTYOURKEYHERE` to the relevant file for your setup. 
5. Run the entertainment_center.py file from the terminal with `python entertainment_center.py`
6. Enjoy!