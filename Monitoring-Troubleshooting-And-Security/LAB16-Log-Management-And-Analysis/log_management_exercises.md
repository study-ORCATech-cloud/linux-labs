# LAB16 - Log Management and Analysis Exercises

These exercises will help you develop skills in analyzing, monitoring, and managing system logs in Linux. Complete each task to strengthen your log management abilities.

## Exercise 1: Exploring Log Files

### TODO:
1. Identify and list at least 5 important log files in the `/var/log/` directory.

2. Examine the content of the system log file (syslog or messages depending on your distribution).

3. Locate the authentication log file and view its contents.

4. Find and examine the kernel log messages.

5. Identify where Apache or Nginx web server logs are stored (if installed).

## Exercise 2: Basic Log Analysis

### TODO:
1. Find all error messages in the system log from today.

2. Extract all login failure messages from the authentication log.

3. Identify all kernel-related messages containing the word "error" or "fail".

4. Count how many SSH login attempts were made in the last 24 hours.

5. Create a file containing all messages related to USB device connections from the system log.

## Exercise 3: Using Log Analysis Tools

### TODO:
1. Use `journalctl` to view the logs managed by systemd.

2. Filter journalctl output to show only error messages.

3. View logs for a specific time range (e.g., between 2 PM and 4 PM today).

4. Export systemd journal entries from the last hour to a file.

5. Use `journalctl` to follow live log entries (similar to `tail -f`).

## Exercise 4: Log Rotation

### TODO:
1. Examine the configuration of the `logrotate` utility.

2. Identify which logs are configured to be rotated and their rotation schedule.

3. Create a custom logrotate configuration for a log file of your choice.

4. Manually trigger a log rotation for testing.

5. Verify that the log rotation worked correctly.

## Exercise 5: Creating Logging Scripts

### TODO:
1. Write a script that generates log entries with timestamps for system events.

2. Create a script that checks disk space and logs warnings when space is below 20%.

3. Develop a script that monitors failed SSH login attempts and logs them to a custom log file.

4. Write a script that archives old log files into compressed files.

5. Create a simple log rotation script without using logrotate.

## Exercise 6: Centralized Logging

### TODO:
1. Configure rsyslog to send log messages to a central log server (or local file simulating a remote server).

2. Configure a specific application to log to a custom facility.

3. Set up log filtering to process only important messages.

4. Test the centralized logging setup.

5. Modify rsyslog configuration to format log messages in a specific way.

## Exercise 7: Log Monitoring and Alerting

### TODO:
1. Write a script that monitors logs for specific error patterns.

2. Configure the script to send an email alert when critical errors are detected.

3. Set up the script to run periodically using cron.

4. Create a summary report of errors and warnings found in logs.

5. Implement a simple log dashboard script that shows the most recent critical errors.

## Bonus Challenge: 
Develop a comprehensive log analysis system that:
- Collects logs from multiple sources
- Parses and normalizes log formats
- Identifies patterns and potential security issues
- Generates daily reports with statistics
- Alerts on suspicious activity
- Maintains an archive of historical logs

This challenge will test your ability to create a complete log management solution integrating multiple concepts from this lab.

## Cleanup:
1. Remove any custom log files created during the exercises.
2. Restore any modified system configuration files to their original state.
3. Remove any temporary files or scripts created for the exercises. 