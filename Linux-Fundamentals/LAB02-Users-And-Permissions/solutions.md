# LAB02 - Users and Permissions Solutions

Below are the solutions to the exercises on managing users, groups, and permissions. Remember to try solving them on your own first!

## Exercise 1: User Management

### Solution:
1. Create three new users:
   ```bash
   sudo useradd user1
   sudo useradd user2
   sudo useradd user3
   ```

2. Set passwords for each user:
   ```bash
   sudo passwd user1
   # Enter and confirm password when prompted
   sudo passwd user2
   # Enter and confirm password when prompted
   sudo passwd user3
   # Enter and confirm password when prompted
   ```

3. Verify users were created:
   ```bash
   grep "user[1-3]" /etc/passwd
   ```

4. Check home directories:
   ```bash
   ls -la /home/user1
   ls -la /home/user2
   ls -la /home/user3
   ```

## Exercise 2: Group Management

### Solution:
1. Create two groups:
   ```bash
   sudo groupadd developers
   sudo groupadd testers
   ```

2. Add users to the developers group:
   ```bash
   sudo usermod -aG developers user1
   sudo usermod -aG developers user2
   ```

3. Add users to the testers group:
   ```bash
   sudo usermod -aG testers user2
   sudo usermod -aG testers user3
   ```

4. Verify group memberships:
   ```bash
   groups user1
   groups user2
   groups user3
   ```
   
   Alternatively, check the `/etc/group` file:
   ```bash
   grep "developers\|testers" /etc/group
   ```

## Exercise 3: Understanding File Permissions

### Solution:
1. Create a test directory:
   ```bash
   mkdir /tmp/permissions_test
   ```

2. Create three empty files:
   ```bash
   touch /tmp/permissions_test/owner_only.txt
   touch /tmp/permissions_test/group_only.txt
   touch /tmp/permissions_test/everyone.txt
   ```

3. Examine default permissions:
   ```bash
   ls -l /tmp/permissions_test/
   ```
   
   Default permissions typically show as `-rw-r--r--` which means:
   - Owner has read and write (rw-)
   - Group has read only (r--)
   - Others have read only (r--)

4. Permission bits representation:
   - First 3 characters after the file type (positions 2-4) represent owner permissions
   - Next 3 characters (positions 5-7) represent group permissions
   - Last 3 characters (positions 8-10) represent others permissions

## Exercise 4: Changing File Permissions

### Solution:
1. Modify permissions:
   ```bash
   # For owner_only.txt - owner can read/write (600)
   chmod 600 /tmp/permissions_test/owner_only.txt
   
   # For group_only.txt - owner and group can read/write (660)
   chmod 660 /tmp/permissions_test/group_only.txt
   
   # For everyone.txt - all can read, only owner can write (644)
   chmod 644 /tmp/permissions_test/everyone.txt
   ```

2. Verify permissions:
   ```bash
   ls -l /tmp/permissions_test/
   ```
   
   - `owner_only.txt` should show `-rw-------` (600)
   - `group_only.txt` should show `-rw-rw----` (660)
   - `everyone.txt` should show `-rw-r--r--` (644)

3. Test permissions:
   ```bash
   # You should be able to read and write to all files
   echo "Test write" > /tmp/permissions_test/owner_only.txt
   cat /tmp/permissions_test/owner_only.txt
   ```

## Exercise 5: Changing Ownership

### Solution:
1. Change ownership:
   ```bash
   # Change owner of owner_only.txt to user1
   sudo chown user1 /tmp/permissions_test/owner_only.txt
   
   # Change owner and group of group_only.txt to user2 and developers
   sudo chown user2:developers /tmp/permissions_test/group_only.txt
   
   # Change group of everyone.txt to testers
   sudo chgrp testers /tmp/permissions_test/everyone.txt
   ```

2. Verify ownership changes:
   ```bash
   ls -l /tmp/permissions_test/
   ```

## Exercise 6: Special Permissions

### Solution:
1. Create a script:
   ```bash
   echo '#!/bin/bash' > /tmp/permissions_test/test_script.sh
   echo 'echo "This script is running as $(whoami)"' >> /tmp/permissions_test/test_script.sh
   ```

2. Make it executable for owner only:
   ```bash
   chmod 700 /tmp/permissions_test/test_script.sh
   ```

3. Change ownership to user3:
   ```bash
   sudo chown user3 /tmp/permissions_test/test_script.sh
   ```

4. Set SUID bit:
   ```bash
   sudo chmod u+s /tmp/permissions_test/test_script.sh
   ```

5. Execute the script:
   ```bash
   /tmp/permissions_test/test_script.sh
   ```
   
   **Note:** For security reasons, modern Linux systems typically don't allow SUID to work on shell scripts. You might see the output showing your user rather than user3. This is a security feature to prevent privilege escalation.

## Exercise 7: Cleanup

### Solution:
1. Remove test directory:
   ```bash
   sudo rm -rf /tmp/permissions_test/
   ```

2. Remove users and groups:
   ```bash
   # Remove users
   sudo userdel user1
   sudo userdel user2
   sudo userdel user3
   
   # Remove home directories if they weren't automatically removed
   sudo rm -rf /home/user1
   sudo rm -rf /home/user2
   sudo rm -rf /home/user3
   
   # Remove groups
   sudo groupdel developers
   sudo groupdel testers
   ```

3. Verify removal:
   ```bash
   # Check users
   grep "user[1-3]" /etc/passwd
   
   # Check groups
   grep "developers\|testers" /etc/group
   
   # Check home directories
   ls -la /home/
   ```

## Bonus Challenge Solution:

Create a project directory structure with different permissions:

```bash
# Create project directories
sudo mkdir -p /opt/project/{code,docs,tests}

# Create groups
sudo groupadd developers
sudo groupadd testers

# Set group ownership
sudo chgrp developers /opt/project/code
sudo chgrp developers /opt/project/docs
sudo chgrp testers /opt/project/tests

# Set directory permissions
# Developers have full access to code and docs
sudo chmod 770 /opt/project/code
sudo chmod 770 /opt/project/docs

# Testers have read-only access to code, full access to tests
sudo chmod 750 /opt/project/code
sudo chmod 770 /opt/project/tests

# Everyone has read access to docs
sudo chmod 775 /opt/project/docs

# Set SGID bit to ensure new files inherit the group
sudo chmod g+s /opt/project/code
sudo chmod g+s /opt/project/docs
sudo chmod g+s /opt/project/tests
``` 