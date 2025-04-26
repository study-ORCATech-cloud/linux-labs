# LAB05 - Basic Shell Commands Solutions

Below are the solutions to the basic shell commands exercises. Remember to try solving them on your own first!

## Exercise 1: Creating Sample Data Files

### Solution:
1. Create the directory:
   ```bash
   mkdir ~/shell_lab
   ```

2. Create the users.txt file:
   ```bash
   cat > ~/shell_lab/users.txt << EOF
   user1:student:1001:Active
   user2:admin:1002:Active
   user3:developer:1003:Inactive
   user4:student:1004:Active
   user5:admin:1005:Inactive
   user6:developer:1006:Active
   EOF
   ```

3. Create the numbers.txt file:
   ```bash
   cat > ~/shell_lab/numbers.txt << EOF
   10
   5
   42
   17
   5
   10
   8
   42
   1
   EOF
   ```

4. Create the log.txt file:
   ```bash
   cat > ~/shell_lab/log.txt << EOF
   2023-10-01 08:15:01 INFO Starting application
   2023-10-01 08:15:03 DEBUG Loading configuration
   2023-10-01 08:15:05 WARNING Config file missing default section
   2023-10-01 08:15:10 ERROR Failed to connect to database
   2023-10-01 08:15:15 ERROR Connection timed out
   2023-10-01 08:16:01 INFO Retrying connection
   2023-10-01 08:16:10 INFO Connected successfully
   2023-10-01 08:16:30 DEBUG User authentication started
   2023-10-01 08:16:35 INFO User logged in
   EOF
   ```

## Exercise 2: Basic File Viewing Commands

### Solution:
1. Display entire file content:
   ```bash
   cat ~/shell_lab/users.txt
   ```

2. Display first 3 lines:
   ```bash
   head -n 3 ~/shell_lab/log.txt
   ```

3. Display last 4 lines:
   ```bash
   tail -n 4 ~/shell_lab/log.txt
   ```

4. Display lines 3-5 using head and tail:
   ```bash
   head -n 5 ~/shell_lab/log.txt | tail -n 3
   ```

5. Count lines, words, and characters:
   ```bash
   wc ~/shell_lab/*.txt
   ```

## Exercise 3: Text Processing with cut, sort, and uniq

### Solution:
1. Extract usernames:
   ```bash
   cut -d: -f1 ~/shell_lab/users.txt
   ```

2. Extract roles:
   ```bash
   cut -d: -f2 ~/shell_lab/users.txt
   ```

3. Extract and sort roles:
   ```bash
   cut -d: -f2 ~/shell_lab/users.txt | sort
   ```

4. Extract, sort, and unique roles:
   ```bash
   cut -d: -f2 ~/shell_lab/users.txt | sort | uniq
   ```

5. Sort numbers numerically:
   ```bash
   sort -n ~/shell_lab/numbers.txt
   ```

6. Find duplicate numbers:
   ```bash
   sort ~/shell_lab/numbers.txt | uniq -d
   ```

7. Count occurrences of each number:
   ```bash
   sort ~/shell_lab/numbers.txt | uniq -c
   ```

## Exercise 4: Working with Log Files

### Solution:
1. Find ERROR messages:
   ```bash
   grep "ERROR" ~/shell_lab/log.txt
   ```

2. Find INFO or DEBUG messages:
   ```bash
   grep "INFO\|DEBUG" ~/shell_lab/log.txt
   # Alternative:
   grep -E "INFO|DEBUG" ~/shell_lab/log.txt
   ```

3. Extract timestamps and message levels:
   ```bash
   cut -d' ' -f1,2,3 ~/shell_lab/log.txt
   ```

4. Count ERROR messages:
   ```bash
   grep "ERROR" ~/shell_lab/log.txt | wc -l
   ```

5. Create errors.txt:
   ```bash
   grep "ERROR" ~/shell_lab/log.txt > ~/shell_lab/errors.txt
   ```

## Exercise 5: Data Analysis with Shell Commands

### Solution:
1. Count users by role:
   ```bash
   cut -d: -f2 ~/shell_lab/users.txt | sort | uniq -c > ~/shell_lab/roles_count.txt
   ```

2. List active users sorted by username:
   ```bash
   grep "Active" ~/shell_lab/users.txt | sort > ~/shell_lab/active_users.txt
   ```

3. Find highest number:
   ```bash
   sort -n ~/shell_lab/numbers.txt | tail -n 1
   ```

4. Calculate sum of numbers:
   ```bash
   # Using awk
   awk '{sum += $1} END {print sum}' ~/shell_lab/numbers.txt
   
   # Using paste and bc
   paste -sd+ ~/shell_lab/numbers.txt | bc
   ```

5. Find average:
   ```bash
   # Using awk
   awk '{sum += $1; count++} END {print sum/count}' ~/shell_lab/numbers.txt
   
   # Using multiple commands
   sum=$(paste -sd+ ~/shell_lab/numbers.txt | bc)
   count=$(wc -l < ~/shell_lab/numbers.txt)
   echo "scale=2; $sum / $count" | bc
   ```

## Exercise 6: Redirection and Command Chaining

### Solution:
1. Create system_info.txt:
   ```bash
   # Create the file with date
   date > ~/shell_lab/system_info.txt
   
   # Append username
   whoami >> ~/shell_lab/system_info.txt
   
   # Append current directory
   pwd >> ~/shell_lab/system_info.txt
   
   # Append disk space
   df -h >> ~/shell_lab/system_info.txt
   
   # Append memory usage
   free -h >> ~/shell_lab/system_info.txt
   ```

2. Append kernel info:
   ```bash
   uname -a >> ~/shell_lab/system_info.txt
   ```

3. Create reports directory:
   ```bash
   mkdir -p ~/shell_lab/reports
   ```

4. Copy files with ERROR content:
   ```bash
   grep -l "ERROR" ~/shell_lab/*.txt | xargs -I{} cp {} ~/shell_lab/reports/
   ```

5. Create sorted unique numbers file:
   ```bash
   sort -n ~/shell_lab/numbers.txt | uniq > ~/shell_lab/reports/sorted_unique_numbers.txt
   ```

## Exercise 7: Cleanup

### Solution:
1. Create compressed archive:
   ```bash
   tar -czvf ~/shell_lab_backup.tar.gz ~/shell_lab
   ```

2. Create backup directory and move archive:
   ```bash
   mkdir -p ~/backups
   mv ~/shell_lab_backup.tar.gz ~/backups/
   ```

3. Create cleanup script:
   ```bash
   cat > ~/shell_lab/cleanup.sh << 'EOF'
   #!/bin/bash
   
   # Script to remove all .txt files from the shell_lab directory
   
   # Check if we're in the right directory
   if [[ $(basename $(pwd)) != "shell_lab" ]]; then
       echo "Please run this script from the shell_lab directory."
       exit 1
   fi
   
   # List the files that would be removed
   echo "The following .txt files will be removed:"
   ls -la *.txt
   
   # Ask for confirmation
   read -p "Are you sure you want to delete these files? (y/n): " confirm
   
   # Check the response
   if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
       echo "Removing files..."
       rm *.txt
       echo "Files removed successfully."
   else
       echo "Operation cancelled. No files were removed."
   fi
   EOF
   ```

4. Make the script executable:
   ```bash
   chmod +x ~/shell_lab/cleanup.sh
   ```

## Bonus Challenge Solution:

```bash
#!/bin/bash

# Log analyzer script

# Check if argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

LOG_FILE="$1"

# Check if file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: File '$LOG_FILE' not found."
    exit 1
fi

# Create a temp directory for our analysis
TEMP_DIR=$(mktemp -d)

# Function to cleanup temp files
cleanup() {
    rm -rf "$TEMP_DIR"
}

# Register cleanup function to run on exit
trap cleanup EXIT

# Get the total number of log entries
TOTAL_ENTRIES=$(wc -l < "$LOG_FILE")

# Extract message levels and count
echo "Analyzing log levels..."
grep -o 'INFO\|DEBUG\|ERROR\|WARNING' "$LOG_FILE" | sort | uniq -c > "$TEMP_DIR/level_counts.txt"

# Extract ERROR messages
grep "ERROR" "$LOG_FILE" > "$TEMP_DIR/errors.txt"

# Get time range
FIRST_TIMESTAMP=$(head -n 1 "$LOG_FILE" | cut -d' ' -f1,2)
LAST_TIMESTAMP=$(tail -n 1 "$LOG_FILE" | cut -d' ' -f1,2)

# Create the report
cat << EOF > "log_analysis_report.txt"
=== Log Analysis Report ===
Log file: $LOG_FILE
Generated: $(date)

Total log entries: $TOTAL_ENTRIES

Message Level Counts:
$(cat "$TEMP_DIR/level_counts.txt")

ERROR Messages:
$(cat "$TEMP_DIR/errors.txt")

Time Period Covered:
From: $FIRST_TIMESTAMP
To:   $LAST_TIMESTAMP
EOF

echo "Analysis complete. Report saved to 'log_analysis_report.txt'"
```

To use the script:
```bash
chmod +x log_analyzer.sh
./log_analyzer.sh ~/shell_lab/log.txt
``` 