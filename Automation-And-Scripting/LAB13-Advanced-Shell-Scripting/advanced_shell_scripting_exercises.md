# LAB13 - Advanced Shell Scripting Exercises

These exercises will help you develop advanced shell scripting skills. Complete each task to build on your shell scripting foundations.

## Exercise 1: Working with Functions

### TODO:
1. Create a script called `function_library.sh` that contains multiple functions:
   - Add a function called `greeting` that accepts a name parameter and displays a greeting
   - Add a function called `square` that calculates the square of a number
   - Add a function called `check_even_odd` that determines if a number is even or odd
   - Call each function with example values
   - Make the script executable and run it

2. Create a script called `function_return.sh` that demonstrates function return values:
   - Create a function that returns success (0) or failure (1) based on whether a file is executable
   - Create another function that returns a value using echo
   - Implement a function that uses the return value of another function
   - Call your functions with various test cases
   - Make the script executable and run it

## Exercise 2: Advanced Script Arguments

### TODO:
1. Create a script called `process_options.sh` that processes command-line arguments with getopts:
   - Implement a help/usage function
   - Add support for verbose mode (-v)
   - Add options for directory (-d) and filename (-f)
   - Require a message argument after the options
   - Implement functionality that uses the directory and filename options
   - Make the script executable and test it with different option combinations

2. Create a script called `process_all_args.sh` that processes unlimited arguments:
   - Display the total number of arguments
   - Display all arguments as a list
   - Process each argument individually
   - Add a function to check if each argument is a file, directory, or neither
   - Make the script executable and test it with different arguments

## Exercise 3: Error Handling and Debugging

### TODO:
1. Create a script called `robust_script.sh` with comprehensive error handling:
   - Ensure the script exits if any command fails
   - Implement a function to handle errors
   - Set up an error trap
   - Create a function to check if commands exist
   - Implement a function to back up a file with proper error checking
   - Add main script functionality that uses these error handling techniques
   - Make the script executable and test it with various scenarios

2. Create a script called `debug_demo.sh` that demonstrates debugging techniques:
   - Implement functions with potential bugs
   - Use set -x to enable debugging for part of the script
   - Add a function with a common mistake (using -a instead of -e in a test)
   - Make the script executable and run it with and without debugging options

## Exercise 4: Script Best Practices

### TODO:
1. Refactor a poorly written script:
   - Create a file called `bad_script.sh` with the following content:
     ```bash
     #!/bin/bash
     # badly written script
     A=5
     B=10
     C=15
     function F1 {
     echo $1
     }
     function F2 {
     if [ $1 -gt 10 ]
     then
     echo "greater than 10"
     else
     echo "not greater than 10"
     fi
     }
     if [ $A -lt $B ]
     then
     F1 "A is less than B"
     fi
     F2 $C
     F2 $A
     if [ -d /tmp ]; then
     echo "tmp exists"
     fi
     ls /nonexistentfolder
     echo "Script finished"
     ```
   - Create a new file called `good_script.sh` that improves this script by:
     - Using meaningful variable and function names
     - Adding proper indentation and spacing
     - Implementing error handling
     - Adding comments explaining the code
     - Making the script more modular and maintainable

2. Create a script called `secure_script.sh` that follows security best practices:
   - Set a secure PATH
   - Use secure temporary files with proper cleanup
   - Implement input validation
   - Set appropriate umask
   - Quote all variable expansions
   - Avoid using unsafe commands
   - Make the script executable and test it with various inputs

## Exercise 5: Advanced Text Processing

### TODO:
1. Create a script called `text_processor.sh` that combines awk, sed, and grep:
   - Implement a function to extract usernames from /etc/passwd
   - Create a function to count words in a file
   - Add a function to replace text in a file
   - Implement a function to find lines matching a pattern
   - Create a sample text file to test these functions
   - Demonstrate each function in action
   - Include cleanup to remove temporary files
   - Make the script executable and run it

## Bonus Challenge: Create a Full-Featured Script

Create a comprehensive script called `script_analyzer.sh` that combines many of the concepts learned in this lab. This script should:

1. Process multiple command-line options using getopts
2. Implement multiple functions for different operations
3. Include proper error handling and debugging capabilities
4. Process files or directories specified as arguments
5. Generate formatted reports using advanced text processing
6. Follow security and best practice guidelines

For example, you could create a script that analyzes other shell scripts for common issues and best practices, or a system information reporter that collects and displays system information.

## Cleanup

When you've completed all exercises, clean up by creating a cleanup script that removes all the script files created during this lab. 