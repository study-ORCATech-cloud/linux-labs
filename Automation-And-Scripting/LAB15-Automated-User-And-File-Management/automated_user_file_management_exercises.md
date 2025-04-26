# LAB15 - Automated User and File Management Exercises

These exercises will help you develop scripts to automate common Linux system administration tasks. Complete each task to strengthen your automation skills.

## Exercise 1: Basic User Management Script

### TODO:
1. Create a script called `user_creator.sh` that:
   - Accepts a username as a command-line argument
   - Creates a new user with that username
   - Creates a home directory for the user
   - Sets appropriate ownership and permissions on the home directory
   - Provides appropriate error messages if the username is not provided

2. Make the script executable.

3. Execute the script to create a test user (note: you may need root/sudo privileges).

4. Verify that the user was created correctly by checking `/etc/passwd` and the home directory.

5. Test the script's error handling by running it without specifying a username.

## Exercise 2: Enhanced User Management

### TODO:
1. Create an enhanced version of your script called `user_manager.sh` that:
   - Creates users with customizable home directory paths
   - Sets a random temporary password for the new user
   - Enforces password change on first login
   - Adds the user to specified groups
   - Records user creation in a log file

2. Add a feature to check if the username already exists before attempting to create it.

3. Add command-line options for different features using getopts.

4. Test the script with various combinations of options.

5. Implement proper error handling and usage information.

## Exercise 3: Batch User Management

### TODO:
1. Create a script called `batch_user_creator.sh` that:
   - Reads a CSV file containing user information (username, groups, home directory)
   - Creates multiple users based on this information
   - Reports success or failure for each user creation

2. Create a sample CSV file with at least 5 test users.

3. Add validation for the CSV file format.

4. Implement error handling that continues processing other users even if one fails.

5. Add a summary report at the end showing how many users were successfully created and how many failed.

## Exercise 4: User Environment Setup

### TODO:
1. Create a script called `user_env_setup.sh` that:
   - Sets up a complete environment for a new user
   - Creates standard directories inside the user's home (Documents, Projects, etc.)
   - Copies skeleton configuration files (.bashrc, .bash_profile, etc.)
   - Creates customized welcome message

2. Modify the script to accept customization options via command-line arguments.

3. Add a feature to apply different templates based on user role (developer, admin, standard).

4. Test the script with different user roles.

5. Add logging of all actions performed by the script.

## Exercise 5: File Permission Management

### TODO:
1. Create a script called `permission_manager.sh` that:
   - Recursively applies specified permissions to a directory
   - Handles files and directories differently
   - Preserves special permissions or applies them as needed

2. Add features to:
   - Change ownership of files and directories
   - Set default permissions for new files created in the directory
   - Apply special permissions (setuid, setgid, sticky bit) selectively

3. Include safety checks to prevent accidental permission changes on system directories.

4. Test the script on a test directory with various file types.

5. Add a dry-run option that shows what changes would be made without actually making them.

## Exercise 6: File System Cleanup

### TODO:
1. Create a script called `filesystem_cleanup.sh` that:
   - Finds and lists files larger than a specified size
   - Identifies directories consuming the most space
   - Locates files that haven't been accessed in a given time period
   - Provides options to archive or delete old files

2. Add safety features to prevent accidental deletion of important files.

3. Implement a confirmation prompt before performing destructive actions.

4. Add logging of all actions performed by the script.

5. Test the script on a test directory with various file types and timestamps.

## Exercise 7: Cleanup

### TODO:
1. Create a cleanup script called `lab_cleanup.sh` that:
   - Removes test users created during the lab
   - Removes test directories
   - Restores any system files that were modified

2. Ensure all cleanup operations check if the resource exists before attempting removal.

3. Test the cleanup script on your system.

4. Add confirmations before performing destructive actions.

## Bonus Challenge:
Create a comprehensive system initialization script called `system_init.sh` that:
- Sets up a new Linux system with multiple users
- Configures appropriate groups and permissions
- Creates project directories with the correct sharing permissions
- Sets up scheduled backups of important directories
- Implements proper logging of all actions
- Includes error handling and detailed reporting

This script should consolidate everything you've learned in the lab into a single, robust utility. 