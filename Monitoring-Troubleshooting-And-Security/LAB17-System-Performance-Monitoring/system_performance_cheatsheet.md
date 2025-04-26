# LAB17 - System Performance Monitoring Cheatsheet

This cheatsheet provides a quick reference for monitoring system performance in Linux.

## Process and CPU Monitoring

### top Command

| Key | Action | Description |
|-----|--------|-------------|
| `top` | Launch top | Show real-time system statistics and process list |
| `q` | Quit | Exit top |
| `h` | Help | Display help screen |
| `k` | Kill | Kill a process (prompts for PID) |
| `r` | Renice | Change process priority (prompts for PID) |
| `f` | Fields | Select fields to display |
| `F` | Sort | Sort by different columns |
| `o` | Filter | Filter processes by specific criteria |
| `u` | User filter | Show processes of a specific user |
| `M` | Sort by memory | Sort processes by memory usage |
| `P` | Sort by CPU | Sort processes by CPU usage (default) |
| `T` | Sort by time | Sort processes by running time |
| `1` | CPU cores | Toggle display of individual CPU cores |
| `c` | Command | Toggle between command name and full command line |
| `V` | Forest view | Show processes in a tree format |
| `d` | Refresh rate | Change the refresh interval (seconds) |

### htop Command

| Key | Action | Description |
|-----|--------|-------------|
| `htop` | Launch htop | Enhanced interactive process viewer |
| `F1-F10` | Menu options | Various functions as shown at bottom of screen |
| `F2` | Setup | Configure htop settings |
| `F3` | Search | Search for a process |
| `F4` | Filter | Filter processes by keyword |
| `F5` | Tree view | Toggle tree view of processes |
| `F6` | Sort | Sort by column |
| `F7/F8` | Nice | Decrease/increase process priority |
| `F9` | Kill | Kill a process |
| `F10` | Quit | Exit htop |
| `u` | Filter user | Show only processes of a specific user |
| `Space` | Select | Tag a process (for group operations) |
| `h` | Help | Show help |

### ps Command

| Command | Description | Example |
|---------|-------------|---------|
| `ps` | List user's processes | `ps` |
| `ps aux` | List all processes with details | `ps aux` |
| `ps -ef` | Unix-style process listing | `ps -ef` |
| `ps axjf` | Display process tree | `ps axjf` |
| `ps -p <PID>` | Info for specific PID | `ps -p 1234` |
| `ps -u <user>` | Processes owned by user | `ps -u john` |
| `ps --sort=-pcpu` | Sort by CPU usage (descending) | `ps aux --sort=-pcpu` |
| `ps --sort=-pmem` | Sort by memory usage (descending) | `ps aux --sort=-pmem` |

### Process Control

| Command | Description | Example |
|---------|-------------|---------|
| `kill <PID>` | Terminate a process | `kill 1234` |
| `kill -9 <PID>` | Force terminate a process | `kill -9 1234` |
| `killall <name>` | Kill processes by name | `killall firefox` |
| `pkill <pattern>` | Kill processes by pattern | `pkill fire` |
| `nice -n <val> <cmd>` | Run command with adjusted priority | `nice -n 10 ./script.sh` |
| `renice <val> -p <PID>` | Change priority of running process | `renice 10 -p 1234` |
| `pgrep <pattern>` | Find PIDs of matching processes | `pgrep firefox` |

## Memory Monitoring

### free Command

| Command | Description | Example |
|---------|-------------|---------|
| `free` | Show memory usage | `free` |
| `free -h` | Show in human-readable format | `free -h` |
| `free -m` | Show in megabytes | `free -m` |
| `free -g` | Show in gigabytes | `free -g` |
| `free -s 5` | Update every 5 seconds | `free -s 5` |
| `free -c 10` | Display 10 times and exit | `free -c 10 -s 1` |

### Memory Information

| Command | Description | Example |
|---------|-------------|---------|
| `cat /proc/meminfo` | Detailed memory info | `cat /proc/meminfo` |
| `vmstat` | Virtual memory statistics | `vmstat` |
| `vmstat 2 5` | Updated every 2s, 5 times | `vmstat 2 5` |

## Disk and I/O Monitoring

### iotop Command

| Key | Action | Description |
|-----|--------|-------------|
| `iotop` | Launch iotop | Monitor disk I/O by process |
| `r` | Reverse sort | Toggle sort order |
| `o` | Only active | Show only processes doing I/O |
| `p` | Process view | Toggle between processes and threads |
| `a` | Accumulated | Show accumulated I/O instead of bandwidth |
| `q` | Quit | Exit iotop |
| `i` | Idle processes | Toggle showing idle processes |

### Disk Usage

| Command | Description | Example |
|---------|-------------|---------|
| `df -h` | Filesystem disk space | `df -h` |
| `df -i` | Inode usage | `df -i` |
| `du -h` | Directory space usage | `du -h /var/log` |
| `du -sh *` | Size of directories in current location | `du -sh *` |
| `du -sh * \| sort -hr` | Sorted sizes (largest first) | `du -sh * \| sort -hr` |
| `ncdu` | Interactive disk usage analyzer | `ncdu /var` |

### Disk I/O Performance

| Command | Description | Example |
|---------|-------------|---------|
| `iostat` | I/O statistics | `iostat` |
| `iostat -x` | Extended statistics | `iostat -x` |
| `iostat -x 2 5` | Update every 2s, 5 times | `iostat -x 2 5` |
| `iostat -p sda` | Stats for specific device | `iostat -p sda` |
| `hdparm -tT /dev/sda` | Disk read performance test | `hdparm -tT /dev/sda` |

## Network Monitoring

### Network Connections

| Command | Description | Example |
|---------|-------------|---------|
| `netstat -tuln` | Show listening ports | `netstat -tuln` |
| `netstat -anp` | All connections with process info | `netstat -anp` |
| `ss -tuln` | Modern alternative to netstat | `ss -tuln` |
| `ss -anp` | All connections with process info | `ss -anp` |
| `lsof -i` | List files opened by network connections | `lsof -i` |
| `lsof -i:80` | What's using port 80 | `lsof -i:80` |

### Network Bandwidth Monitoring

| Command | Description | Example |
|---------|-------------|---------|
| `iftop` | Network bandwidth monitoring by connection | `iftop` |
| `nethogs` | Network bandwidth by process | `nethogs` |
| `iptraf-ng` | Interactive network monitoring | `iptraf-ng` |
| `bmon` | Bandwidth monitor and rate estimator | `bmon` |
| `speedtest-cli` | Test internet bandwidth | `speedtest-cli` |

### Network Testing

| Command | Description | Example |
|---------|-------------|---------|
| `ping <host>` | Test connectivity | `ping google.com` |
| `traceroute <host>` | Trace route to host | `traceroute google.com` |
| `mtr <host>` | Combine ping and traceroute | `mtr google.com` |
| `dig <domain>` | DNS lookup | `dig google.com` |
| `nslookup <domain>` | DNS lookup | `nslookup google.com` |
| `curl -I <url>` | Get HTTP headers | `curl -I https://www.google.com` |

## Overall System Monitoring

### vmstat Command

| Command | Description | Example |
|---------|-------------|---------|
| `vmstat` | Virtual memory statistics | `vmstat` |
| `vmstat 2 5` | Update every 2s, 5 times | `vmstat 2 5` |
| `vmstat -s` | Table of memory stats | `vmstat -s` |
| `vmstat -d` | Disk statistics | `vmstat -d` |
| `vmstat -a` | Active/inactive memory | `vmstat -a` |

### uptime and Load Average

| Command | Description | Example |
|---------|-------------|---------|
| `uptime` | System uptime and load averages | `uptime` |
| `w` | Who is logged in and what they're doing | `w` |

Load average interpretation (for a single CPU system):
- < 1: System not busy
- = 1: System at perfect utilization
- > 1: System overloaded

For multi-core systems, divide by the number of cores to get per-core load.

### System Stress Testing

| Command | Description | Example |
|---------|-------------|---------|
| `stress --cpu 4` | Stress 4 CPU cores | `stress --cpu 4` |
| `stress --vm 2` | Stress virtual memory with 2 workers | `stress --vm 2 --vm-bytes 1G` |
| `stress --io 3` | Stress I/O with 3 workers | `stress --io 3` |
| `stress-ng --cpu 4` | More advanced CPU stress | `stress-ng --cpu 4 --cpu-method all` |
| `stress-ng --vm 2` | More advanced memory stress | `stress-ng --vm 2 --vm-bytes 1G` |

## Data Collection and Reporting

### sar (System Activity Reporter)

| Command | Description | Example |
|---------|-------------|---------|
| `sar` | Display today's CPU activity | `sar` |
| `sar -r` | Memory usage | `sar -r` |
| `sar -b` | I/O and transfer rate statistics | `sar -b` |
| `sar -n DEV` | Network statistics | `sar -n DEV` |
| `sar -f /var/log/sa/sa01` | View specific logfile | `sar -f /var/log/sa/sa01` |
| `sar -A` | All statistics | `sar -A` |
| `sar 2 5` | Every 2 seconds for 5 times | `sar 2 5` |
| `sar -o output.file 1 10` | Save to a file | `sar -o output.file 1 10` |

### Setting up sysstat

```bash
# Install sysstat
sudo apt install sysstat    # Debian/Ubuntu
sudo yum install sysstat    # CentOS/RHEL

# Enable data collection
sudo systemctl enable sysstat
sudo systemctl start sysstat

# Edit collection interval (10 min default)
sudo vi /etc/cron.d/sysstat
```

## Useful Scripts and One-liners

### CPU Usage by Process

```bash
ps aux | sort -nrk 3,3 | head -n 10
```

### Memory Usage by Process

```bash
ps aux | sort -nrk 4,4 | head -n 10
```

### Find Top 5 Directories by Size

```bash
du -h /path/to/dir | sort -hr | head -n 5
```

### Monitor Memory and CPU every 2 seconds

```bash
watch -n 2 'free -m; echo ""; ps aux --sort=-%mem | head -n 6'
```

### Simple Memory Alert Script

```bash
#!/bin/bash
THRESHOLD=20
FREE_MEM=$(free | grep Mem | awk '{print $4/$2 * 100.0}')

if (( $(echo "$FREE_MEM < $THRESHOLD" | bc -l) )); then
    echo "WARNING: Free memory is low: $FREE_MEM%"
    echo "Top memory processes:"
    ps aux --sort=-%mem | head -n 5
fi
```

### Network Connectivity Monitor

```bash
#!/bin/bash
HOST="google.com"
LOG_FILE="/var/log/network_monitor.log"

while true; do
    if ping -c 1 $HOST &> /dev/null; then
        STATUS="UP"
    else
        STATUS="DOWN"
        echo "$(date): Network connection to $HOST is DOWN" >> $LOG_FILE
    fi
    echo "$(date): Network status: $STATUS"
    sleep 60
done
```

### Disk Space Alert

```bash
#!/bin/bash
THRESHOLD=90
for fs in $(df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }'); do
    USAGE=$(echo $fs | awk '{ print $1 }' | cut -d'%' -f1)
    PARTITION=$(echo $fs | awk '{ print $2 }')
    
    if [ $USAGE -ge $THRESHOLD ]; then
        echo "WARNING: Partition $PARTITION is ${USAGE}% full!"
    fi
done
```

## Performance Tuning

### Process and System Limits

| Command | Description | Example |
|---------|-------------|---------|
| `ulimit -a` | Show all limits | `ulimit -a` |
| `ulimit -n 4096` | Set open files limit | `ulimit -n 4096` |
| `cat /proc/sys/vm/swappiness` | Check swappiness value | `cat /proc/sys/vm/swappiness` |
| `sysctl vm.swappiness=10` | Set swappiness temporarily | `sysctl vm.swappiness=10` |
| `sysctl -a` | Show all kernel parameters | `sysctl -a` |

### I/O Scheduling

| Command | Description | Example |
|---------|-------------|---------|
| `cat /sys/block/sda/queue/scheduler` | Show active scheduler | `cat /sys/block/sda/queue/scheduler` |
| `echo deadline > /sys/block/sda/queue/scheduler` | Change scheduler | `echo deadline > /sys/block/sda/queue/scheduler` |

## Performance Bottleneck Reference

| Subsystem | Key Indicators | Possible Solutions |
|-----------|---------------|-------------------|
| **CPU** | High load average, high %usr or %sys in top | Add CPU cores, optimize application, use nice for less important processes |
| **Memory** | High %used memory, high swap usage, low cache/buffers | Add RAM, find memory leaks, optimize application memory usage |
| **Disk I/O** | High iowait, high disk utilization in iostat | Use faster disks (SSD), optimize application I/O, use appropriate I/O scheduler |
| **Network** | High network utilization, increased latency | Increase bandwidth, check for network bottlenecks, optimize application network usage |
| **Application** | High specific process CPU/memory usage | Profile and optimize code, check for memory leaks, optimize database queries |

## Understanding Key Metrics

### CPU Metrics (from top/vmstat)

| Metric | Description |
|--------|-------------|
| `us` | User CPU time (applications) |
| `sy` | System CPU time (kernel operations) |
| `id` | Idle CPU time |
| `wa` | I/O wait CPU time (waiting for disk) |
| `st` | Stolen time (in virtualized environments) |

### Memory Metrics (from free)

| Metric | Description |
|--------|-------------|
| `total` | Total installed memory |
| `used` | Used memory |
| `free` | Completely free memory |
| `shared` | Shared memory |
| `buff/cache` | Memory used by kernel buffers/cache |
| `available` | Memory available for applications |

### Disk I/O Metrics (from iostat)

| Metric | Description |
|--------|-------------|
| `tps` | Transfers per second |
| `kB_read/s` | Kilobytes read per second |
| `kB_wrtn/s` | Kilobytes written per second |
| `await` | Average time for I/O requests (ms) |
| `%util` | Percentage of CPU time device was busy | 