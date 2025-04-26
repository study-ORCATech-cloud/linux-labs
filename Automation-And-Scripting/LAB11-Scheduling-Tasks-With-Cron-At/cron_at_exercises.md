# LAB11 - Scheduling Tasks with Cron and At Exercises

These exercises will help you practice scheduling tasks in Linux using the `cron` and `at` schedulers. Complete each task to build essential automation skills.

## Exercise 1: Understanding Cron Syntax

### TODO:
1. Learn the format of a crontab entry by examining the structure:
   ```
   # ┌───────────── minute (0 - 59)
   # │ ┌───────────── hour (0 - 23)
   # │ │ ┌───────────── day of the month (1 - 31)
   # │ │ │ ┌───────────── month (1 - 12)
   # │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
   # │ │ │ │ │
   # * * * * * command to execute
   ```

2. Examine these example crontab entries and explain what each one does:
   ```
   15 14 * * * /path/to/command
   0 0 1 * * /path/to/command
   */15 * * * * /path/to/command
   0 9 * * 1 /path/to/command
   0 6 * * 1-5 /path/to/command
   ```

3. View your current user's crontab:
   ```
   crontab -l
   ```

## Exercise 2: Working with User Crontabs

### TODO:
1. Open your crontab file for editing.

2. Add a simple cron job that runs every minute and logs the date to a file.

3. Verify your new cron job is scheduled.

4. Wait 2-3 minutes, then check the log file to confirm it's working.

5. Modify your crontab to add a job that runs every 5 minutes.

6. Schedule a cron job to run at a specific time (for example, 2 minutes from now).

## Exercise 3: System Crontabs and Special Directories

### TODO:
1. Examine system-wide cron directories:
   ```
   /etc/cron.d/
   /etc/cron.daily/
   /etc/cron.hourly/
   /etc/cron.monthly/
   /etc/cron.weekly/
   ```

2. Look at the system-wide crontab file and note how it differs from user crontabs.

3. Create a simple script for the hourly cron directory that logs the execution time to a file.

## Exercise 4: Using Special Cron Strings

### TODO:
1. Edit your crontab again.

2. Add cron entries using the following special time strings:
   - `@reboot`
   - `@daily`
   - `@weekly`

3. Research other special strings like `@yearly`, `@annually`, `@monthly`, and `@hourly`.

## Exercise 5: Setting Up At Jobs for One-time Tasks

### TODO:
1. Schedule a job to run 2 minutes from now using the `at` command.

2. List your pending at jobs.

3. Examine the content of an at job.

4. Schedule a job for a specific time today.

5. Schedule a job for tomorrow.

6. Schedule a job for a specific date and time.

7. Remove a scheduled at job.

## Exercise 6: Redirecting Output and Handling Errors

### TODO:
1. Edit your crontab.

2. Add a job that redirects both standard output and standard error to a log file.

3. Create a script that might generate errors.

4. Schedule this script using cron with different output handling methods:
   - Discard all output
   - Save all output to a log file
   - Save only error output to a log file

## Exercise 7: Environment Variables and Path Issues

### TODO:
1. Create a simple script that prints environment variables and uses common commands.

2. Schedule it with cron, specifying the PATH environment variable.

3. Test how environment variables behave in cron jobs by creating jobs that:
   - Print all environment variables
   - Use a custom environment variable

## Exercise 8: Restricting Cron Access

### TODO:
1. Examine cron allow/deny files on your system.

2. Research how these files control access to cron functionality.

## Bonus Challenge:
Create a backup script that:
1. Archives a specific directory
2. Adds a date/timestamp to the archive name
3. Schedules to run daily at 3 AM
4. Keeps only the 7 most recent backups, deleting older ones
5. Logs success or failure to a separate log file 