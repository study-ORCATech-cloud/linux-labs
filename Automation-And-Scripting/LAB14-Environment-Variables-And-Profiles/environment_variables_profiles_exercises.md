# LAB14 - Environment Variables and Profiles Exercises

These exercises will help you understand how environment variables and profile files manage user sessions and system configuration in Linux. Complete each task to strengthen your system customization skills.

## Exercise 1: Understanding Environment Variables

### TODO:
1. Display all current environment variables in your shell.

2. Display only the PATH environment variable and count how many directories it contains.

3. Display the current shell you are using (hint: look for a specific environment variable).

4. Find which environment variables store your username and home directory.

5. Find where the system stores temporary files using an environment variable.

## Exercise 2: Creating and Using Environment Variables

### TODO:
1. Create a temporary environment variable called `MY_NAME` with your name as its value.

2. Create another temporary environment variable called `CURRENT_PROJECT` with the value "Linux Environment Lab".

3. Create a third environment variable called `PROJECT_PATH` that points to a directory called `projects` in your home directory.

4. Write a command that displays a message using all three variables, like "Hello, {MY_NAME}! You are working on {CURRENT_PROJECT} in {PROJECT_PATH}".

5. Create a new shell session (open a new terminal) and check if your variables still exist. Explain the result.

## Exercise 3: Making Environment Variables Permanent

### TODO:
1. Edit your `.bashrc` file to add the three environment variables from Exercise 2.

2. Create a new environment variable in `.bashrc` called `BACKUP_DIR` that points to a directory called `backups` in your home directory.

3. Make the necessary changes for the environment variables to be available immediately without logging out.

4. Verify that your environment variables are properly set.

5. Create a new shell session and verify that your environment variables are still available.

## Exercise 4: Understanding Profile Files

### TODO:
1. Identify and list all the profile files in your home directory (hint: look for hidden files).

2. Examine the `/etc/profile` file and write a brief summary of its purpose.

3. Compare the content and purpose of `.bash_profile`, `.profile`, and `.bashrc` files.

4. Determine which profile files are executed when you log in and which are executed when you start a new shell.

5. Create a small shell script in your home directory that prints "Profile files lab completed" and add a line to your `.bashrc` file to execute this script each time you open a new terminal.

## Exercise 5: PATH Management

### TODO:
1. Create a directory called `bin` in your home directory if it doesn't already exist.

2. Add this directory to your PATH environment variable permanently (in your profile files).

3. Create a simple shell script called `hello` in your `~/bin` directory that prints a greeting message.

4. Make the script executable.

5. Test the script by simply typing `hello` in any directory without specifying the path.

## Exercise 6: Custom Shell Prompt

### TODO:
1. Examine your current prompt by checking the PS1 environment variable.

2. Modify your `.bashrc` file to create a custom prompt that includes:
   - Your username
   - The current directory
   - The current time
   - A different color for the prompt text

3. Apply the changes to your current session.

4. Create another custom prompt that shows the current working directory, the number of files in the current directory, and the exit status of the last command.

5. Test your custom prompts in different directories.

## Exercise 7: Cleanup

### TODO:
1. Create a backup of your modified profile files.

2. Remove any temporary environment variables you created.

3. If desired, restore your original prompt settings.

4. Keep or remove the permanent environment variables as you prefer.

## Bonus Challenge:
Create a script called `env_manager.sh` that can:
- List all environment variables
- Add a new environment variable permanently to the appropriate profile file
- Remove an environment variable from profile files
- Search for specific environment variables
- Create backups of profile files before making changes 