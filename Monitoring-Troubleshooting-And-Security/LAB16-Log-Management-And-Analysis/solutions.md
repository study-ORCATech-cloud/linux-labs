# LAB16 - Log Management and Analysis Solutions

This file contains solutions to the exercises in LAB16. Try to solve the exercises yourself before looking at these solutions.

## Exercise 1: Exploring Log Files

```bash
# 1. List important log files
ls -lh /var/log/

# Important log files include:
# - /var/log/syslog or /var/log/messages (general system logs)
# - /var/log/auth.log or /var/log/secure (authentication logs)
# - /var/log/kern.log (kernel logs)
# - /var/log/dmesg (boot messages)
# - /var/log/apache2/ or /var/log/httpd/ (web server logs if installed)

# 2. View system log file
sudo less /var/log/syslog   # Ubuntu/Debian
# or
sudo less /var/log/messages # CentOS/RHEL

# 3. View authentication log
sudo less /var/log/auth.log  # Ubuntu/Debian
# or
sudo less /var/log/secure    # CentOS/RHEL

# 4. View kernel log messages
sudo less /var/log/kern.log
# or
dmesg | less

# 5. Check web server logs (if installed)
ls -l /var/log/apache2/     # Ubuntu/Debian
# or
ls -l /var/log/httpd/       # CentOS/RHEL
```

## Exercise 2: Basic Log Analysis

```bash
# 1. Find error messages in system log from today
grep -i error /var/log/syslog | grep "$(date '+%b %e')"

# 2. Extract login failure messages
grep "Failed password" /var/log/auth.log

# 3. Find kernel errors
grep -E "error|fail" /var/log/kern.log
# or
dmesg | grep -E "error|fail"

# 4. Count SSH login attempts in last 24 hours
grep "sshd" /var/log/auth.log | grep "$(date -d '24 hours ago' '+%b %e')" | wc -l
# Note: This is approximate as it doesn't account for midnight crossing

# 5. Create file with USB connection messages
grep -i "usb" /var/log/kern.log > usb_connections.log
```

## Exercise 3: Using Log Analysis Tools

```bash
# 1. View systemd logs
sudo journalctl

# 2. Filter to show only error messages
sudo journalctl -p err

# 3. View logs for specific time range
sudo journalctl --since "2023-07-01 14:00:00" --until "2023-07-01 16:00:00"
# Replace with current date and times

# 4. Export journal entries from last hour
sudo journalctl --since "1 hour ago" > journal_last_hour.log

# 5. Follow logs in real-time
sudo journalctl -f
# (Press Ctrl+C to stop)
```

## Exercise 4: Log Rotation

```bash
# 1. Examine logrotate configuration
cat /etc/logrotate.conf
ls -l /etc/logrotate.d/

# 2. Identify rotation configuration for specific logs
grep -r "rotate" /etc/logrotate.d/

# 3. Create custom logrotate configuration
sudo nano /etc/logrotate.d/custom_log

# Example content:
# /var/log/custom.log {
#     weekly
#     rotate 4
#     compress
#     delaycompress
#     missingok
#     notifempty
#     create 0640 root root
# }

# 4. Manually trigger log rotation (test mode)
sudo logrotate -d /etc/logrotate.conf  # Test without rotating

# Actually rotate the logs
sudo logrotate -f /etc/logrotate.conf

# 5. Verify rotation worked
ls -l /var/log/
# Look for rotated logs with numbers and possibly .gz extensions
```

## Exercise 5: Creating Logging Scripts

```bash
# 1. Script to generate log entries
cat > log_generator.sh << 'EOF'
#!/bin/bash
LOG_FILE="/var/log/custom_events.log"

log_event() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$1] $2" >> "$LOG_FILE"
}

# Generate some sample logs
log_event "INFO" "System check started"
log_event "WARNING" "Available disk space below 30%"
log_event "ERROR" "Failed to connect to database"
log_event "INFO" "System check completed"

echo "Log entries written to $LOG_FILE"
EOF
chmod +x log_generator.sh

# 2. Script to check disk space
cat > disk_check.sh << 'EOF'
#!/bin/bash
LOG_FILE="/var/log/disk_space.log"

log_with_timestamp() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG_FILE"
}

# Check each mounted filesystem
df -h | grep -vE "^Filesystem|tmpfs|cdrom" | while read line; do
    # Extract disk space information
    usage=$(echo $line | awk '{print $5}' | sed 's/%//')
    mount=$(echo $line | awk '{print $6}')
    
    if [ "$usage" -ge 80 ]; then
        log_with_timestamp "CRITICAL: $mount is $usage% full"
    elif [ "$usage" -ge 20 ]; then
        log_with_timestamp "WARNING: $mount is $usage% full"
    else
        log_with_timestamp "INFO: $mount is $usage% full"
    fi
done

echo "Disk space check completed and logged to $LOG_FILE"
EOF
chmod +x disk_check.sh

# 3. Script to monitor SSH login attempts
cat > ssh_monitor.sh << 'EOF'
#!/bin/bash
AUTH_LOG="/var/log/auth.log"
CUSTOM_LOG="/var/log/ssh_failures.log"

# Create log file if it doesn't exist
touch "$CUSTOM_LOG"

# Get the last line number we processed
if [ -f "$CUSTOM_LOG.lastpos" ]; then
    last_pos=$(cat "$CUSTOM_LOG.lastpos")
else
    last_pos=0
fi

# Find new failed login attempts
current_pos=$(wc -l < "$AUTH_LOG")
new_entries=$(tail -n $((current_pos - last_pos)) "$AUTH_LOG" | grep "Failed password")

if [ ! -z "$new_entries" ]; then
    echo "--- New failed login attempts at $(date) ---" >> "$CUSTOM_LOG"
    echo "$new_entries" >> "$CUSTOM_LOG"
    
    # Count failures by IP
    echo "--- Failures by IP address ---" >> "$CUSTOM_LOG"
    echo "$new_entries" | grep -oE "from ([0-9]{1,3}\.){3}[0-9]{1,3}" | 
    sort | uniq -c | sort -nr >> "$CUSTOM_LOG"
    echo "" >> "$CUSTOM_LOG"
fi

# Save current position
echo "$current_pos" > "$CUSTOM_LOG.lastpos"
EOF
chmod +x ssh_monitor.sh

# 4. Script to archive old logs
cat > log_archiver.sh << 'EOF'
#!/bin/bash
LOG_DIR="/var/log"
ARCHIVE_DIR="/var/log/archives"
DAYS_OLD=30

# Create archive directory if it doesn't exist
mkdir -p "$ARCHIVE_DIR"

# Find log files older than 30 days
find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS_OLD | while read -r logfile; do
    filename=$(basename "$logfile")
    archive_name="$ARCHIVE_DIR/${filename}_$(date '+%Y%m%d').tar.gz"
    
    # Archive and compress the file
    tar -czf "$archive_name" "$logfile"
    
    if [ $? -eq 0 ]; then
        echo "Archived $logfile to $archive_name"
        # Optionally truncate the original log file
        # cat /dev/null > "$logfile"
    else
        echo "Failed to archive $logfile"
    fi
done
EOF
chmod +x log_archiver.sh

# 5. Simple log rotation script
cat > simple_rotate.sh << 'EOF'
#!/bin/bash
LOG_FILE=$1
MAX_LOGS=5

if [ -z "$LOG_FILE" ]; then
    echo "Usage: $0 <log_file_path>"
    exit 1
fi

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file $LOG_FILE does not exist"
    exit 1
fi

# Rotate logs
for i in $(seq $((MAX_LOGS-1)) -1 1); do
    if [ -f "${LOG_FILE}.$i" ]; then
        mv "${LOG_FILE}.$i" "${LOG_FILE}.$((i+1))"
    fi
done

# Rotate current log
if [ -f "$LOG_FILE" ]; then
    mv "$LOG_FILE" "${LOG_FILE}.1"
    touch "$LOG_FILE"
    chmod --reference="${LOG_FILE}.1" "$LOG_FILE"
fi

echo "Log rotation completed for $LOG_FILE"
EOF
chmod +x simple_rotate.sh
```

## Exercise 6: Centralized Logging

```bash
# 1. Configure rsyslog to send logs to a central server
sudo nano /etc/rsyslog.d/remote.conf

# Add the following for UDP logging (replace with your server IP)
# *.* @192.168.1.100:514
# Or for TCP logging:
# *.* @@192.168.1.100:514

# 2. Configure app to log to custom facility
sudo nano /etc/rsyslog.d/custom-app.conf

# Add the following:
# local3.* /var/log/custom-app.log

# Example of sending logs with logger:
logger -p local3.info "Test message for custom application"

# 3. Set up log filtering
sudo nano /etc/rsyslog.d/filter.conf

# Add rules like:
# :msg, contains, "error" /var/log/important_errors.log
# :msg, contains, "critical" /var/log/important_errors.log
# & stop

# 4. Test the centralized logging setup
systemctl restart rsyslog
logger "Test message for central logging"

# 5. Custom log format
sudo nano /etc/rsyslog.d/custom-format.conf

# Add:
# $template CustomFormat,"%TIMESTAMP:::date-rfc3339% %HOSTNAME% %syslogtag%%msg%\n"
# *.* /var/log/formatted.log;CustomFormat
```

## Exercise 7: Log Monitoring and Alerting

```bash
# 1. Script to monitor logs for errors
cat > log_monitor.sh << 'EOF'
#!/bin/bash
LOG_FILE="/var/log/syslog"
PATTERN="error|critical|failed"
OUTPUT_FILE="/tmp/error_report.txt"

grep -iE "$PATTERN" "$LOG_FILE" | grep "$(date '+%b %e')" > "$OUTPUT_FILE"

if [ -s "$OUTPUT_FILE" ]; then
    echo "Errors found in logs. See $OUTPUT_FILE for details."
else
    echo "No errors found in today's logs."
fi
EOF
chmod +x log_monitor.sh

# 2. Add email alerting to the script
cat > email_alert.sh << 'EOF'
#!/bin/bash
LOG_FILE="/var/log/syslog"
PATTERN="error|critical|failed"
EMAIL="admin@example.com"
SUBJECT="Log Error Alert"

# Check for errors in today's logs
ERRORS=$(grep -iE "$PATTERN" "$LOG_FILE" | grep "$(date '+%b %e')")

if [ ! -z "$ERRORS" ]; then
    echo "The following errors were found in the logs:" | 
    mail -s "$SUBJECT" "$EMAIL" << EOF_MAIL
Date: $(date)
Host: $(hostname)

$ERRORS
EOF_MAIL
    echo "Alert email sent to $EMAIL"
fi
EOF
chmod +x email_alert.sh

# 3. Set up cron job
crontab -e

# Add:
# */30 * * * * /path/to/email_alert.sh

# 4. Create summary report script
cat > log_summary.sh << 'EOF'
#!/bin/bash
LOG_FILE="/var/log/syslog"
REPORT_FILE="/var/log/daily_summary.txt"

echo "Log Summary Report - $(date '+%Y-%m-%d')" > "$REPORT_FILE"
echo "=================================" >> "$REPORT_FILE"

echo -e "\nError Count by Type:" >> "$REPORT_FILE"
grep -i "error" "$LOG_FILE" | awk '{print $5}' | sort | uniq -c | sort -nr >> "$REPORT_FILE"

echo -e "\nWarning Count by Type:" >> "$REPORT_FILE"
grep -i "warning" "$LOG_FILE" | awk '{print $5}' | sort | uniq -c | sort -nr >> "$REPORT_FILE"

echo -e "\nMost Recent Critical Errors:" >> "$REPORT_FILE"
grep -i "critical" "$LOG_FILE" | tail -n 10 >> "$REPORT_FILE"

echo "Summary report created at $REPORT_FILE"
EOF
chmod +x log_summary.sh

# 5. Simple log dashboard script
cat > log_dashboard.sh << 'EOF'
#!/bin/bash
# Simple CLI dashboard for recent log errors

clear
echo "==============================================="
echo "           SYSTEM LOG DASHBOARD"
echo "==============================================="
echo "Generated: $(date)"
echo "Hostname: $(hostname)"
echo "==============================================="

echo -e "\nRecent Authentication Failures:"
grep "Failed password" /var/log/auth.log | tail -5

echo -e "\nRecent System Errors:"
grep -i "error" /var/log/syslog | tail -5

echo -e "\nRecent Critical Alerts:"
grep -iE "critical|emergency" /var/log/syslog | tail -5

echo -e "\nSystem Load:"
uptime

echo -e "\nDisk Space:"
df -h | grep -vE "tmpfs|udev"

echo "==============================================="
EOF
chmod +x log_dashboard.sh
```

## Bonus Challenge Solution

Here's a framework for a comprehensive log analysis system:

```bash
#!/bin/bash
# log_analyzer.sh - A comprehensive log analysis system

# Configuration
LOG_DIR="/var/log"
ARCHIVE_DIR="/var/log/archives"
REPORT_DIR="/var/log/reports"
CUSTOM_LOG_DIR="/var/log/custom"
EMAIL="admin@example.com"
RETENTION_DAYS=30

# Create necessary directories
mkdir -p "$ARCHIVE_DIR" "$REPORT_DIR" "$CUSTOM_LOG_DIR"

# Log collection function
collect_logs() {
    local source_dir="$1"
    local target_dir="$2"
    local timestamp="$(date '+%Y%m%d_%H%M%S')"
    
    # Create timestamp directory for this collection
    mkdir -p "$target_dir/$timestamp"
    
    # Copy important logs
    cp "$LOG_DIR/syslog" "$target_dir/$timestamp/"
    cp "$LOG_DIR/auth.log" "$target_dir/$timestamp/"
    cp "$LOG_DIR/kern.log" "$target_dir/$timestamp/"
    
    # If apache is installed, get those logs too
    if [ -d "$LOG_DIR/apache2" ]; then
        mkdir -p "$target_dir/$timestamp/apache2"
        cp "$LOG_DIR/apache2/access.log" "$target_dir/$timestamp/apache2/"
        cp "$LOG_DIR/apache2/error.log" "$target_dir/$timestamp/apache2/"
    fi
    
    echo "Logs collected to $target_dir/$timestamp"
    echo "$timestamp"  # Return the timestamp
}

# Log normalization function
normalize_logs() {
    local source_dir="$1"
    local timestamp="$2"
    local target_dir="$CUSTOM_LOG_DIR/normalized_$timestamp"
    
    mkdir -p "$target_dir"
    
    # Process syslog - extract timestamp, hostname, facility, and message
    if [ -f "$source_dir/$timestamp/syslog" ]; then
        awk '{print $1,$2,$3,$4,$5,$6,$7"...",$0}' "$source_dir/$timestamp/syslog" > "$target_dir/syslog_normalized.log"
    fi
    
    # Process auth log - extract timestamp, action, and details
    if [ -f "$source_dir/$timestamp/auth.log" ]; then
        awk '{print $1,$2,$3,$4,$5,$6,$7"...",$0}' "$source_dir/$timestamp/auth.log" > "$target_dir/auth_normalized.log"
    fi
    
    echo "Logs normalized to $target_dir"
}

# Pattern detection function
detect_patterns() {
    local normalized_dir="$1"
    local report_file="$2"
    
    echo "Security Analysis Report - $(date)" > "$report_file"
    echo "=====================================" >> "$report_file"
    
    # Check for failed logins
    echo -e "\n=== Failed Login Attempts ===" >> "$report_file"
    grep -i "failed password" "$normalized_dir/auth_normalized.log" 2>/dev/null | 
    awk '{print $1,$2,$3,$NF}' | sort | uniq -c | sort -nr >> "$report_file"
    
    # Check for suspicious sudo usage
    echo -e "\n=== Sudo Usage ===" >> "$report_file"
    grep -i "sudo" "$normalized_dir/auth_normalized.log" 2>/dev/null | 
    grep -v "session closed" | awk '{print $1,$2,$3,$NF}' >> "$report_file"
    
    # Check for system errors
    echo -e "\n=== System Errors ===" >> "$report_file"
    grep -iE "error|critical|fail" "$normalized_dir/syslog_normalized.log" 2>/dev/null | 
    awk '{print $1,$2,$3,$NF}' | sort | uniq -c | sort -nr >> "$report_file"
    
    echo "Pattern detection complete. Report at $report_file"
}

# Generate statistics report
generate_statistics() {
    local normalized_dir="$1"
    local stats_file="$2"
    
    echo "Log Statistics Report - $(date)" > "$stats_file"
    echo "=====================================" >> "$stats_file"
    
    # Count events by hour
    echo -e "\n=== Events by Hour ===" >> "$stats_file"
    awk '{print $3}' "$normalized_dir/syslog_normalized.log" 2>/dev/null | 
    cut -d: -f1 | sort | uniq -c >> "$stats_file"
    
    # Count events by type
    echo -e "\n=== Events by Type ===" >> "$stats_file"
    awk '{print $6}' "$normalized_dir/syslog_normalized.log" 2>/dev/null | 
    sort | uniq -c | sort -nr >> "$stats_file"
    
    # Count authentication events by type
    echo -e "\n=== Auth Events by Type ===" >> "$stats_file"
    awk '{print $6}' "$normalized_dir/auth_normalized.log" 2>/dev/null | 
    sort | uniq -c | sort -nr >> "$stats_file"
    
    echo "Statistics generated. Report at $stats_file"
}

# Alert function
send_alert() {
    local report_file="$1"
    local email="$2"
    
    # Check if there are critical issues to alert on
    if grep -qiE "critical|failed password|error" "$report_file"; then
        mail -s "CRITICAL: Security issues detected on $(hostname)" "$email" < "$report_file"
        echo "Alert email sent to $email"
    else
        echo "No critical issues detected. No alert sent."
    fi
}

# Archive old logs function
archive_old_logs() {
    local dir="$1"
    local days="$2"
    
    find "$dir" -type d -name "normalized_*" -mtime +$days | while read -r old_dir; do
        archive_name="$(basename "$old_dir")_$(date '+%Y%m%d').tar.gz"
        tar -czf "$ARCHIVE_DIR/$archive_name" "$old_dir"
        if [ $? -eq 0 ]; then
            echo "Archived $old_dir to $ARCHIVE_DIR/$archive_name"
            rm -rf "$old_dir"
        else
            echo "Failed to archive $old_dir"
        fi
    done
}

# Main execution
echo "Starting log analysis system at $(date)"
timestamp=$(collect_logs "$LOG_DIR" "$CUSTOM_LOG_DIR")
normalize_logs "$CUSTOM_LOG_DIR" "$timestamp"

# Generate reports
normalized_dir="$CUSTOM_LOG_DIR/normalized_$timestamp"
security_report="$REPORT_DIR/security_report_$timestamp.txt"
stats_report="$REPORT_DIR/stats_report_$timestamp.txt"

detect_patterns "$normalized_dir" "$security_report"
generate_statistics "$normalized_dir" "$stats_report"
send_alert "$security_report" "$EMAIL"
archive_old_logs "$CUSTOM_LOG_DIR" "$RETENTION_DAYS"

echo "Log analysis completed at $(date)"
```

## Cleanup

```bash
# Remove custom log files
rm -f /var/log/custom_events.log
rm -f /var/log/disk_space.log
rm -f /var/log/ssh_failures.log
rm -f /var/log/ssh_failures.log.lastpos
rm -f /var/log/daily_summary.txt
rm -f usb_connections.log
rm -f journal_last_hour.log

# Remove custom scripts
rm -f log_generator.sh disk_check.sh ssh_monitor.sh 
rm -f log_archiver.sh simple_rotate.sh log_monitor.sh
rm -f email_alert.sh log_summary.sh log_dashboard.sh
rm -f log_analyzer.sh

# Restore rsyslog configuration (if modified)
sudo rm -f /etc/rsyslog.d/remote.conf
sudo rm -f /etc/rsyslog.d/custom-app.conf
sudo rm -f /etc/rsyslog.d/filter.conf
sudo rm -f /etc/rsyslog.d/custom-format.conf

# Remove logrotate configuration (if created)
sudo rm -f /etc/logrotate.d/custom_log

# Restart rsyslog to apply original configuration
sudo systemctl restart rsyslog

# Remove cron job if added
crontab -l | grep -v "email_alert.sh" | crontab -

# Remove report and archive directories if created
sudo rm -rf /var/log/reports /var/log/archives /var/log/custom
``` 