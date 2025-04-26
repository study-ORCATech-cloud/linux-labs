# LAB01 - File System Navigation Exercises

These exercises will help you practice navigating the Linux file system. Complete each task to build your file system navigation skills.

## Exercise 1: Path Understanding

### TODO:
1. Display the absolute path to your current directory.

2. Identify whether the following paths are absolute or relative:
   - `/home/user/Documents`
   - `../Downloads`
   - `~/Pictures`
   - `Documents/Projects`
   - `/var/log`

## Exercise 2: Directory Creation and Navigation

### TODO:
1. Create the following directory structure in your home directory:
   ```
   lab01_practice/
   ├── dir1/
   │   ├── subdir1/
   │   └── subdir2/
   └── dir2/
       └── subdir3/
   ```

2. Navigate to each created directory using both absolute and relative paths.

3. From inside `subdir2`, navigate to `subdir3` using a relative path.

## Exercise 3: Directory Listing

### TODO:
1. List all files in your home directory, including hidden files.

2. List files showing permissions, ownership, and size.

3. List files sorted by modification time (newest first).

4. List only the directories in your current location.

5. Navigate to `/etc` and list the first 5 configuration files alphabetically.

## Exercise 4: Path Navigation Shortcuts

### TODO:
1. From any directory, navigate directly to your home directory using a shortcut.

2. Navigate to a directory of your choice, then return to the previous directory using a shortcut.

3. Navigate to `/usr/bin`, then to `/var/log` using absolute paths.

4. Navigate from your current location to your home directory and then to the `lab01_practice` directory using relative paths.

## Exercise 5: Cleanup

### TODO:
1. Remove the entire directory structure created in Exercise 2.

2. Verify all directories were successfully removed.

## Bonus Challenge:
Create a hidden directory `.secret` inside your home directory, create a file called `hidden_file.txt` inside it, then navigate to it and verify its contents all using command line only. 