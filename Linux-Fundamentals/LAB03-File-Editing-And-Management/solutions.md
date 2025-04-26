# LAB03 - File Editing and Management Solutions

Below are the solutions to the file editing and management exercises. Remember to try solving them on your own first!

## Exercise 1: Creating and Viewing Files

### Solution:
1. Create a new directory:
   ```bash
   mkdir ~/file_lab
   ```

2. Create an empty file with touch:
   ```bash
   cd ~/file_lab
   touch sample.txt
   ```

3. Create a file with a text editor:
   ```bash
   # Using nano
   nano notes.txt
   
   # OR using vim
   vim notes.txt
   ```

4. Add the text to notes.txt:
   - For nano: Type the content, then save with Ctrl+O, hit Enter, and exit with Ctrl+X
   - For vim: Press i to enter insert mode, type the content, press Esc to exit insert mode, then type :wq and hit Enter to save and quit

5. View file contents:
   ```bash
   cat notes.txt
   less notes.txt  # Press q to exit less
   ```

## Exercise 2: Working with Nano Text Editor

### Solution:
1. Open file with nano:
   ```bash
   nano sample.txt
   ```

2. Add the content by typing it in.

3. Save using Ctrl+O, then Enter.

4. To navigate to line 3:
   - Press Ctrl+_ (underscore)
   - Type 3 and press Enter

5. Delete line 3:
   - With cursor at the beginning of line 3, press Ctrl+K

6. Add the new line:
   - Type "This is the NEW line 3"

7. Save and exit:
   - Press Ctrl+O, then Enter to save
   - Press Ctrl+X to exit

8. Verify content:
   ```bash
   cat sample.txt
   ```

## Exercise 3: Introduction to Vim

### Solution:
1. Open sample.txt with vim:
   ```bash
   vim sample.txt
   ```

2. Enter insert mode:
   - Press i

3. Add a new line at the end:
   - Move to the end of the file using the arrow keys
   - Press Enter to create a new line
   - Type "This line was added with vim"

4. Exit insert mode:
   - Press Esc

5. Save and quit:
   - Type :wq
   - Press Enter

6. Create new file with vim:
   ```bash
   vim vim_practice.txt
   ```

7. Add five lines of text:
   - Press i to enter insert mode
   - Type your five lines
   - Press Esc to exit insert mode

8. Save and exit:
   - Type :wq
   - Press Enter

9. View contents:
   ```bash
   cat vim_practice.txt
   ```

## Exercise 4: Copying and Moving Files

### Solution:
1. Create backup directory:
   ```bash
   mkdir ~/file_lab/backup
   ```

2. Copy sample.txt:
   ```bash
   cp ~/file_lab/sample.txt ~/file_lab/backup/
   ```

3. Create documents directory:
   ```bash
   mkdir ~/file_lab/documents
   ```

4. Move notes.txt:
   ```bash
   mv ~/file_lab/notes.txt ~/file_lab/documents/
   ```

5. Create duplicate file:
   ```bash
   cp ~/file_lab/vim_practice.txt ~/file_lab/vim_practice_copy.txt
   ```

6. Verify file locations:
   ```bash
   ls -la ~/file_lab
   ls -la ~/file_lab/backup
   ls -la ~/file_lab/documents
   ```

## Exercise 5: Working with File Content

### Solution:
1. Create combined.txt:
   ```bash
   touch ~/file_lab/combined.txt
   ```

2. Concatenate files:
   ```bash
   cat ~/file_lab/sample.txt ~/file_lab/vim_practice.txt > ~/file_lab/combined.txt
   ```

3. Create file with first 3 lines:
   ```bash
   head -n 3 ~/file_lab/combined.txt > ~/file_lab/first_three.txt
   ```

4. Create file with last 3 lines:
   ```bash
   tail -n 3 ~/file_lab/combined.txt > ~/file_lab/last_three.txt
   ```

5. Count lines, words, and characters:
   ```bash
   wc ~/file_lab/combined.txt
   ```

## Exercise 6: Finding and Comparing Files

### Solution:
1. Edit the backup copy:
   ```bash
   nano ~/file_lab/backup/sample.txt
   # Make some changes to the content
   ```

2. Compare the files:
   ```bash
   diff ~/file_lab/sample.txt ~/file_lab/backup/sample.txt
   ```

3. Find all .txt files:
   ```bash
   find ~/file_lab -name "*.txt"
   ```

4. Find files containing "line":
   ```bash
   grep -r "line" ~/file_lab
   ```

## Exercise 7: Cleanup

### Solution:
1. Create archive directory:
   ```bash
   mkdir ~/archive
   ```

2. Move the file_lab directory:
   ```bash
   mv ~/file_lab ~/archive/
   ```

3. Navigate to home directory:
   ```bash
   cd ~
   ```

4. Delete the archive directory:
   ```bash
   rm -rf ~/archive
   ```

## Bonus Challenge Solution:

Create a file_report.sh script:

```bash
#!/bin/bash

# Check if directory is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Check if the provided path is a directory
if [ ! -d "$1" ]; then
    echo "Error: $1 is not a directory"
    exit 1
fi

# Navigate to the directory
cd "$1"

# Get directory name
DIR_NAME=$(basename "$1")

# Create report header
echo "===== File Report for $DIR_NAME ====="
echo "Generated on: $(date)"
echo

# Count total files
total_files=$(find . -type f | wc -l)
echo "Total files: $total_files"

# Count by file extension
echo
echo "Files by type:"
find . -type f | grep -o '\.[^./]*$' | sort | uniq -c | sort -nr

# Calculate total size
echo
total_size=$(du -sh . | cut -f1)
echo "Total size: $total_size"

# List largest files
echo
echo "Top 5 largest files:"
find . -type f -exec du -h {} \; | sort -hr | head -n 5

echo
echo "===== End of Report ====="
```

To use the script:
```bash
chmod +x file_report.sh
./file_report.sh ~/file_lab
``` 