# LAB12 - Shell Scripting Basics Exercises

These exercises will help you practice writing bash shell scripts to automate tasks. Complete each task to build essential shell scripting skills.

## Exercise 1: Your First Script

### TODO:
1. Create a simple "Hello World" script that outputs a greeting message.

2. Make the script executable.

3. Run the script.

4. Create another script that displays the current date and time.

## Exercise 2: Working with Variables

### TODO:
1. Create a script that uses variables to store:
   - Your name
   - The current directory
   - The number of files in the current directory
   
   Then display this information with appropriate messages.

2. Create a script that asks for user input (name and favorite color) and then displays a personalized message.

3. Create a script that accepts command-line arguments and displays:
   - The script name
   - The first argument
   - The second argument
   - All arguments
   - The number of arguments

## Exercise 3: Conditional Statements

### TODO:
1. Create a script that checks if a file exists. If it does, display a message. If not, create the file.

2. Create a script that prompts for a number and then indicates whether it's:
   - Zero
   - Positive
   - Negative

3. Create a script with nested if statements that asks for the user's age and determines if they are:
   - A minor (under 18)
   - An adult (18 or over)
   - A senior citizen (65 or over)

## Exercise 4: Looping Constructs

### TODO:
1. Create a script with a for loop that:
   - Counts from 1 to 5
   - Lists all files in the current directory

2. Create a script with a while loop that counts from 1 to 5.

3. Create a script with an until loop that counts from 1 to 5.

## Exercise 5: Working with Functions

### TODO:
1. Create a script with a simple function that displays a greeting message.

2. Create a script with a function that takes arguments (a name and a status) and displays a personalized greeting.

3. Create a script with a function that calculates the sum of two numbers and returns the result.

## Exercise 6: Practical Script - File Operations

### TODO:
1. Create a script that backs up a file by:
   - Checking if a filename was provided as an argument
   - Verifying the file exists
   - Creating a backup with the current date in the filename
   - Confirming the backup was successful

## Exercise 7: Debugging and Error Handling

### TODO:
1. Create a script with debugging features that can be enabled by uncommenting a line.

2. Create a script with error handling that:
   - Uses a function to handle errors
   - Creates a temporary directory and file
   - Attempts an operation that will fail (like creating a file in a non-existent directory)
   - Reports the errors properly

## Bonus Challenge:
Create a script called `system_info.sh` that displays:
1. System hostname
2. Current username
3. Operating system information
4. Current memory usage
5. Disk space usage
6. Current processes for the user
7. Network interfaces and IP addresses

Format the output to be easy to read with nice headers and organized information.

## Cleanup

When you've completed all exercises, clean up with:
```
rm *.sh test.txt test_file.txt
``` 