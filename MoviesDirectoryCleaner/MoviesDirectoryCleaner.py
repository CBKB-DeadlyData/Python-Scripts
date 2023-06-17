import os
import shutil

movies_directory = "/deadlydata/private/Torrents/Movies"
movies_file = "movies.txt"
deleted_file = "deleted.txt"

# Read the movie names from the file
with open(movies_file, "r") as file:
    movie_names = file.read().splitlines()

# Iterate over the movie names and delete matching folders
deleted_folders = []
for movie_name in movie_names:
    movie_directory = os.path.join(movies_directory, movie_name)
    if os.path.exists(movie_directory) and os.path.isdir(movie_directory):
        print("Deleting folder: {}".format(movie_directory))
        shutil.rmtree(movie_directory, ignore_errors=True, onerror=lambda *args: None)
        deleted_folders.append(movie_name)

# Write the deleted folder names to the file
with open(deleted_file, "w") as file:
    for folder_name in deleted_folders:
        file.write(folder_name + "\n")
