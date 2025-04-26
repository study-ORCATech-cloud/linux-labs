# LAB18 - Troubleshooting Common Issues - Solutions

This document provides solutions and guidance for the exercises in the Linux Troubleshooting lab.

## Exercise 1: Storage Issues Troubleshooting

### Finding and analyzing storage issues:

```bash
# Check disk usage on all mounted filesystems
df -h

# Find directories consuming the most space
du -sh /* 2>/dev/null | sort -hr | head -10

# Find large files (greater than 100MB)
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5hr

# Find files created or modified in the last 24 hours
find / -type f -mtime -1 -ls 2>/dev/null

# Check for open but deleted files still using space
lsof +L1 | grep -i deleted
```

### Cleaning up storage:

```bash
# Clean up old logs
sudo find /var/log -name "*.gz" -type f -mtime +7 -delete

# Clear journalctl logs
sudo journalctl --vacuum-time=7d

# Clean package cache (for Debian/Ubuntu)
sudo apt clean

# Clean package cache (for RHEL/CentOS)
sudo dnf clean all
```

## Exercise 2: Memory Issues Troubleshooting

### Analyzing memory utilization:

```bash
# Display memory usage
free -h

# Show swap usage
swapon -s

# Display top memory-consuming processes
ps aux --sort=-%mem | head -15

# Check virtual memory statistics
vmstat 1 5

# Look for out-of-memory killer events
dmesg | grep -i "out of memory"

# View detailed memory information
cat /proc/meminfo
```

### Managing memory issues:

```bash
# Clear filesystem cache (as root)
echo 3 > /proc/sys/vm/drop_caches

# Set process priority lower for a memory-intensive process
renice 19 -p PID

# Kill a process that's consuming too much memory
kill -15 PID   # Try SIGTERM first
kill -9 PID    # SIGKILL as last resort
```

## Exercise 3: Service Troubleshooting

### Diagnosing service issues (example for SSH service):

```bash
# Check service status
systemctl status sshd

# View service logs
journalctl -u sshd --since today

# Find errors in service logs
journalctl -u sshd -p err

# Check configuration file syntax
sshd -t   # For SSH

# List all failed services
systemctl list-units --state=failed

# Check service dependencies
systemctl list-dependencies sshd
```

### Fixing service issues:

```bash
# Restart service
systemctl restart sshd

# Check service configuration permissions
ls -la /etc/ssh/sshd_config

# Fix service configuration permissions if needed
chmod 644 /etc/ssh/sshd_config
chown root:root /etc/ssh/sshd_config

# Enable and start service
systemctl enable sshd
systemctl start sshd
```

## Exercise 4: CPU and Process Issues

### Analyzing CPU usage:

```bash
# Show current load average
uptime

# Display CPU-intensive processes
ps aux --sort=-%cpu | head -10

# Monitor system in real-time
top
# Or using htop (if installed)
htop

# Check CPU information
lscpu

# Show running processes as a tree
ps auxf

# Monitor process statistics
pidstat 1 5
```

### Managing processes:

```bash
# Set process priority (nice value)
nice -n 19 ./cpu_intensive_command

# Change priority of running process
renice 19 -p PID

# Stop a process gracefully
kill -15 PID

# Force kill a process
kill -9 PID

# Kill all processes by name
killall processname
```

## Exercise 5: Permission Problems

### Analyzing permission issues:

```bash
# Check file ownership and permissions
ls -la /path/to/file

# Trace permissions along a path
namei -l /path/to/file

# Check current user's sudo privileges
sudo -l

# View user groups
groups username

# Check process privileges
ps aux | grep processname
```

### Fixing permission issues:

```bash
# Change file permissions
chmod 755 /path/to/script.sh  # rwx-r-x-r-x

# Change file ownership
chown user:group /path/to/file

# Add user to a group
usermod -aG groupname username

# Set ACL for specific user
setfacl -m u:username:rw /path/to/file

# View ACLs on a file
getfacl /path/to/file
```

## Exercise 6: Network Troubleshooting

### Diagnosing network issues:

```bash
# Check network interfaces
ip a

# View routing table
ip route

# Test connectivity
ping -c 4 8.8.8.8
ping -c 4 google.com

# Trace network path
traceroute google.com

# DNS lookup
dig google.com
nslookup google.com

# Check listening ports
ss -tuln

# Test TCP connectivity to specific port
nc -zv google.com 443
```

### Analyzing network issues:

```bash
# Find what process is using a port
lsof -i:80

# Check firewall rules
sudo iptables -L

# Monitor network traffic
sudo tcpdump -i eth0 host 192.168.1.1

# View network statistics
netstat -s

# Check DNS servers
cat /etc/resolv.conf
```

## Exercise 7: Log Analysis

### Analyzing system logs:

```bash
# View systemd journal logs
journalctl -xe

# Follow logs in real-time
journalctl -f

# Show recent logs (last hour)
journalctl --since "1 hour ago"

# Show specific service logs
journalctl -u sshd

# View boot logs
journalctl -b

# Check system logs
tail -n 50 /var/log/syslog

# Search for errors in logs
grep -i error /var/log/syslog
```

### Analyzing application logs (example for Apache):

```bash
# View Apache access logs
tail -n 50 /var/log/apache2/access.log

# View Apache error logs
tail -n 50 /var/log/apache2/error.log

# Search for 404 errors
grep -i "404" /var/log/apache2/access.log

# Search for specific IP in logs
grep "192.168.1.10" /var/log/apache2/access.log

# Count occurrences of HTTP status codes
grep -o "HTTP/[0-9.]\+\" [0-9]\+" /var/log/apache2/access.log | sort | uniq -c
```

## Bonus Challenge: Comprehensive Troubleshooting Script

Here's a solution for the bonus challenge - a basic system troubleshooting script:

```bash
#!/bin/bash
# system_troubleshoot.sh - A comprehensive system troubleshooting script

# Set output file
output_file="/tmp/system_diagnostic_$(date +%Y%m%d-%H%M%S).txt"
echo "System Diagnostic Report - $(date)" > $output_file
echo "=================================" >> $output_file

# Function to add section headers
add_section() {
    echo "" >> $output_file
    echo "## $1" >> $output_file
    echo "--------------------------------" >> $output_file
}

# System info
add_section "System Information"
echo "Hostname: $(hostname)" >> $output_file
echo "Kernel: $(uname -r)" >> $output_file
echo "Uptime: $(uptime)" >> $output_file
echo "Last boot: $(who -b)" >> $output_file

# CPU info
add_section "CPU Information"
echo "Load average: $(cat /proc/loadavg)" >> $output_file
echo "Top CPU processes:" >> $output_file
ps aux --sort=-%cpu | head -6 >> $output_file

# Memory info
add_section "Memory Information"
free -h >> $output_file
echo "Top memory processes:" >> $output_file
ps aux --sort=-%mem | head -6 >> $output_file

# Disk info
add_section "Disk Usage"
df -h >> $output_file
echo "Largest directories in /var:" >> $output_file
du -sh /var/* 2>/dev/null | sort -hr | head -5 >> $output_file

# Open but deleted files
add_section "Open but Deleted Files"
lsof +L1 2>/dev/null | head -20 >> $output_file

# Network info
add_section "Network Information"
echo "Network interfaces:" >> $output_file
ip -brief a >> $output_file
echo "Default route:" >> $output_file
ip route show default >> $output_file
echo "Listening services:" >> $output_file
ss -tuln >> $output_file

# Failed services
add_section "Failed Services"
systemctl list-units --state=failed >> $output_file

# Recent errors
add_section "Recent System Errors"
journalctl -p err -n 20 --no-pager >> $output_file

# Last logins
add_section "Recent Logins"
last | head -10 >> $output_file

# Failed logins
add_section "Recent Failed Logins"
lastb | head -10 2>/dev/null >> $output_file

# Finish
echo "" >> $output_file
echo "Report completed at $(date)" >> $output_file
echo "Report saved to $output_file"
```

## Cleanup

To restore the system to its original state:

```bash
# Remove any test files or scripts created
rm -f /tmp/test_large_file.img
rm -f /tmp/system_diagnostic_*.txt
rm -f /home/$USER/test_script.sh

# Stop any resource-intensive processes started during the exercises
pkill -f "stress"
pkill -f "yes"

# Restore permissions if changed
chmod 644 /etc/ssh/sshd_config

# Remove any deliberate errors introduced during exercises
sed -i '/^TEST_ERROR/d' ~/.bashrc

# Clean up logs created during testing
journalctl --vacuum-time=1d
```

> **Note:** These solutions provide a reference for correctly completing the exercises. Always understand the commands before running them, especially those requiring root access. 