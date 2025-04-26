# LAB01 - File System Navigation Solutions

Below are the solutions to the navigation exercises. Remember to try solving them on your own first!

## Exercise 1: Path Understanding

### Solution:
1. Run the `pwd` command:
   ```bash
   pwd
   ```
   This will show your current absolute path, for example: `/home/username`

2. Path types:
   - `/home/user/Documents` - Absolute path (starts with /)
   - `../Downloads` - Relative path (starts with ..)
   - `~/Pictures` - Relative path (starts with ~ which is a shortcut)
   - `Documents/Projects` - Relative path (starts with directory name)
   - `/var/log` - Absolute path (starts with /)

## Exercise 2: Directory Creation and Navigation

### Solution:
1. Create the directory structure:
   ```bash
   mkdir -p lab01_practice/dir1/subdir1
   mkdir -p lab01_practice/dir1/subdir2
   mkdir -p lab01_practice/dir2/subdir3
   ```

2. Navigate to each directory using absolute and relative paths:
   ```bash
   # Using absolute paths (replace username with your actual username)
   cd /home/username/lab01_practice
   cd /home/username/lab01_practice/dir1
   cd /home/username/lab01_practice/dir1/subdir1
   cd /home/username/lab01_practice/dir1/subdir2
   cd /home/username/lab01_practice/dir2
   cd /home/username/lab01_practice/dir2/subdir3
   
   # Using relative paths (starting from home directory)
   cd ~/lab01_practice
   cd dir1
   cd subdir1
   cd ..
   cd subdir2
   cd ../../dir2
   cd subdir3
   ```

3. From inside subdir2, navigate to subdir3:
   ```bash
   cd ../../dir2/subdir3
   ```

## Exercise 3: Directory Listing

### Solution:
1. List all files including hidden ones:
   ```bash
   ls -a
   ```

2. List files in long format:
   ```bash
   ls -l
   ```

3. List files sorted by modification time:
   ```bash
   ls -lt
   ```

4. List only directories:
   ```bash
   ls -d */
   # Alternative approach
   ls -l | grep ^d
   ```

5. List first 5 configuration files in /etc:
   ```bash
   cd /etc
   ls | sort | head -5
   ```

## Exercise 4: Path Navigation Shortcuts

### Solution:
1. Navigate to home directory:
   ```bash
   cd ~
   # Or simply
   cd
   ```

2. Return to previous directory:
   ```bash
   cd /tmp  # Go somewhere
   cd -     # Return to previous directory
   ```

3. Navigate between absolute paths:
   ```bash
   cd /usr/bin
   cd /var/log
   ```

4. Navigate using relative paths:
   ```bash
   cd ~
   cd lab01_practice
   ```

## Exercise 5: Cleanup

### Solution:
1. Remove the directory structure:
   ```bash
   rm -r ~/lab01_practice
   ```

2. Verify removal:
   ```bash
   ls -la ~ | grep lab01_practice
   ```
   Should return nothing if successfully removed.

## Bonus Challenge Solution:
```bash
mkdir ~/.secret
echo "This is a hidden file" > ~/.secret/hidden_file.txt
cd ~/.secret
cat hidden_file.txt
``` 