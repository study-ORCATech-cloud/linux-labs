# Cron and At Scheduling Cheatsheet

## Crontab Commands

| Command | Description | Example |
|---------|-------------|---------|
| `crontab -e` | Edit your crontab file | `crontab -e` |
| `crontab -l` | List your cron jobs | `crontab -l` |
| `crontab -r` | Remove your crontab file | `crontab -r` |
| `crontab -u user -e` | Edit another user's crontab (as root) | `sudo crontab -u john -e` |
| `crontab -u user -l` | List another user's crontab (as root) | `sudo crontab -u john -l` |
| `crontab -u user -r` | Remove another user's crontab (as root) | `sudo crontab -u john -r` |
| `systemctl status cron` | Check if cron service is running | `systemctl status cron` |
| `systemctl restart cron` | Restart the cron service | `sudo systemctl restart cron` |

## Crontab Syntax

```
* * * * * command_to_execute
↑ ↑ ↑ ↑ ↑
│ │ │ │ └─── Day of week (0-6) (Sunday = 0)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

## Crontab Special Characters

| Character | Description | Example |
|-----------|-------------|---------|
| `*` | Any value | `* * * * *` (every minute) |
| `,` | Value list separator | `0,15,30,45 * * * *` (every 15 minutes) |
| `-` | Range of values | `0-5 * * * *` (first 6 minutes of every hour) |
| `/` | Step values | `*/15 * * * *` (every 15 minutes) |

## Crontab Special Strings

| String | Description | Equivalent |
|--------|-------------|------------|
| `@reboot` | Run once at startup | None |
| `@yearly` or `@annually` | Run once a year | `0 0 1 1 *` |
| `@monthly` | Run once a month | `0 0 1 * *` |
| `@weekly` | Run once a week | `0 0 * * 0` |
| `@daily` or `@midnight` | Run once a day | `0 0 * * *` |
| `@hourly` | Run once an hour | `0 * * * *` |

## System Crontab Directories

| Directory | Description | Usage |
|-----------|-------------|-------|
| `/etc/crontab` | System-wide crontab file | Contains system tasks |
| `/etc/cron.d/` | Directory for crontab fragments | Place custom cron job files here |
| `/etc/cron.hourly/` | Run scripts hourly | Place executable scripts here |
| `/etc/cron.daily/` | Run scripts daily | Place executable scripts here |
| `/etc/cron.weekly/` | Run scripts weekly | Place executable scripts here |
| `/etc/cron.monthly/` | Run scripts monthly | Place executable scripts here |

## Common Crontab Examples

| Cron Expression | Description |
|-----------------|-------------|
| `0 * * * *` | Run at the top of every hour |
| `0 0 * * *` | Run at midnight (00:00) daily |
| `0 0 * * 0` | Run at midnight on Sunday |
| `0 0 1 * *` | Run at midnight on the first of every month |
| `0 0 1 1 *` | Run at midnight on January 1 (New Year) |
| `0 8-17 * * 1-5` | Run hourly from 8 AM-5 PM, Monday-Friday |
| `*/10 * * * *` | Run every 10 minutes |
| `0,30 * * * *` | Run at 0 and 30 minutes past every hour |
| `0 12 * * 1-5` | Run at noon on weekdays |

## Output Redirection in Crontab

| Example | Description |
|---------|-------------|
| `* * * * * command > /dev/null 2>&1` | Discard all output (both stdout and stderr) |
| `* * * * * command > /path/to/output.log 2>&1` | Save all output to a log file |
| `* * * * * command >> /path/to/output.log 2>&1` | Append all output to a log file |
| `* * * * * command 2>/path/to/errors.log` | Save only errors to a log file |
| `* * * * * command >/path/to/output.log` | Save only stdout to a log file |

## Environment Variables in Crontab

```
# Set environment variables at the top of your crontab
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=user@example.com
HOME=/home/username

# Jobs will use these environment variables
* * * * * command_to_execute
```

## At Command Syntax

| Command | Description | Example |
|---------|-------------|---------|
| `at TIME` | Schedule a job at a specific time | `at 10:00 PM` |
| `at TIME DATE` | Schedule a job at a specific time on a date | `at 10:00 PM Jul 31 2023` |
| `at now + TIME` | Schedule a job relative to current time | `at now + 1 hour` |
| `atq` | List pending at jobs | `atq` |
| `atrm JOB_NUMBER` | Remove an at job by its number | `atrm 12` |
| `at -c JOB_NUMBER` | View the content of a scheduled job | `at -c 12` |
| `batch` | Run job when system load permits | `batch` |

## At Time Formats

| Format | Description | Example |
|--------|-------------|---------|
| `HH:MM` | 24-hour time format | `14:30` |
| `HH:MM AM/PM` | 12-hour time format | `2:30 PM` |
| `now + N minutes/hours/days/weeks` | Relative time | `now + 30 minutes` |
| `noon` | 12:00 PM | `noon` |
| `midnight` | 12:00 AM | `midnight` |
| `tomorrow` | Tomorrow at current time | `tomorrow` |
| `noon tomorrow` | Tomorrow at noon | `noon tomorrow` |
| `next week` | One week from today | `next week` |
| `next month` | One month from today | `next month` |
| `next year` | One year from today | `next year` |

## At Examples

| Command | Description |
|---------|-------------|
| `at now + 5 minutes` | Schedule job for 5 minutes from now |
| `at 3:00 PM` | Schedule job for 3:00 PM today |
| `at 3:00 PM tomorrow` | Schedule job for 3:00 PM tomorrow |
| `at 3:00 PM next Monday` | Schedule job for 3:00 PM next Monday |
| `at 3:00 PM July 15 2023` | Schedule job for a specific date |
| `at -f scriptfile.sh now + 1 hour` | Run a script file in 1 hour |

## Troubleshooting Tips

1. **Cron isn't running jobs:**
   - Check if cron service is running: `systemctl status cron`
   - Check system logs: `grep CRON /var/log/syslog`
   - Verify file permissions on scripts (should be executable)
   - Ensure scripts have proper shebang line (e.g., `#!/bin/bash`)

2. **Path issues in cron:**
   - Use absolute paths to commands in cron jobs
   - Set PATH variable explicitly in crontab
   - Use absolute paths to any files referenced in scripts

3. **Mail issues:**
   - Check if cron mail is being sent: `ls -la /var/mail/username`
   - Redirect output to a log file for easier debugging
   - Install a mail service if you want mail notifications

4. **Syntax errors:**
   - Validate your crontab syntax: `crontab -e` then save (it will show errors)
   - Check that the job timing fields are correct

5. **Permission issues:**
   - Check if the user has permission to run the command
   - For system-wide cron jobs, specify the user to run as

6. **At command issues:**
   - Ensure atd service is running: `systemctl status atd`
   - Check if user is allowed in `/etc/at.allow` or not in `/etc/at.deny`
   - Check for syntax errors in commands

## Security Considerations

1. **Access restriction:**
   - `/etc/cron.allow`: Only users listed can use cron
   - `/etc/cron.deny`: Users listed cannot use cron
   - `/etc/at.allow`: Only users listed can use at
   - `/etc/at.deny`: Users listed cannot use at

2. **Audit cron usage:**
   - Review all user crontabs: `for user in $(cut -f1 -d: /etc/passwd); do echo $user; sudo crontab -u $user -l 2>/dev/null; done`
   - Check system cron jobs: `ls -la /etc/cron.*/ /etc/cron.d/`

3. **Logging:**
   - Review cron log entries: `grep CRON /var/log/syslog | tail -n 50`
   - Enable detailed logging: Edit `/etc/rsyslog.d/50-default.conf` and uncomment the cron line 