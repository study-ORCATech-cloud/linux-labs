# LAB05 - Basic Shell Commands Exercises

These exercises will help you practice essential Linux shell commands for file handling and text processing. Complete each task to strengthen your command-line skills.

## Exercise 1: Creating Sample Data Files

### TODO:
1. Create a directory called `shell_lab` in your home directory.

2. Inside this directory, create a file called `users.txt` with the following content:
   ```
   user1:student:1001:Active
   user2:admin:1002:Active
   user3:developer:1003:Inactive
   user4:student:1004:Active
   user5:admin:1005:Inactive
   user6:developer:1006:Active
   ```

3. Create another file called `numbers.txt` with the following content:
   ```
   10
   5
   42
   17
   5
   10
   8
   42
   1
   ```

4. Create a third file called `log.txt` with the following content:
   ```
   2023-10-01 08:15:01 INFO Starting application
   2023-10-01 08:15:03 DEBUG Loading configuration
   2023-10-01 08:15:05 WARNING Config file missing default section
   2023-10-01 08:15:10 ERROR Failed to connect to database
   2023-10-01 08:15:15 ERROR Connection timed out
   2023-10-01 08:16:01 INFO Retrying connection
   2023-10-01 08:16:10 INFO Connected successfully
   2023-10-01 08:16:30 DEBUG User authentication started
   2023-10-01 08:16:35 INFO User logged in
   ```

## Exercise 2: Basic File Viewing Commands

### TODO:
1. Display the entire content of `users.txt`.

2. Display only the first 3 lines of `log.txt`.

3. Display only the last 4 lines of `log.txt`.

4. Display lines 3-5 of `log.txt` using a combination of commands.

5. Count the number of lines, words, and characters in all three files.

## Exercise 3: Text Processing with cut, sort, and uniq

### TODO:
1. Extract only the usernames (first field) from `users.txt`.

2. Extract the roles (second field) from `users.txt`.

3. Extract the roles and arrange them alphabetically.

4. Extract the roles, sort them, and show each role only once.

5. Sort the numbers in `numbers.txt` numerically.

6. Find duplicate numbers in `numbers.txt`.

7. Count how many times each number appears in `numbers.txt`.

## Exercise 4: Working with Log Files

### TODO:
1. Find all ERROR messages in `log.txt`.

2. Find all lines with "INFO" or "DEBUG" messages.

3. Extract only the timestamps (first column) and message levels (third column) from `log.txt`.

4. Count how many ERROR messages are in the log.

5. Create a new file called `errors.txt` that contains only the ERROR lines from `log.txt`.

## Exercise 5: Data Analysis with Shell Commands

### TODO:
1. Create a file showing how many users have each role.

2. Create a new file showing only active users sorted by username.

3. Find the line in `numbers.txt` with the highest number.

4. Calculate the sum of all numbers in `numbers.txt`.

5. Find the average of the numbers in `numbers.txt`.

## Exercise 6: Redirection and Command Chaining

### TODO:
1. Create a file called `system_info.txt` that contains:
   - Current date and time
   - Your username
   - Current working directory
   - Available disk space
   - Memory usage

2. Append the kernel version information to `system_info.txt`.

3. Create a directory called `reports`.

4. Copy all files with "ERROR" content from your current directory to the `reports` directory.

5. Create a single sorted file containing all unique numbers from `numbers.txt` in the `reports` directory.

## Exercise 7: Cleanup

### TODO:
1. Create a compressed archive of the entire `shell_lab` directory.

2. Create a backup directory and move the archive there.

3. Create a script called `cleanup.sh` that would remove all `.txt` files from the `shell_lab` directory.

4. Add a confirmation prompt to the script before deletion.

5. Make the script executable but don't run it (we don't want to delete our files yet).

## Bonus Challenge:
Create a shell script called `log_analyzer.sh` that accepts a log file as an argument and generates a report showing:
1. The total number of log entries
2. Count of entries by message level (INFO, DEBUG, ERROR, WARNING)
3. Chronological list of all ERROR messages
4. The time period covered in the log (earliest to latest timestamp) 