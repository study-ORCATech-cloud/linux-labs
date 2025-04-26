# Linux Troubleshooting Cheatsheet

This cheatsheet provides essential commands and techniques for troubleshooting common Linux issues. Use it as a quick reference when diagnosing problems in your system.

## Storage and Disk Issues

| Command | Description |
|---------|-------------|
| `df -h` | Shows disk space usage for all mounted filesystems in human-readable format |
| `du -h --max-depth=1 /path` | Shows the size of immediate subdirectories in the specified path |
| `du -sh /path` | Shows the total size of a directory and all its contents |
| `ls -la /path` | Lists all files including hidden ones with detailed information |
| `find /path -type f -size +100M` | Finds files larger than 100MB in the specified path |
| `find /path -mtime -1` | Finds files modified in the last 24 hours |
| `find /path -atime -7` | Finds files accessed in the last 7 days |
| `lsof +L1` | Lists open files that have been deleted but are still held open by processes |
| `lsof /path` | Lists processes that have open files in the specified path |
| `ncdu /path` | Interactive disk usage analyzer (may need to be installed) |
| `dd if=/dev/zero of=/tmp/testfile bs=1M count=100` | Creates a 100MB test file |

## Memory Issues

| Command | Description |
|---------|-------------|
| `free -h` | Shows memory and swap usage in human-readable format |
| `vmstat 1 10` | Shows virtual memory statistics, updating every 1 second for 10 samples |
| `ps aux --sort=-%mem` | Lists processes sorted by memory usage (highest first) |
| `ps aux --sort=-%mem \| head -10` | Shows the top 10 memory-consuming processes |
| `top -o %MEM` | Interactive process viewer sorted by memory usage |
| `watch -n 1 'free -m'` | Monitors memory usage in real-time, updating every second |
| `cat /proc/meminfo` | Detailed memory information from the kernel |
| `dmesg \| grep -i 'out of memory'` | Checks for OOM (Out Of Memory) killer messages |
| `journalctl \| grep -i 'oom'` | Searches system logs for OOM events |
| `slabtop` | Displays kernel slab cache information in real-time |
| `echo 1 > /proc/sys/vm/drop_caches` | Clears page cache (requires root, use cautiously) |

## Service Troubleshooting

| Command | Description |
|---------|-------------|
| `systemctl status service_name` | Shows the status of a specific service |
| `systemctl list-units --state=failed` | Lists all failed systemd units |
| `journalctl -u service_name` | Shows logs for a specific service |
| `journalctl -u service_name -p err` | Shows only error messages for a service |
| `systemctl restart service_name` | Restarts a service |
| `systemctl cat service_name` | Displays the service unit file |
| `ps -ef \| grep service_name` | Finds processes related to a service |
| `kill -0 PID` | Checks if a process is running without sending a signal |
| `strace -p PID` | Traces system calls and signals of a running process |
| `ltrace -p PID` | Traces library calls of a running process |

## CPU and Process Issues

| Command | Description |
|---------|-------------|
| `uptime` | Shows load averages for the last 1, 5, and 15 minutes |
| `top` | Interactive process viewer showing CPU, memory, and other resource usage |
| `htop` | Enhanced interactive process viewer (may need to be installed) |
| `ps aux --sort=-%cpu` | Lists processes sorted by CPU usage (highest first) |
| `ps aux --sort=-%cpu \| head -10` | Shows the top 10 CPU-consuming processes |
| `pidstat 1` | Reports statistics for Linux tasks (processes) updated every second |
| `mpstat -P ALL 1` | Reports CPU usage per processor updated every second |
| `nice -n 19 command` | Runs a command with lower priority (nice value 19 is lowest) |
| `renice -n 10 -p PID` | Changes the priority of a running process |
| `kill PID` | Sends SIGTERM signal to terminate a process |
| `kill -9 PID` | Sends SIGKILL signal to forcefully kill a process |
| `pgrep process_name` | Finds PIDs of a process by name |
| `pkill process_name` | Kills processes by name |

## Permission Issues

| Command | Description |
|---------|-------------|
| `ls -la /path` | Shows detailed file information including permissions |
| `stat file` | Displays detailed file status including permissions and timestamps |
| `namei -l /path/to/file` | Shows the permissions of each component in a path |
| `getcap file` | Shows capabilities set on a file |
| `getfacl file` | Shows Access Control List settings for a file |
| `chmod permissions file` | Changes file permissions (e.g., `chmod 755 file`) |
| `chown user:group file` | Changes file ownership |
| `id user` | Shows user ID, group ID, and groups for a user |
| `groups user` | Lists groups a user belongs to |
| `sudo -l` | Lists commands the current user can run with sudo |
| `find /path -type f -perm 777` | Finds files with specific permissions (777 in this case) |

## Network Issues

| Command | Description |
|---------|-------------|
| `ip addr show` | Shows network interface information |
| `ip route show` | Shows routing table |
| `ping -c 4 destination` | Tests connectivity to a destination with 4 packets |
| `traceroute destination` | Shows the network path to a destination |
| `mtr destination` | Combines ping and traceroute for continuous monitoring |
| `ss -tuln` | Lists listening ports (TCP, UDP, listening, numeric) |
| `netstat -tuln` | Alternative for listing listening ports |
| `nslookup domain` | Performs DNS lookup for a domain |
| `dig domain` | More detailed DNS lookup tool |
| `host domain` | Simple DNS lookup tool |
| `curl -I https://website.com` | Shows HTTP headers from a website |
| `wget -q -O- https://website.com` | Downloads and displays website content |
| `iptables -L` | Lists firewall rules (requires root) |
| `tcpdump -i eth0` | Captures and displays packets on a network interface (requires root) |

## Log Analysis

| Command | Description |
|---------|-------------|
| `journalctl` | Shows all system logs when using systemd |
| `journalctl -b` | Shows logs from the current boot |
| `journalctl -p err` | Shows only error-level messages |
| `journalctl --since "1 hour ago"` | Shows logs from the last hour |
| `journalctl -f` | Shows logs in real-time (follow mode) |
| `tail -f /var/log/syslog` | Shows the last entries in syslog file in real-time |
| `grep "error" /var/log/file` | Searches for "error" in a log file |
| `grep -i "failed" /var/log/auth.log` | Case-insensitive search for "failed" in auth log |
| `zgrep "error" /var/log/file.gz` | Searches in compressed log files |
| `awk '/pattern/ {print $5}' /var/log/file` | Extracts specific fields from logs matching a pattern |
| `sed -n '/May 1/,/May 10/p' /var/log/file` | Extracts logs between two date patterns |

## Comprehensive System Analysis

| Command | Description |
|---------|-------------|
| `uname -a` | Shows system information including kernel version |
| `hostnamectl` | Displays system hostname and OS information |
| `lscpu` | Displays CPU information |
| `lsmem` | Shows memory ranges and their online status |
| `lsblk` | Lists block devices |
| `lspci` | Lists PCI devices |
| `lsusb` | Lists USB devices |
| `dmesg` | Shows kernel ring buffer messages |
| `dmesg -T` | Shows kernel messages with human-readable timestamps |
| `cat /proc/interrupts` | Shows information about IRQs |
| `cat /proc/cpuinfo` | Shows detailed CPU information |
| `w` | Shows who is logged in and what they're doing |
| `last` | Shows listing of last logged in users |
| `lastb` | Shows listing of bad login attempts |
| `who` | Shows who is logged in |

## Process and System Control

| Command | Description |
|---------|-------------|
| `systemctl list-dependencies service_name` | Shows service dependencies |
| `systemctl list-units --type=service` | Lists all services |
| `systemd-analyze` | Shows system boot time |
| `systemd-analyze blame` | Shows which services took the most time to start |
| `systemd-analyze critical-chain` | Shows critical chain of boot sequence |
| `initctl list` | Lists services managed by Upstart (on older systems) |
| `service --status-all` | Lists status of all services (on older systems) |
| `chkconfig --list` | Lists services and their runlevels (on older systems) |
| `sysctl -a` | Shows all kernel parameters |

## Troubleshooting Methodology

1. **Identify the problem**
   - Define what's wrong: error messages, unexpected behavior, performance issues
   - Determine when the problem started
   - Note any recent changes to the system

2. **Gather information**
   - Check system logs
   - Examine resource usage (CPU, memory, disk, network)
   - Check service status
   - Look for error messages

3. **Analyze the data**
   - Look for patterns or correlations
   - Identify potential causes
   - Narrow down the problem area

4. **Plan a solution**
   - Determine what needs to be fixed
   - Consider potential impacts of your solution
   - Create a rollback plan if needed

5. **Implement and test**
   - Apply your solution
   - Verify that the problem is resolved
   - Ensure no new issues were introduced

6. **Document**
   - Record what was done
   - Note the root cause
   - Document the solution for future reference

## General Troubleshooting Tips

- **One change at a time**: Make one change, then test to see if it resolved the issue
- **Keep notes**: Document what you try and the results
- **Check the basics first**: Often issues are due to simple problems (disk full, service not running)
- **Read error messages carefully**: They often tell you exactly what's wrong
- **Use man pages**: When unsure about a command, read its manual (`man command`)
- **Don't assume**: Verify your assumptions with appropriate commands
- **When stuck, reboot**: For temporary testing, a reboot can confirm if the issue persists
- **Know when to ask for help**: If you're stuck, don't waste too much time before consulting others
- **Search online**: Many problems have been solved by others and documented online
- **Remember security**: Don't disable security features just to make something work 