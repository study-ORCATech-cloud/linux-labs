# LAB04 - File Searching and Archiving Solutions

Below are the solutions to the file searching and archiving exercises. Remember to try solving them on your own first!

## Exercise 1: Basic File Searching

### Solution:
1. Create the directory structure:
   ```bash
   mkdir -p ~/search_lab/{documents,images,scripts}
   ```

2. Create files in the directories:
   ```bash
   # Create files in documents
   touch ~/search_lab/documents/report.txt
   touch ~/search_lab/documents/notes.md
   touch ~/search_lab/documents/plan.txt
   
   # Create files in images
   touch ~/search_lab/images/photo.jpg
   touch ~/search_lab/images/diagram.png
   touch ~/search_lab/images/image.jpg
   
   # Create files in scripts
   touch ~/search_lab/scripts/backup.sh
   touch ~/search_lab/scripts/update.sh
   touch ~/search_lab/scripts/analyze.py
   ```

3. Use find to locate files:
   ```bash
   # Find all .txt files
   find ~/search_lab -name "*.txt"
   
   # Find all .sh files
   find ~/search_lab -name "*.sh"
   
   # Find all files in images directory
   find ~/search_lab/images -type f
   ```

## Exercise 2: Advanced File Searching

### Solution:
1. Add content to files:
   ```bash
   echo "This is a test file" > ~/search_lab/documents/report.txt
   echo "The backup runs daily" > ~/search_lab/scripts/backup.sh
   echo "Python script for data analysis" > ~/search_lab/scripts/analyze.py
   ```

2. Advanced find commands:
   ```bash
   # Find files modified in the last 5 minutes
   find ~/search_lab -type f -mmin -5
   
   # Find files smaller than 100 bytes
   find ~/search_lab -type f -size -100c
   
   # Find executable files
   find ~/search_lab -type f -executable
   
   # If no files are executable yet, make some executable
   chmod +x ~/search_lab/scripts/*.sh
   ```

3. Grep for content:
   ```bash
   # Find files containing "backup"
   grep -r "backup" ~/search_lab
   
   # Find files containing "test"
   grep -r "test" ~/search_lab
   
   # Case-insensitive search for "python"
   grep -ri "python" ~/search_lab
   ```

## Exercise 3: Basic Tar Archiving

### Solution:
1. Create tar archive:
   ```bash
   tar -cvf ~/documents_backup.tar ~/search_lab/documents
   ```

2. List contents without extracting:
   ```bash
   tar -tvf ~/documents_backup.tar
   ```

3. Extract to new directory:
   ```bash
   mkdir ~/documents_restored
   tar -xvf ~/documents_backup.tar -C ~/documents_restored
   ```

4. Compare contents:
   ```bash
   # Using diff to compare directories
   diff -r ~/search_lab/documents ~/documents_restored/home/$USER/search_lab/documents
   
   # Or list both directories and compare visually
   ls -la ~/search_lab/documents
   ls -la ~/documents_restored/home/$USER/search_lab/documents
   ```

## Exercise 4: Compression with gzip

### Solution:
1. Compress file with gzip:
   ```bash
   gzip -c ~/search_lab/documents/report.txt > ~/search_lab/documents/report.txt.gz
   # Or to replace the original
   # cp ~/search_lab/documents/report.txt ~/search_lab/documents/report.txt.bak
   # gzip ~/search_lab/documents/report.txt
   ```

2. Compare file sizes:
   ```bash
   ls -lh ~/search_lab/documents/report.txt.bak
   ls -lh ~/search_lab/documents/report.txt.gz
   ```

3. Decompress the file:
   ```bash
   gunzip -c ~/search_lab/documents/report.txt.gz > ~/search_lab/documents/report.txt.restored
   # Or to restore in place (if original was compressed):
   # gunzip ~/search_lab/documents/report.txt.gz
   ```

4. Create compressed tarball:
   ```bash
   tar -czvf ~/images_backup.tar.gz ~/search_lab/images
   ```

5. Extract compressed tarball:
   ```bash
   mkdir ~/images_restored
   tar -xzvf ~/images_backup.tar.gz -C ~/images_restored
   ```

## Exercise 5: Working with zip Archives

### Solution:
1. Install zip/unzip if needed:
   ```bash
   # On Debian/Ubuntu
   sudo apt-get install zip unzip
   
   # On RHEL/CentOS
   sudo yum install zip unzip
   ```

2. Create zip archive:
   ```bash
   zip ~/scripts_backup.zip ~/search_lab/scripts/*.sh
   ```

3. List contents:
   ```bash
   unzip -l ~/scripts_backup.zip
   ```

4. Add a file to existing archive:
   ```bash
   zip -u ~/scripts_backup.zip ~/search_lab/scripts/analyze.py
   ```

5. Extract specific file:
   ```bash
   mkdir ~/specific_restore
   unzip ~/scripts_backup.zip "*/backup.sh" -d ~/specific_restore
   ```

## Exercise 6: Finding and Archiving in One Command

### Solution:
1. Create tar with find results:
   ```bash
   find ~/search_lab -name "*.txt" | tar -cvf ~/txt_files.tar -T -
   ```

2. Add text to script files with find -exec:
   ```bash
   find ~/search_lab -name "*.sh" -exec sed -i '1i # Executable script' {} \;
   ```

3. Create sorted file list:
   ```bash
   find ~/search_lab -type f | sort > ~/search_lab_files.txt
   ```

## Exercise 7: Cleanup

### Solution:
1. Create compressed archive:
   ```bash
   tar -czvf ~/search_lab_backup.tar.gz ~/search_lab
   ```

2. Remove directory:
   ```bash
   rm -rf ~/search_lab
   ```

3. Extract archive:
   ```bash
   tar -xzvf ~/search_lab_backup.tar.gz -C ~
   ```

4. Compare (use one of these methods):
   ```bash
   # If you have a previous list of files
   find ~/search_lab -type f | sort > ~/search_lab_files_new.txt
   diff ~/search_lab_files.txt ~/search_lab_files_new.txt
   
   # Or just check if all expected files exist
   find ~/search_lab -type f -name "*.txt" | wc -l  # Should show the right number
   find ~/search_lab -type f -name "*.sh" | wc -l   # Should show the right number
   ```

## Bonus Challenge Solution:

```bash
#!/bin/bash

# Check if correct number of arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <search_pattern> <backup_name>"
    exit 1
fi

PATTERN="$1"
BACKUP_NAME="$2"

# Find matching files
echo "Searching for files matching pattern: $PATTERN"
MATCHING_FILES=$(find ~ -name "$PATTERN" -type f)

# Check if any files found
if [ -z "$MATCHING_FILES" ]; then
    echo "No files found matching the pattern."
    exit 1
fi

# Display matching files
echo "Found the following matching files:"
echo "$MATCHING_FILES" | while read -r file; do
    echo "- $file"
done

# Ask for confirmation
read -p "Create archive of these files? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "Operation cancelled."
    exit 0
fi

# Create archive directory if it doesn't exist
ARCHIVE_DIR=~/archives
mkdir -p $ARCHIVE_DIR

# Create the archive
ARCHIVE_PATH="$ARCHIVE_DIR/${BACKUP_NAME}.tar.gz"
echo "$MATCHING_FILES" | tar -czvf "$ARCHIVE_PATH" -T -

# Check if archive was created successfully
if [ $? -eq 0 ]; then
    echo "Archive created successfully at $ARCHIVE_PATH"
    echo "Archive size: $(du -h "$ARCHIVE_PATH" | cut -f1)"
    echo "Files in archive: $(tar -tvf "$ARCHIVE_PATH" | wc -l)"
else
    echo "Error creating archive."
    exit 1
fi
```

To use the script:
```bash
chmod +x search_backup.sh
./search_backup.sh "*.txt" "text_files_backup"
``` 