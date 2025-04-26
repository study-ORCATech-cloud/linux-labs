# LAB03 - File Editing and Management Exercises

These exercises will help you practice creating, editing, and managing files in Linux. Complete each task to strengthen your file management skills.

## Exercise 1: Creating and Viewing Files

### TODO:
1. Create a new directory called `file_lab` in your home directory.

2. Inside `file_lab`, create an empty file called `sample.txt`.

3. Create another file called `notes.txt` using a text editor of your choice.

4. Add the following text to `notes.txt`:
   ```
   Linux File Management Lab
   =======================
   This file was created for practice purposes.
   Today's date: <insert current date>
   ```

5. View the file's contents using two different commands.

## Exercise 2: Working with Text Editors

### TODO:
1. Open `sample.txt` with a text editor.

2. Add the following content:
   ```
   This is line 1
   This is line 2
   This is line 3
   This is line 4
   This is line 5
   ```

3. Save the file.

4. Navigate to line 3.

5. Delete line 3.

6. Add a new line "This is the NEW line 3" at that position.

7. Save and exit.

8. Verify the content of the file.

## Exercise 3: Using Another Text Editor

### TODO:
1. Open `sample.txt` with a different text editor than you used in Exercise 2.

2. Add a new line at the end: "This line was added with a different editor".

3. Save and quit.

4. Create a new file called `practice.txt` using this text editor.

5. Add five lines of text (your choice).

6. Save and exit.

7. View the contents of the file.

## Exercise 4: Copying and Moving Files

### TODO:
1. Create a new subdirectory called `backup` inside `file_lab`.

2. Copy `sample.txt` to the `backup` directory.

3. Create a new subdirectory called `documents`.

4. Move `notes.txt` to the `documents` directory.

5. Create a duplicate of `practice.txt` called `practice_copy.txt` in the current directory.

6. Verify the files are in the expected locations.

## Exercise 5: Working with File Content

### TODO:
1. Create a new file called `combined.txt`.

2. Concatenate the contents of `sample.txt` and `practice.txt` into `combined.txt`.

3. Create a new file containing only the first 3 lines of `combined.txt` called `first_three.txt`.

4. Create a new file containing only the last 3 lines of `combined.txt` called `last_three.txt`.

5. Count the number of lines, words, and characters in `combined.txt`.

## Exercise 6: Finding and Comparing Files

### TODO:
1. Edit the backup copy of `sample.txt` to make it slightly different from the original.

2. Compare the original and backup versions.

3. Find all `.txt` files in the `file_lab` directory and its subdirectories.

4. Find all files containing the word "line" in the `file_lab` directory.

## Exercise 7: Cleanup

### TODO:
1. Create a new directory called `archive` in your home directory.

2. Move the entire `file_lab` directory into the `archive` directory.

3. Navigate to your home directory.

4. Delete the `archive` directory and all its contents using a single command.

## Bonus Challenge:
Create a bash script called `file_report.sh` that accepts a directory path as an argument and produces a report showing the number of files, their types, and total size. Test the script on the directories you created in these exercises. 