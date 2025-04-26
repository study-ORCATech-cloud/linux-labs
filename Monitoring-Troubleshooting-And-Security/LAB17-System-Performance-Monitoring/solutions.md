# LAB17 - System Performance Monitoring Solutions

This file contains solutions to the exercises in LAB17. Try to solve the exercises yourself before looking at these solutions.

## Exercise 1: Basic System Monitoring

```bash
# 1. View current system resource usage
top

# 2. Identify CPU-intensive processes
# Look at the %CPU column in top (processes are sorted by CPU usage by default)
# You can also use:
ps aux --sort=-%cpu | head -n 10

# 3. Sort processes by memory usage in top
# Press 'M' while in top

# 4. Find and terminate a high CPU process
# Create a CPU-intensive process for testing:
yes > /dev/null &
# Note the PID shown in the output
# Then terminate it:
kill <PID>
# Or using top: press 'k', enter the PID, confirm with Enter

# 5. Analyze load average
uptime
# The three values represent load average over 1, 5, and 15 minutes
# Load average of 1.0 on a single-core system means 100% CPU utilization
# On multi-core systems, divide by number of cores (e.g., 4.0 on 4 cores = 100%)
# Values consistently above these thresholds indicate CPU bottlenecks
```

## Exercise 2: Advanced Process Monitoring with htop

```bash
# 1. Install htop
sudo apt install htop    # Debian/Ubuntu
sudo yum install htop    # CentOS/RHEL
sudo dnf install htop    # Fedora

# 2. Launch htop
htop

# 3. Sort processes by different metrics
# CPU: Press F6, select CPU%
# Memory: Press F6, select MEM%
# Time: Press F6, select TIME+

# 4. Filter processes by user
# Press u, select a username from the list

# 5. Change process priority
# Select a process using arrow keys
# Press F7 to decrease priority (higher nice value)
# Press F8 to increase priority (lower nice value)
# Nice values range from -20 (highest priority) to 19 (lowest priority)
```

## Exercise 3: Memory Analysis

```bash
# 1. Display memory usage in human-readable format
free -h

# 2. Analyze buffer and cache
# From the free -h output:
# - buffers: Kernel buffers, temporary storage for raw disk blocks
# - cache: Page cache, used to cache files from disk
# These can be released when applications need memory
# "available" shows memory that can be allocated without swapping

# 3. Observe memory usage over time
watch -n 2 "free -h"

# 4. Use vmstat for memory, CPU, and I/O statistics
vmstat 2 5  # Update every 2 seconds, 5 times
# The first line shows averages since boot
# Subsequent lines show real-time statistics

# 5. Script to alert when free memory is low
cat > memory_alert.sh << 'EOF'
#!/bin/bash

THRESHOLD=20  # Percentage
LOG_FILE="/tmp/memory_alerts.log"

while true; do
    # Calculate free memory percentage
    MEM_INFO=$(free | grep Mem)
    TOTAL_MEM=$(echo "$MEM_INFO" | awk '{print $2}')
    AVAIL_MEM=$(echo "$MEM_INFO" | awk '{print $7}')
    FREE_PERCENT=$(echo "scale=2; $AVAIL_MEM * 100 / $TOTAL_MEM" | bc)
    
    # Check if below threshold
    if (( $(echo "$FREE_PERCENT < $THRESHOLD" | bc -l) )); then
        echo "$(date): ALERT - Available memory is low: $FREE_PERCENT%" | tee -a "$LOG_FILE"
        echo "Top memory consumers:" | tee -a "$LOG_FILE"
        ps aux --sort=-%mem | head -n 5 | tee -a "$LOG_FILE"
    fi
    
    sleep 60
done
EOF

chmod +x memory_alert.sh
# Run it with: ./memory_alert.sh
```

## Exercise 4: Disk I/O Monitoring

```bash
# 1. Use iotop to monitor disk operations
sudo apt install iotop    # Debian/Ubuntu
sudo yum install iotop    # CentOS/RHEL
sudo iotop  # Run iotop
# Press 'o' to show only active processes
# Press 'a' to show accumulated I/O instead of bandwidth

# 2. Monitor disk I/O with iostat
sudo apt install sysstat    # Debian/Ubuntu
sudo yum install sysstat    # CentOS/RHEL
iostat -x 2 5  # Extended stats, every 2 seconds, 5 times
# Key metrics:
# - %util: Percentage of CPU time device was busy
# - await: Average time for I/O requests (ms)
# - r/s, w/s: Reads/writes per second

# 3. Create high disk I/O situation
# Method 1: Copy a large file
dd if=/dev/zero of=/tmp/largefile bs=1M count=1000
# Method 2: Force disk sync
sync
# Monitor in another terminal with iostat or iotop

# 4. Analyze disk space usage
df -h  # Shows disk space usage by filesystem
du -h --max-depth=1 /var  # Shows disk usage by directories in /var
du -sh /var/log/*  # Shows size of each item in /var/log

# 5. Script to report top 5 directories by size
cat > disk_space_report.sh << 'EOF'
#!/bin/bash

DIR=${1:-"/"}  # Default to root directory if not specified
REPORT_FILE="/tmp/disk_space_report.txt"

echo "Disk Space Report for $DIR - $(date)" > "$REPORT_FILE"
echo "=================================================" >> "$REPORT_FILE"

echo -e "\nTop 5 Directories by Size:" >> "$REPORT_FILE"
du -h --max-depth=1 "$DIR" 2>/dev/null | sort -hr | head -n 5 >> "$REPORT_FILE"

echo -e "\nFilesystem Usage:" >> "$REPORT_FILE"
df -h | grep -v "tmpfs\|devtmpfs" >> "$REPORT_FILE"

echo "Report saved to $REPORT_FILE"
EOF

chmod +x disk_space_report.sh
# Run it with: ./disk_space_report.sh /home
```

## Exercise 5: Network Performance Monitoring

```bash
# 1. List active network connections
# Using netstat
netstat -tuln  # TCP/UDP listening ports
netstat -anp  # All connections with process info
# Using ss (modern alternative)
ss -tuln  # TCP/UDP listening ports
ss -anp  # All connections with process info

# 2. Monitor real-time network traffic with iftop
sudo apt install iftop    # Debian/Ubuntu
sudo yum install iftop    # CentOS/RHEL
sudo iftop  # Monitor all interfaces
sudo iftop -i eth0  # Monitor specific interface
# Press 'h' for help, 'q' to quit

# 3. Check bandwidth usage by process
sudo apt install nethogs    # Debian/Ubuntu
sudo yum install nethogs    # CentOS/RHEL
sudo nethogs  # Monitor all interfaces
sudo nethogs eth0  # Monitor specific interface
# Press q to quit

# 4. Measure network latency
ping -c 10 google.com  # 10 pings to Google
# Look at the min/avg/max/mdev values in the summary

# 5. Network connectivity monitoring script
cat > network_monitor.sh << 'EOF'
#!/bin/bash

HOST="google.com"  # Target to monitor
INTERVAL=60  # Check every minute
LOG_FILE="/tmp/network_monitor.log"

echo "Starting network monitor for $HOST - $(date)" > "$LOG_FILE"

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Check connectivity
    if ping -c 1 -W 2 "$HOST" &>/dev/null; then
        echo "$timestamp - Connection to $HOST: UP" >> "$LOG_FILE"
    else
        echo "$timestamp - Connection to $HOST: DOWN" >> "$LOG_FILE"
        
        # Get more diagnostic info
        echo "$timestamp - Network diagnostic:" >> "$LOG_FILE"
        echo "-- Route --" >> "$LOG_FILE"
        ip route get 8.8.8.8 2>&1 >> "$LOG_FILE"
        echo "-- DNS --" >> "$LOG_FILE"
        host "$HOST" 2>&1 >> "$LOG_FILE"
    fi
    
    sleep "$INTERVAL"
done
EOF

chmod +x network_monitor.sh
# Run in background: ./network_monitor.sh &
```

## Exercise 6: System Load Analysis

```bash
# 1. Display system load
uptime
# Output shows current time, uptime, users, and load averages

# 2. Install and use stress tools
sudo apt install stress stress-ng    # Debian/Ubuntu
sudo yum install stress stress-ng    # CentOS/RHEL

# Stress CPU
stress --cpu 2 --timeout 30s  # Use 2 CPU cores for 30 seconds
# Stress memory
stress --vm 1 --vm-bytes 500M --timeout 30s
# Stress I/O
stress --io 2 --timeout 30s
# Combined stress test
stress --cpu 2 --vm 1 --vm-bytes 500M --io 2 --timeout 60s

# More advanced stress with stress-ng
stress-ng --cpu 2 --cpu-method matrixprod --timeout 30s
stress-ng --vm 1 --vm-bytes 500M --vm-method flip --timeout 30s

# 3. Monitor stress test impact
# While stress is running, open separate terminals and run:
top  # General monitoring
htop  # Enhanced monitoring
vmstat 1  # System stats every second
iostat -x 1  # I/O stats every second

# 4. Identify bottlenecks
# CPU bottleneck: High CPU usage, low iowait, high load
# Memory bottleneck: High memory usage, swap activity, high page-in/page-out in vmstat
# I/O bottleneck: High iowait in CPU stats, high disk utilization in iostat
# Network bottleneck: Use iftop/nethogs to confirm

# 5. Run CPU-intensive process with lower priority
nice -n 19 stress --cpu 1 --timeout 30s  # Lowest priority
# Compare to normal priority
stress --cpu 1 --timeout 30s
```

## Exercise 7: Performance Data Collection and Visualization

```bash
# 1. Install sysstat
sudo apt install sysstat    # Debian/Ubuntu
sudo yum install sysstat    # CentOS/RHEL

# Configure sysstat to collect data
sudo systemctl enable sysstat
sudo systemctl start sysstat

# 2. Set up periodic data collection
# Edit the sysstat configuration
sudo vi /etc/cron.d/sysstat  # Ubuntu/Debian
# or
sudo vi /etc/sysconfig/sysstat  # CentOS/RHEL

# Ensure data collection is enabled
sudo vi /etc/default/sysstat  # Ubuntu/Debian
# Change ENABLED="false" to ENABLED="true" if needed

# 3. Collect performance metrics manually
# CPU activity
sar -u 1 3600  # CPU usage every 1 second for 1 hour
# Memory
sar -r 1 3600  # Memory usage every 1 second for 1 hour
# Disk I/O
sar -b 1 3600  # Disk activity every 1 second for 1 hour
# Network
sar -n DEV 1 3600  # Network activity every 1 second for 1 hour

# 4. Generate reports from collected data
# For today's data:
sar  # CPU
sar -r  # Memory
sar -b  # Disk I/O
sar -n DEV  # Network

# For data from a specific day:
sar -f /var/log/sysstat/sa20  # 20th day of the month

# 5. Simple performance dashboard script
cat > performance_dashboard.sh << 'EOF'
#!/bin/bash

clear
echo "======================================"
echo "System Performance Dashboard"
echo "======================================"
echo "Generated: $(date)"
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime)"
echo "--------------------------------------"

echo -e "\n------ CPU ------"
mpstat | grep -A 2 "%usr"

echo -e "\n------ Memory ------"
free -h

echo -e "\n------ Disk Usage ------"
df -h | grep -vE "tmpfs|devtmpfs"

echo -e "\n------ Disk I/O (Top 5) ------"
iostat -x | head -n 7

echo -e "\n------ Network ------"
netstat -i | head -n 7

echo -e "\n------ Load Average History (1-hour) ------"
sar -q | grep -v -e "^$" -e "Average" | tail -n 12

echo -e "\n------ Top Processes (CPU) ------"
ps aux --sort=-%cpu | head -n 6

echo -e "\n------ Top Processes (Memory) ------"
ps aux --sort=-%mem | head -n 6

echo "======================================"
EOF

chmod +x performance_dashboard.sh
# Run it with: ./performance_dashboard.sh
```

## Bonus Challenge - Comprehensive Monitoring Solution

```bash
#!/bin/bash
# system_monitor.sh - Comprehensive system monitoring solution

# Configuration
WATCH_INTERVAL=60  # Check every minute
CPU_THRESHOLD=80   # CPU usage threshold (%)
MEM_THRESHOLD=80   # Memory usage threshold (%)
DISK_THRESHOLD=90  # Disk usage threshold (%)
REPORT_DIR="/var/log/system_monitor"
LOG_FILE="$REPORT_DIR/system_monitor.log"
DAILY_REPORT="$REPORT_DIR/daily_report_$(date +%Y%m%d).txt"
EMAIL="admin@example.com"  # Change to your email

# Create report directory
mkdir -p "$REPORT_DIR"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
    echo "$1"
}

# Check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check dependencies
check_deps() {
    for cmd in bc awk grep sort head; do
        if ! command_exists "$cmd"; then
            echo "Error: Required command '$cmd' not found. Please install it."
            exit 1
        fi
    done
    
    # Optional tools
    for cmd in iostat mpstat sar; do
        if ! command_exists "$cmd"; then
            log "Warning: '$cmd' not found. Some features will be limited."
        fi
    done
}

# Get CPU usage
get_cpu_usage() {
    # Method 1: Using top
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    
    # Method 2: Using mpstat if available
    if command_exists mpstat; then
        CPU_USAGE=$(mpstat 1 1 | awk '/Average:/ {print 100 - $12}')
    fi
    
    echo "$CPU_USAGE"
}

# Get memory usage
get_mem_usage() {
    MEM_INFO=$(free | grep Mem)
    TOTAL=$(echo "$MEM_INFO" | awk '{print $2}')
    USED=$(echo "$MEM_INFO" | awk '{print $3}')
    PERCENTAGE=$(echo "scale=2; $USED * 100 / $TOTAL" | bc)
    
    echo "$PERCENTAGE"
}

# Check disk usage for each partition
check_disk_usage() {
    df -h | grep -vE "tmpfs|devtmpfs|Filesystem" | while read -r line; do
        USAGE=$(echo "$line" | awk '{print $5}' | sed 's/%//')
        MOUNT=$(echo "$line" | awk '{print $6}')
        
        if [ "$USAGE" -ge "$DISK_THRESHOLD" ]; then
            log "ALERT: Disk usage for $MOUNT is critical: $USAGE%"
            return 1
        fi
    done
    
    return 0
}

# Get top resource consumers
get_top_consumers() {
    echo "Top CPU Consumers:"
    ps aux --sort=-%cpu | head -n 6
    
    echo -e "\nTop Memory Consumers:"
    ps aux --sort=-%mem | head -n 6
    
    if command_exists iostat; then
        echo -e "\nDisk I/O Stats:"
        iostat -x | head -n 7
    fi
}

# Generate performance suggestions
generate_suggestions() {
    CPU_USAGE=$1
    MEM_USAGE=$2
    DISK_FULL=$3
    
    echo "Performance Suggestions:"
    
    if [ "$(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc)" -eq 1 ]; then
        echo "- High CPU usage detected. Consider:"
        echo "  * Identifying and optimizing CPU-intensive processes"
        echo "  * Using nice to prioritize important processes"
        echo "  * Distributing load or scaling up CPU resources"
    fi
    
    if [ "$(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc)" -eq 1 ]; then
        echo "- High memory usage detected. Consider:"
        echo "  * Checking for memory leaks in applications"
        echo "  * Adjusting application memory limits"
        echo "  * Adding more RAM if consistently high"
    fi
    
    if [ "$DISK_FULL" -eq 1 ]; then
        echo "- Disk space issues detected. Consider:"
        echo "  * Cleaning up temporary files and logs"
        echo "  * Implementing log rotation"
        echo "  * Moving data to additional storage"
    fi
    
    # I/O suggestions
    if command_exists iostat; then
        IOWAIT=$(iostat | awk '/^avg-cpu:/ {getline; print $4}')
        if [ "$(echo "$IOWAIT > 10" | bc)" -eq 1 ]; then
            echo "- High I/O wait detected. Consider:"
            echo "  * Using faster storage (SSD)"
            echo "  * Optimizing applications for better I/O patterns"
            echo "  * Checking for disk health issues"
        fi
    fi
}

# Send email alert
send_alert() {
    SUBJECT="ALERT: System Resources Critical on $(hostname)"
    MESSAGE=$1
    
    if command_exists mail; then
        echo -e "$MESSAGE" | mail -s "$SUBJECT" "$EMAIL"
        log "Alert email sent to $EMAIL"
    else
        log "Warning: 'mail' command not available, can't send email alert"
    fi
}

# Generate daily report
generate_daily_report() {
    {
        echo "========================================"
        echo "System Performance Report - $(date '+%Y-%m-%d')"
        echo "========================================"
        echo "Hostname: $(hostname)"
        echo "Kernel: $(uname -r)"
        echo "Uptime: $(uptime)"
        
        echo -e "\n----- CPU Statistics -----"
        if command_exists sar; then
            sar | grep -v -e "^$" -e "Average" | tail -n 12
        else
            mpstat | grep -A 2 "%usr"
        fi
        
        echo -e "\n----- Memory Statistics -----"
        free -h
        
        echo -e "\n----- Disk Usage -----"
        df -h | grep -vE "tmpfs|devtmpfs"
        
        echo -e "\n----- Network Statistics -----"
        if command_exists sar; then
            sar -n DEV | grep -v -e "^$" -e "Average" | head -n 12
        else
            netstat -i | head -n 7
        fi
        
        echo -e "\n----- Top Processes -----"
        ps aux --sort=-%cpu | head -n 10
        
        echo -e "\n----- Recent Alerts -----"
        grep "ALERT" "$LOG_FILE" | tail -n 10
        
    } > "$DAILY_REPORT"
    
    log "Daily report generated: $DAILY_REPORT"
    
    # Optionally email the report
    if command_exists mail; then
        cat "$DAILY_REPORT" | mail -s "Daily System Report - $(hostname)" "$EMAIL"
    fi
}

# Main monitoring loop
monitor_system() {
    log "Starting system monitoring (checking every $WATCH_INTERVAL seconds)"
    
    while true; do
        CPU_USAGE=$(get_cpu_usage)
        MEM_USAGE=$(get_mem_usage)
        check_disk_usage
        DISK_FULL=$?
        
        # Log current status
        log "Status - CPU: ${CPU_USAGE}%, Memory: ${MEM_USAGE}%"
        
        # Check for threshold violations
        ALERT=0
        ALERT_MESSAGE="System Alert on $(hostname) - $(date)\n\n"
        
        if [ "$(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc)" -eq 1 ]; then
            log "ALERT: CPU usage is critical: $CPU_USAGE%"
            ALERT=1
            ALERT_MESSAGE+="CPU usage is critical: $CPU_USAGE%\n"
        fi
        
        if [ "$(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc)" -eq 1 ]; then
            log "ALERT: Memory usage is critical: $MEM_USAGE%"
            ALERT=1
            ALERT_MESSAGE+="Memory usage is critical: $MEM_USAGE%\n"
        fi
        
        if [ "$DISK_FULL" -eq 1 ]; then
            ALERT=1
            ALERT_MESSAGE+="Disk usage exceeds threshold on one or more partitions\n"
        fi
        
        # Send alert if thresholds exceeded
        if [ "$ALERT" -eq 1 ]; then
            ALERT_MESSAGE+="\n----- Top Resource Consumers -----\n"
            ALERT_MESSAGE+="$(get_top_consumers)\n\n"
            ALERT_MESSAGE+="$(generate_suggestions "$CPU_USAGE" "$MEM_USAGE" "$DISK_FULL")"
            send_alert "$ALERT_MESSAGE"
        fi
        
        # Generate daily report at midnight
        CURRENT_HOUR=$(date +%H)
        CURRENT_MIN=$(date +%M)
        if [ "$CURRENT_HOUR" -eq 0 ] && [ "$CURRENT_MIN" -eq 0 ]; then
            generate_daily_report
        fi
        
        sleep "$WATCH_INTERVAL"
    done
}

# Main execution
check_deps
monitor_system
```

## Cleanup

```bash
# 1. Stop stress tests
pkill stress
pkill stress-ng

# 2. Remove temporary files
rm -f /tmp/largefile
rm -f /tmp/memory_alerts.log
rm -f /tmp/disk_space_report.txt
rm -f /tmp/network_monitor.log

# 3. Optionally uninstall packages
# sudo apt remove stress stress-ng iotop htop nethogs iftop
# sudo yum remove stress stress-ng iotop htop nethogs iftop

# 4. Remove scripts
rm -f memory_alert.sh
rm -f disk_space_report.sh
rm -f network_monitor.sh
rm -f performance_dashboard.sh
rm -f system_monitor.sh
``` 