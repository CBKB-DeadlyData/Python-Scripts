import os
import shutil

# Read movies.txt
with open('movies.txt', 'r') as f:
    movies_to_delete = f.read().splitlines()

# Path to the directory containing movie folders
path = '/media/sdx1/deadlydata/private/Torrents/Movies'

# Prepare a list for deleted movies
deleted_movies = []

# Iterate over each movie folder in the path
for movie in os.listdir(path):
    # If the movie folder is in the list of movies to delete
    if movie in movies_to_delete:
        # Full path to the movie folder
        full_path = os.path.join(path, movie)
        # Delete the movie folder
        shutil.rmtree(full_path)
        # Add the movie to the list of deleted movies
        deleted_movies.append(movie)

# Write deleted movies to removed.txt
with open('removed.txt', 'w') as f:
    for movie in deleted_movies:
        f.write("{}\n".format(movie))
