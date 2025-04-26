# LAB11 - Scheduling Tasks with Cron and At Solutions

Below are the solutions to the cron and at scheduling exercises. Remember to try solving them on your own first!

## Exercise 1: Understanding Cron Syntax

### Solution:
1. Learning the format of a crontab entry:
   ```bash
   # The format is: minute hour day-of-month month day-of-week command
   ```

2. Understanding example crontab entries:
   ```bash
   # "15 14 * * *" = 2:15 PM every day
   # "0 0 1 * *" = midnight on the first day of every month
   # "*/15 * * * *" = every 15 minutes
   # "0 9 * * 1" = 9 AM every Monday
   # "0 6 * * 1-5" = 6 AM Monday through Friday
   ```

3. Viewing your current crontab:
   ```bash
   crontab -l
   ```
   If you haven't set up any cron jobs yet, you might see:
   ```
   no crontab for username
   ```

## Exercise 2: Working with User Crontabs

### Solution:
1. Opening your crontab file for editing:
   ```bash
   crontab -e
   ```
   You might be prompted to select an editor if this is your first time. Select your preferred editor (1 for nano is a good choice for beginners).

2. Adding a simple cron job that runs every minute:
   ```bash
   * * * * * echo "Cron test at $(date)" >> ~/cron_minute_test.log
   ```
   Save and exit the editor (in nano: Ctrl+O, Enter, Ctrl+X).

3. Verifying your cron job is scheduled:
   ```bash
   crontab -l
   ```
   Output should show:
   ```
   * * * * * echo "Cron test at $(date)" >> ~/cron_minute_test.log
   ```

4. Checking the log file after a few minutes:
   ```bash
   cat ~/cron_minute_test.log
   ```
   Output example:
   ```
   Cron test at Wed Jan 17 14:32:01 UTC 2024
   Cron test at Wed Jan 17 14:33:01 UTC 2024
   Cron test at Wed Jan 17 14:34:01 UTC 2024
   ```

5. Adding a job that runs every 5 minutes:
   ```bash
   crontab -e
   ```
   Add the line:
   ```
   */5 * * * * echo "5-minute interval test at $(date)" >> ~/cron_5min_test.log
   ```
   Your crontab should now have both entries:
   ```
   * * * * * echo "Cron test at $(date)" >> ~/cron_minute_test.log
   */5 * * * * echo "5-minute interval test at $(date)" >> ~/cron_5min_test.log
   ```

6. Scheduling a cron job to run at a specific time:
   ```bash
   crontab -e
   ```
   Add a line like this (assuming current time is 14:20 and you want it to run at 14:22):
   ```
   22 14 * * * echo "Specific time test at $(date)" >> ~/cron_specific_test.log
   ```
   After a few minutes, check the result:
   ```bash
   cat ~/cron_specific_test.log
   ```
   Output example:
   ```
   Specific time test at Wed Jan 17 14:22:01 UTC 2024
   ```

## Exercise 3: System Crontabs and Special Directories

### Solution:
1. Examining system-wide cron directories:
   ```bash
   ls -la /etc/cron.d/
   ```
   Output example:
   ```
   total 24
   drwxr-xr-x  2 root root 4096 Jan 15 12:34 .
   drwxr-xr-x 90 root root 4096 Jan 17 10:22 ..
   -rw-r--r--  1 root root  102 Feb  2  2023 .placeholder
   -rw-r--r--  1 root root  712 Mar 14  2023 anacron
   -rw-r--r--  1 root root  191 Feb 14  2023 sysstat
   ```

   ```bash
   ls -la /etc/cron.daily/
   ```
   Output example:
   ```
   total 56
   drwxr-xr-x  2 root root 4096 Jan 15 12:34 .
   drwxr-xr-x 90 root root 4096 Jan 17 10:22 ..
   -rw-r--r--  1 root root  102 Feb  2  2023 .placeholder
   -rwxr-xr-x  1 root root  376 Dec  4  2022 apport
   -rwxr-xr-x  1 root root  355 Dec 29  2022 aptitude
   -rwxr-xr-x  1 root root 1478 Feb 27  2023 apt-compat
   ...
   ```

   Similar commands for the other directories:
   ```bash
   ls -la /etc/cron.hourly/
   ls -la /etc/cron.weekly/
   ls -la /etc/cron.monthly/
   ```

2. Looking at the system-wide crontab file:
   ```bash
   sudo cat /etc/crontab
   ```
   Output example:
   ```
   # /etc/crontab: system-wide crontab
   # Unlike any other crontab you don't have to run the `crontab'
   # command to install the new version when you edit this file
   # and files in /etc/cron.d. These files also have username fields,
   # that none of the other crontabs do.

   SHELL=/bin/sh
   PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

   # Example of job definition:
   # .---------------- minute (0 - 59)
   # |  .------------- hour (0 - 23)
   # |  |  .---------- day of month (1 - 31)
   # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
   # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
   # |  |  |  |  |
   # *  *  *  *  * user-name command to be executed
   17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
   25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
   47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
   52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
   ```
   Note the additional "username" field that doesn't exist in user crontabs.

3. Creating a simple script for the hourly cron directory:
   ```bash
   sudo nano /etc/cron.hourly/example_script
   ```
   Adding the content:
   ```bash
   #!/bin/bash
   echo "Hourly cron executed at $(date)" >> /tmp/system_cron_test.log
   ```
   Making it executable:
   ```bash
   sudo chmod +x /etc/cron.hourly/example_script
   ```
   You can verify it was created and made executable:
   ```bash
   ls -la /etc/cron.hourly/example_script
   ```
   Output example:
   ```
   -rwxr-xr-x 1 root root 76 Jan 17 15:05 /etc/cron.hourly/example_script
   ```
   After an hour, check the log:
   ```bash
   cat /tmp/system_cron_test.log
   ```

## Exercise 4: Using Special Cron Strings

### Solution:
1. Editing your crontab:
   ```bash
   crontab -e
   ```

2. Adding cron entries using special time strings:
   ```
   @reboot echo "System rebooted at $(date)" >> ~/cron_reboot.log
   @daily echo "Daily job at $(date)" >> ~/cron_daily.log
   @weekly echo "Weekly job at $(date)" >> ~/cron_weekly.log
   ```
   
   Save and exit the editor. You can verify these were added:
   ```bash
   crontab -l
   ```
   
   The reboot entry will run after you restart your system. The daily and weekly entries will run at the appropriate times.

3. Other special strings:
   These special strings make crontab entries more readable:
   - `@yearly` or `@annually`: Runs once a year at midnight on January 1st
   - `@monthly`: Runs once a month at midnight on the first day
   - `@hourly`: Runs once an hour at the beginning of the hour

## Exercise 5: Setting Up At Jobs for One-time Tasks

### Solution:
1. Scheduling a job to run 2 minutes from now:
   ```bash
   at now + 2 minutes
   ```
   At the prompt, type:
   ```
   echo "At job executed at $(date)" >> ~/at_test.log
   ```
   Press CTRL+D to save the job.
   
   You'll see something like:
   ```
   warning: commands will be executed using /bin/sh
   job 1 at Wed Jan 17 15:10:00 2024
   ```

2. Listing pending at jobs:
   ```bash
   atq
   ```
   Output example:
   ```
   1	Wed Jan 17 15:10:00 2024 a username
   ```

3. Examining the content of an at job:
   ```bash
   at -c 1
   ```
   Output example (truncated):
   ```
   #!/bin/sh
   # atrun uid=1000 gid=1000
   # mail username 0
   umask 22
   ... [environment variables] ...
   cd /home/username || {
           echo 'Execution directory inaccessible' >&2
           exit 1
   }
   ${SHELL:-/bin/sh} << 'marcinDELIMITER37ac0518'
   echo "At job executed at $(date)" >> ~/at_test.log
   marcinDELIMITER37ac0518
   ```

4. Scheduling a job for a specific time today:
   ```bash
   at 16:30
   ```
   At the prompt, type:
   ```
   echo "Scheduled for specific time: $(date)" >> ~/at_time_test.log
   ```
   Press CTRL+D to save the job.

5. Scheduling a job for tomorrow:
   ```bash
   at 10:00 tomorrow
   ```
   At the prompt, type:
   ```
   echo "Tomorrow job executed at $(date)" >> ~/at_tomorrow_test.log
   ```
   Press CTRL+D to save the job.

6. Scheduling a job for a specific date and time:
   ```bash
   at 2:00 PM July 15 2024
   ```
   At the prompt, type:
   ```
   echo "Specific date job executed at $(date)" >> ~/at_date_test.log
   ```
   Press CTRL+D to save the job.

7. Removing a scheduled at job:
   ```bash
   atq
   ```
   Find the job number you want to remove, then:
   ```bash
   atrm JOB_NUMBER
   ```
   For example:
   ```bash
   atrm 3
   ```
   Verify it was removed:
   ```bash
   atq
   ```

## Exercise 6: Redirecting Output and Handling Errors

### Solution:
1. Editing your crontab:
   ```bash
   crontab -e
   ```

2. Adding a job with proper output redirection:
   ```
   */10 * * * * /path/to/script.sh > /tmp/output.log 2>&1
   ```
   This redirects both standard output (stdout) and standard error (stderr) to the log file.

3. Creating a script that might generate errors:
   ```bash
   nano ~/test_script.sh
   ```
   Adding content:
   ```bash
   #!/bin/bash
   echo "Starting script"
   ls /path/does/not/exist
   echo "Script completed"
   ```
   Making it executable:
   ```bash
   chmod +x ~/test_script.sh
   ```

4. Testing the script:
   ```bash
   ~/test_script.sh
   ```
   Output example:
   ```
   Starting script
   ls: cannot access '/path/does/not/exist': No such file or directory
   Script completed
   ```

5. Scheduling with different output handling:
   ```bash
   crontab -e
   ```
   Add these lines:
   ```
   # Discard all output
   */15 * * * * ~/test_script.sh > /dev/null 2>&1
   
   # Save all output, appending to log
   */16 * * * * ~/test_script.sh >> ~/script_output.log 2>&1
   
   # Save errors only
   */17 * * * * ~/test_script.sh 1>/dev/null 2>>~/script_errors.log
   ```
   
   After some time, check the logs:
   ```bash
   cat ~/script_output.log
   cat ~/script_errors.log
   ```
   
   You should see the complete output in script_output.log:
   ```
   Starting script
   ls: cannot access '/path/does/not/exist': No such file or directory
   Script completed
   ```
   
   And only the error message in script_errors.log:
   ```
   ls: cannot access '/path/does/not/exist': No such file or directory
   ```

## Exercise 7: Environment Variables and Path Issues

### Solution:
1. Creating a script that uses commands:
   ```bash
   nano ~/path_test.sh
   ```
   Adding content:
   ```bash
   #!/bin/bash
   echo "PATH is: $PATH"
   which ls
   date
   ```
   Making it executable:
   ```bash
   chmod +x ~/path_test.sh
   ```

2. Testing the script:
   ```bash
   ~/path_test.sh
   ```
   Output example:
   ```
   PATH is: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   /usr/bin/ls
   Wed Jan 17 15:25:10 UTC 2024
   ```

3. Scheduling with PATH specified:
   ```bash
   crontab -e
   ```
   Add the lines:
   ```
   PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
   */5 * * * * ~/path_test.sh >> ~/path_test.log 2>&1
   ```
   
   After 5 minutes, check the log:
   ```bash
   cat ~/path_test.log
   ```
   
   Output example:
   ```
   PATH is: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
   /usr/bin/ls
   Wed Jan 17 15:30:01 UTC 2024
   ```

4. Testing environment variables:
   ```bash
   crontab -e
   ```
   Add these lines:
   ```
   # Print environment variables
   */10 * * * * env > ~/cron_env.log
   
   # Use environment variables
   HOME=/tmp
   */10 * * * * echo "HOME is $HOME" >> ~/cron_home_test.log
   ```
   
   After 10 minutes, check the logs:
   ```bash
   cat ~/cron_env.log
   cat ~/cron_home_test.log
   ```
   
   In cron_home_test.log, you should see:
   ```
   HOME is /tmp
   ```
   
   This shows that you can set environment variables in the crontab that will be used by your jobs.

## Exercise 8: Restricting Cron Access

### Solution:
1. Examining cron allow/deny files:
   ```bash
   sudo ls -la /etc/cron.allow /etc/cron.deny 2>/dev/null
   ```
   
   If these files don't exist, you might see:
   ```
   ls: cannot access '/etc/cron.allow': No such file or directory
   ls: cannot access '/etc/cron.deny': No such file or directory
   ```
   
   To create them:
   ```bash
   sudo touch /etc/cron.allow
   sudo echo "username" | sudo tee -a /etc/cron.allow
   ```
   
   This would create an allow file with your username, restricting cron to only you.

2. Understanding access control:
   - If `/etc/cron.allow` exists, only users listed in it can use cron
   - If `/etc/cron.allow` doesn't exist but `/etc/cron.deny` exists, all users except those in cron.deny can use cron
   - If neither file exists, the behavior depends on system configuration (often only root can use cron or all users can)

## Bonus Challenge Solution:

Here's a script that creates a backup with all the specified requirements:

```bash
#!/bin/bash

# Backup script with retention policy

# Set variables
BACKUP_DIR="/home/username/backups"        # Where to store backups
SOURCE_DIR="/home/username/important_data" # Directory to backup
LOG_FILE="/home/username/backup.log"       # Log file
MAX_BACKUPS=7                             # Number of backups to keep

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create timestamp for filename
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Log start of backup
echo "Backup started at $(date)" >> "$LOG_FILE"

# Create the backup
if tar -czf "$BACKUP_FILE" "$SOURCE_DIR"; then
    echo "Backup successful: $BACKUP_FILE" >> "$LOG_FILE"
    
    # Count existing backups
    BACKUP_COUNT=$(ls -1 "$BACKUP_DIR"/backup_*.tar.gz 2>/dev/null | wc -l)
    
    # If we have more than MAX_BACKUPS, delete the oldest ones
    if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
        # Calculate how many to delete
        DELETE_COUNT=$((BACKUP_COUNT - MAX_BACKUPS))
        
        # Get the oldest backups and delete them
        OLDEST_BACKUPS=$(ls -1t "$BACKUP_DIR"/backup_*.tar.gz | tail -n "$DELETE_COUNT")
        
        echo "Removing $DELETE_COUNT old backup(s)" >> "$LOG_FILE"
        
        for OLD_BACKUP in $OLDEST_BACKUPS; do
            rm "$OLD_BACKUP"
            echo "Deleted old backup: $OLD_BACKUP" >> "$LOG_FILE"
        done
    fi
else
    echo "Backup failed!" >> "$LOG_FILE"
fi

echo "Backup process completed at $(date)" >> "$LOG_FILE"
echo "----------------------------------------" >> "$LOG_FILE"
```

Save this script as `~/backup_script.sh`, then make it executable:

```bash
chmod +x ~/backup_script.sh
```

Test it manually:

```bash
./backup_script.sh
```

Then schedule it to run at 3 AM daily using crontab:

```bash
crontab -e
```

Add this line:

```
0 3 * * * /home/username/backup_script.sh
```

The script will:
1. Create a dated backup of your specified directory
2. Log the process to a log file
3. Check how many backups exist
4. If there are more than 7, delete the oldest ones
5. Run automatically at 3 AM daily

## Cleanup

To clean up after completing these exercises:

1. Remove all cron jobs:
   ```bash
   crontab -r
   ```

2. Remove test scripts and log files:
   ```bash
   rm ~/test_script.sh ~/path_test.sh ~/backup_script.sh 2>/dev/null
   rm ~/cron_*.log ~/at_*.log ~/script_*.log ~/path_test.log ~/backup.log 2>/dev/null
   ```

3. Remove the system cron example (if you created it):
   ```bash
   sudo rm /etc/cron.hourly/example_script
   sudo rm /tmp/system_cron_test.log 2>/dev/null
   ```

4. Check for and remove any remaining at jobs:
   ```bash
   for job in $(atq | cut -f1); do atrm "$job"; done
   ``` 