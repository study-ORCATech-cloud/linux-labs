# LAB04 - File Searching and Archiving Exercises

These exercises will help you practice finding files and working with archives in Linux. Complete each task to improve your file management skills.

## Exercise 1: Basic File Searching

### TODO:
1. Create a directory called `search_lab` in your home directory.

2. Inside this directory, create the following subdirectories:
   - `documents`
   - `images`
   - `scripts`

3. Create several empty files with various extensions in these directories:
   - In `documents`: `report.txt`, `notes.md`, `plan.txt`
   - In `images`: `photo.jpg`, `diagram.png`, `image.jpg`
   - In `scripts`: `backup.sh`, `update.sh`, `analyze.py`

4. Find all:
   - `.txt` files in the `search_lab` directory
   - Files with the `.sh` extension
   - Files in the `images` directory

## Exercise 2: Advanced File Searching

### TODO:
1. Create additional files with the following content:
   - Add "This is a test file" to `report.txt`
   - Add "The backup runs daily" to `backup.sh`
   - Add "Python script for data analysis" to `analyze.py`

2. Find all files:
   - Modified in the last 5 minutes
   - Smaller than 100 bytes
   - That are executable

3. Search for text in files:
   - Find all files containing the word "backup"
   - Find all files containing the word "test"
   - Search case-insensitively for "python" in all files

## Exercise 3: Basic Tar Archiving

### TODO:
1. Create a tar archive called `documents_backup.tar` containing all files in the `documents` directory.

2. List the contents of the tar archive without extracting it.

3. Extract the archive to a new directory called `documents_restored`.

4. Compare the contents of the original `documents` directory with the `documents_restored` directory.

## Exercise 4: Compression with gzip

### TODO:
1. Compress the `report.txt` file using gzip.

2. Examine the compressed file size compared to the original.

3. Decompress the file.

4. Create a compressed tar archive (tarball) of the entire `images` directory using a single command.

5. Extract the compressed archive to a new location.

## Exercise 5: Working with zip Archives

### TODO:
1. Install the zip/unzip utilities if they're not already installed.

2. Create a zip archive containing all `.sh` scripts.

3. List the contents of the zip archive.

4. Add `analyze.py` to the existing zip archive.

5. Extract only `backup.sh` from the zip archive to a different directory.

## Exercise 6: Finding and Archiving in One Command

### TODO:
1. Create an archive of all `.txt` files in the `search_lab` directory using a combination of commands.

2. Add the string "# Executable script" to the beginning of all `.sh` files.

3. Create a list of all files in the `search_lab` directory sorted by name.

## Exercise 7: Cleanup

### TODO:
1. Create a compressed archive of the entire `search_lab` directory.

2. Remove the original `search_lab` directory and all its contents.

3. Extract the archive to restore the files.

4. Compare the restored directory with the original to ensure everything was preserved.

## Bonus Challenge:
Write a bash script called `search_backup.sh` that accepts two arguments: a search pattern and a backup name. The script should find all files matching the pattern, display them to the user, ask for confirmation, and then create a compressed archive of the matching files. 