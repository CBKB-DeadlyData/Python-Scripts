```
  .,-:::::  :::::::.   :::  .   :::::::.  
,;;;'````'   ;;;'';;'  ;;; .;;,. ;;;'';;' 
[[[          [[[__[[\\. [[[[[/'   [[[__[[\\.
$$$          $$\"\"\"\"Y$$_$$$$,   $$\"\"\"\"Y$$
`88bo,__,o, _88o,,od8P\"888\"88o, _88o,,od8P
  \"YUMMMMMP\"\"\"YUMMMP\"

			 ------
			< hi >
			 ------
			        \   ^__^
			         \  (oo)\_______
			            (__)\       )\/\
			                ||----w | `
			                ||     ||  ` ./$:Color Blind Key Bangers
                                                             -DeadlyData
```


CBKB is a Python script that reads a file containing movie folder names and deletes the corresponding folders in a specified directory.

## Features

- Reads movie names from a file (`movies.txt`).
- Deletes folders in the specified directory (`/Torrents/Movies`) that match the names in the file.
- Handles both empty and non-empty folders.
- Creates a `deleted.txt` file listing the names of the deleted folders.

## Usage

1. Ensure you have Python installed.
2. Clone the repository to your local machine.
3. Update the `movies_directory` variable in the script (`MoviesDirectoryCleaner.py`) with the correct path to your movies directory.
4. Prepare a file named `movies.txt` containing the names of the folders you want to delete.
5. Run the script by executing `python test1.py`.
6. The script will delete the folders and create a `deleted.txt` file listing the deleted folder names.

**Note:** Be cautious when using this script, as it permanently deletes folders and their contents.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute, open issues, or suggest improvements. Happy cleaning!