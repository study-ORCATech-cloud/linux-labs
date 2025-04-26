# LAB02 - Users and Permissions Exercises

These exercises will help you practice managing users, groups, and permissions in Linux. Complete each task to build essential system administration skills.

## Exercise 1: User Management

### TODO:
1. Create three new users: `user1`, `user2`, and `user3`.

2. Set passwords for each user.

3. Verify the users were created by examining the `/etc/passwd` file.

4. Check the home directories that were created for these users.

## Exercise 2: Group Management

### TODO:
1. Create two groups: `developers` and `testers`.

2. Add `user1` and `user2` to the `developers` group.

3. Add `user2` and `user3` to the `testers` group (notice `user2` will be in both groups).

4. Verify group memberships for all three users.

## Exercise 3: Understanding File Permissions

### TODO:
1. As your regular user, create a new directory in `/tmp` called `permissions_test`.

2. Inside this directory, create three empty files:
   - `owner_only.txt`
   - `group_only.txt`
   - `everyone.txt`

3. Examine the default permissions of these files.

4. Identify which permission bits represent:
   - Owner permissions
   - Group permissions
   - Others (world) permissions

## Exercise 4: Changing File Permissions

### TODO:
1. Modify permissions for the files you created:
   - Set `owner_only.txt` to be readable and writable only by the owner (no permissions for group or others)
   - Set `group_only.txt` to be readable and writable by the owner and the group, but not by others
   - Set `everyone.txt` to be readable by everyone but writable only by the owner

2. Verify the permissions using both symbolic notation (rwx) and numeric (octal) notation.

3. Try to read and modify each file as your user to confirm the permissions work as expected.

## Exercise 5: Changing Ownership

### TODO:
1. Change the ownership of the files:
   - Change the owner of `owner_only.txt` to `user1`
   - Change the owner and group of `group_only.txt` to `user2` and `developers` respectively
   - Change the group of `everyone.txt` to `testers`

2. Verify the ownership changes.

## Exercise 6: Special Permissions

### TODO:
1. Inside the `permissions_test` directory, create a simple bash script called `test_script.sh` with the following content:
   ```bash
   #!/bin/bash
   echo "This script is running as $(whoami)"
   ```

2. Make the script executable for the owner only.

3. Change the ownership of the script to `user3`.

4. Set the SUID bit on the script so it runs as `user3` regardless of who executes it.

5. Try to execute the script as your regular user and observe the output.

## Exercise 7: Cleanup

### TODO:
1. Remove the test directory and all its contents.

2. Remove the users and groups created in exercises 1 and 2.

3. Verify that all users and groups have been successfully removed.

## Bonus Challenge:
Create a directory structure where different groups have different levels of access to different subdirectories, simulating a shared project environment with separate roles for developers and testers. 