# LAB16 - Log Management and Analysis Cheatsheet

This cheatsheet provides a quick reference for managing and analyzing logs in Linux systems.

## Important Log Files and Directories

| Log File/Directory | Description | Common Location |
|-------------------|-------------|----------------|
| `/var/log/syslog` or `/var/log/messages` | General system logs | Ubuntu: `/var/log/syslog`<br>CentOS/RHEL: `/var/log/messages` |
| `/var/log/auth.log` or `/var/log/secure` | Authentication logs | Ubuntu: `/var/log/auth.log`<br>CentOS/RHEL: `/var/log/secure` |
| `/var/log/kern.log` | Kernel logs | Most distributions |
| `/var/log/dmesg` | Boot-time hardware detection logs | Most distributions |
| `/var/log/apache2/` or `/var/log/httpd/` | Web server logs | Ubuntu: `/var/log/apache2/`<br>CentOS/RHEL: `/var/log/httpd/` |
| `/var/log/nginx/` | Nginx web server logs | Most distributions |
| `/var/log/mysql/` or `/var/log/mariadb/` | Database logs | Depends on distribution and DB |
| `/var/log/apt/` or `/var/log/yum.log` | Package management logs | Depends on distribution |
| `/var/log/cron` | Cron job logs | Most distributions |
| `/var/log/boot.log` | System boot logs | Most distributions |

## Basic Log Commands

| Command | Description | Example |
|---------|-------------|---------|
| `cat` | Display entire log file | `cat /var/log/syslog` |
| `less` | View logs with pagination | `less /var/log/syslog` |
| `tail` | View the end of a log file | `tail -n 50 /var/log/syslog` |
| `tail -f` | Follow log in real-time | `tail -f /var/log/syslog` |
| `head` | View the beginning of a log file | `head -n 20 /var/log/auth.log` |
| `grep` | Search for patterns in logs | `grep "error" /var/log/syslog` |
| `zcat` | View compressed logs | `zcat /var/log/syslog.1.gz` |
| `zgrep` | Search compressed logs | `zgrep "error" /var/log/syslog.1.gz` |

## Log Filtering with grep

| Command | Description | Example |
|---------|-------------|---------|
| `grep -i` | Case-insensitive search | `grep -i "error" /var/log/syslog` |
| `grep -v` | Invert match (exclude) | `grep -v "DEBUG" /var/log/syslog` |
| `grep -r` | Recursive search | `grep -r "error" /var/log/` |
| `grep -A n` | Show n lines after match | `grep -A 3 "error" /var/log/syslog` |
| `grep -B n` | Show n lines before match | `grep -B 2 "error" /var/log/syslog` |
| `grep -C n` | Show n lines around match | `grep -C 3 "error" /var/log/syslog` |
| `grep -E` | Use extended regex | `grep -E "error|warning" /var/log/syslog` |
| `egrep` | Shorthand for grep -E | `egrep "error|warning" /var/log/syslog` |

## Time-Based Log Analysis

| Command | Description | Example |
|---------|-------------|---------|
| `grep "May 20"` | Filter by date | `grep "May 20" /var/log/syslog` |
| `grep "2023-05-20"` | Filter by ISO date | `grep "2023-05-20" /var/log/syslog` |
| `grep "$(date '+%b %e')"` | Today's logs | `grep "$(date '+%b %e')" /var/log/syslog` |
| `grep -A 1000 "10:00:00" \| grep -B 1000 "11:00:00"` | Time range | Logs between 10 AM and 11 AM |

## Journalctl Commands (Systemd-based Systems)

| Command | Description | Example |
|---------|-------------|---------|
| `journalctl` | View all logs | `journalctl` |
| `journalctl -f` | Follow logs in real-time | `journalctl -f` |
| `journalctl -u` | Logs for a specific unit | `journalctl -u ssh.service` |
| `journalctl -p` | Filter by priority | `journalctl -p err` |
| `journalctl --since` | Logs since time | `journalctl --since "2023-05-20 10:00:00"` |
| `journalctl --until` | Logs until time | `journalctl --until "2023-05-20 11:00:00"` |
| `journalctl --since today` | Today's logs | `journalctl --since today` |
| `journalctl -b` | Logs from current boot | `journalctl -b` |
| `journalctl -b -1` | Logs from previous boot | `journalctl -b -1` |
| `journalctl -o` | Change output format | `journalctl -o json-pretty` |
| `journalctl --disk-usage` | Check journal size | `journalctl --disk-usage` |
| `journalctl --vacuum-size` | Limit journal size | `journalctl --vacuum-size=1G` |
| `journalctl --vacuum-time` | Remove old journals | `journalctl --vacuum-time=1month` |

## Priority Levels for Journalctl

| Level | Description | Keyword | Number |
|-------|-------------|---------|--------|
| Emergency | System is unusable | `emerg` | 0 |
| Alert | Action must be taken immediately | `alert` | 1 |
| Critical | Critical conditions | `crit` | 2 |
| Error | Error conditions | `err` | 3 |
| Warning | Warning conditions | `warning` | 4 |
| Notice | Normal but significant conditions | `notice` | 5 |
| Informational | Informational messages | `info` | 6 |
| Debug | Debug-level messages | `debug` | 7 |

## Rsyslog Configuration

| Item | Description | Example |
|------|-------------|---------|
| Configuration file | Main config file | `/etc/rsyslog.conf` |
| Configuration directory | Drop-in configs | `/etc/rsyslog.d/` |
| Selector format | `facility.priority` | `*.info` or `auth.warning` |
| Action format | Destination for logs | `/var/log/messages` or `@192.168.1.100` |
| Restart service | Apply configuration changes | `systemctl restart rsyslog` |

## Syslog Facilities

| Facility | Description | Keyword | Number |
|----------|-------------|---------|--------|
| Kernel messages | Kernel messages | `kern` | 0 |
| User-level messages | User programs | `user` | 1 |
| Mail system | Mail system | `mail` | 2 |
| System daemons | System daemons | `daemon` | 3 |
| Security/authorization | Auth messages | `auth` or `security` | 4 |
| Internal syslogd | Syslogd messages | `syslog` | 5 |
| Line printer subsystem | Printer messages | `lpr` | 6 |
| Network news subsystem | News system | `news` | 7 |
| UUCP subsystem | UUCP system | `uucp` | 8 |
| Clock daemon | Time-related messages | `cron` | 9 |
| Security/authorization | Auth messages | `authpriv` | 10 |
| FTP daemon | FTP daemon | `ftp` | 11 |
| NTP subsystem | NTP subsystem | `ntp` | 12 |
| Log audit | Log audit | `audit` | 13 |
| Log alert | Log alert | `alert` | 14 |
| Clock daemon | Clock daemon | `clock` | 15 |
| Local use 0-7 | Reserved for local use | `local0` - `local7` | 16-23 |

## Rsyslog Configuration Examples

### Remote Logging (Client Side)
```
# Send all logs to a remote server
*.* @192.168.1.100:514          # UDP
*.* @@192.168.1.100:514         # TCP
```

### Remote Logging (Server Side)
```
# Receive logs from remote hosts
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")
```

### Custom Log Format
```
$template CustomFormat,"%timegenerated% %HOSTNAME% %syslogtag% %msg%\n"
*.* /var/log/custom.log;CustomFormat
```

## Logrotate

| Item | Description | Example |
|------|-------------|---------|
| Configuration file | Main config file | `/etc/logrotate.conf` |
| Configuration directory | App-specific configs | `/etc/logrotate.d/` |
| Manual rotation | Force rotation | `logrotate -f /etc/logrotate.conf` |
| Debug mode | Test configuration | `logrotate -d /etc/logrotate.conf` |

### Logrotate Configuration Options

| Option | Description | Example |
|--------|-------------|---------|
| `rotate n` | Keep n rotated logs | `rotate 7` |
| `daily` | Rotate logs daily | `daily` |
| `weekly` | Rotate logs weekly | `weekly` |
| `monthly` | Rotate logs monthly | `monthly` |
| `compress` | Compress rotated logs | `compress` |
| `delaycompress` | Compress on next rotation | `delaycompress` |
| `missingok` | Don't error if log missing | `missingok` |
| `notifempty` | Don't rotate empty logs | `notifempty` |
| `create mode owner group` | Create new log with permissions | `create 0644 root root` |
| `size size` | Rotate when log reaches size | `size 100M` |
| `dateext` | Add date extension | `dateext` |
| `maxage days` | Remove logs older than days | `maxage 365` |
| `postrotate` | Commands to run after rotation | Commands between `postrotate` and `endscript` |

### Sample Logrotate Configuration
```
/var/log/custom.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0644 root root
    postrotate
        systemctl reload rsyslog
    endscript
}
```

## Scripting for Log Analysis

### Bash Function to Monitor Logs
```bash
monitor_log() {
    local log_file="$1"
    local pattern="$2"
    local notify_cmd="$3"
    
    tail -f "$log_file" | while read line; do
        if echo "$line" | grep -q "$pattern"; then
            echo "[ALERT] Pattern found: $line"
            eval "$notify_cmd \"$line\""
        fi
    done
}

# Example usage:
# monitor_log "/var/log/auth.log" "Failed password" "mail -s 'Login failure' admin@example.com"
```

### Simple Log Entry Generator
```bash
log_event() {
    local level="$1"
    local message="$2"
    local log_file="$3"
    
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" >> "$log_file"
    
    # Also send to syslog if requested
    if [ "$4" = "syslog" ]; then
        logger -p user.$level "$message"
    fi
}

# Example usage:
# log_event "error" "Backup process failed" "/var/log/myapp.log" "syslog"
```

### Scan for Failed SSH Logins
```bash
#!/bin/bash

LOG_FILE="/var/log/auth.log"
REPORT_FILE="/var/log/ssh_attempts.log"
EMAIL="admin@example.com"

echo "SSH login failure report generated on $(date)" > "$REPORT_FILE"
echo "---------------------------------------------" >> "$REPORT_FILE"

grep "Failed password" "$LOG_FILE" | tail -n 50 >> "$REPORT_FILE"

# Count attempts by IP
echo -e "\nAttempts by IP address:" >> "$REPORT_FILE"
grep "Failed password" "$LOG_FILE" | grep -oE "from ([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c | sort -nr >> "$REPORT_FILE"

# Send report by email
mail -s "SSH Login Failure Report" "$EMAIL" < "$REPORT_FILE"
```

## Troubleshooting Log Issues

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| Log file growing too large | Excessive logging, no rotation | Set up logrotate, increase rotation frequency |
| Running out of disk space | Logs not being rotated/deleted | Configure logrotate with limits, use `logrotate -f` |
| Missing logs | Log service not running | Check rsyslog status, restart if needed |
| Cannot view logs with journalctl | Journal not persistent | Edit `/etc/systemd/journald.conf`, set `Storage=persistent` |
| Too many old logs | Retention policy too long | Adjust logrotate settings, run `journalctl --vacuum-time=1month` |
| Application not logging | Incorrect permissions | Check app log configuration, ensure write permissions |
| Remote logging not working | Firewall/network issues | Check firewall rules, verify rsyslog configuration |

## Basic Log Analysis with awk/sed

### Extract Time and Error Message with awk
```bash
awk '/error/ {print $1,$2,$3,$0}' /var/log/syslog
```

### Count Occurrences by Category with awk
```bash
awk '/sshd/ {print $6}' /var/log/auth.log | sort | uniq -c | sort -nr
```

### Format Output with sed
```bash
sed -n 's/.*Failed password for \([^ ]*\) from \([0-9.]*\).*/User: \1 IP: \2/p' /var/log/auth.log
```

## Sending Log Alerts

### Email Alert for Critical Errors
```bash
#!/bin/bash
LOG_FILE="/var/log/syslog"
PATTERN="critical|emergency"
EMAIL="admin@example.com"

if grep -iE "$PATTERN" "$LOG_FILE" | grep -i "$(date '+%b %e')"; then
    grep -iE "$PATTERN" "$LOG_FILE" | grep -i "$(date '+%b %e')" | 
    mail -s "CRITICAL: Server errors detected" "$EMAIL"
fi
```

## Security Best Practices for Logs

1. **Store logs securely** - Protect log files with proper permissions (typically 640 or 600)
2. **Forward logs to a secure log server** - Keep copies of logs separate from the originating system
3. **Implement log rotation** - Prevent logs from consuming all disk space
4. **Maintain logs for an appropriate duration** - Balance security needs with storage constraints
5. **Use timestamps in UTC** - Makes correlation across systems easier
6. **Include relevant context** - Ensure logs contain necessary information for analysis
7. **Monitor logs regularly** - Set up automated alerts for critical events
8. **Protect against log injection** - Validate and sanitize logged data where possible
9. **Implement integrity checking** - Detect unauthorized modification of logs
10. **Establish a log review process** - Regular review helps identify security issues 