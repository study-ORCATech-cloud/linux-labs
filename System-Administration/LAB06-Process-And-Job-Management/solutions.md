# LAB06 - Process and Job Management Solutions

Below are the solutions to the process and job management exercises. Remember to try solving them on your own first!

## Exercise 1: Viewing Processes

### Solution:
1. Display all processes:
   ```bash
   ps aux
   ```

2. Display specific process information:
   ```bash
   ps -eo pid,user,%cpu,%mem,cmd
   ```

3. View real-time process statistics:
   ```bash
   top
   # Press 'q' to exit
   ```

4. Install and use htop:
   ```bash
   # On Debian/Ubuntu
   sudo apt install htop
   # On RHEL/CentOS
   sudo yum install htop
   
   # Run htop
   htop
   # Press 'q' to exit
   ```

5. Find processes owned by your user:
   ```bash
   ps -u $(whoami)
   # Or
   ps aux | grep ^$(whoami)
   ```

6. Find processes using more than 0.1% CPU:
   ```bash
   ps aux | awk '$3 > 0.1 {print $0}'
   ```

## Exercise 2: Process Information and Stats

### Solution:
1. Find the process using the most memory:
   ```bash
   ps aux --sort=-%mem | head -n 2
   # Note: The first line is the header, so we use head -n 2
   ```

2. Find the process using the most CPU:
   ```bash
   ps aux --sort=-%cpu | head -n 2
   ```

3. Check system uptime:
   ```bash
   uptime
   ```

4. Find process ID with pgrep:
   ```bash
   pgrep bash
   ```

5. View process tree:
   ```bash
   ps -aef --forest
   # Or if available
   pstree
   ```

6. Create a file with processes sorted by memory usage:
   ```bash
   ps aux --sort=-%mem > processes_by_memory.txt
   ```

## Exercise 3: Background Jobs

### Solution:
1. Start a sleep command in the background:
   ```bash
   sleep 300 &
   ```

2. Verify the background job:
   ```bash
   jobs
   ```

3. Start another sleep command:
   ```bash
   sleep 600 &
   ```

4. List background jobs:
   ```bash
   jobs -l  # The -l flag lists PIDs as well
   ```

5. Bring a job to the foreground:
   ```bash
   fg %1  # The %1 refers to job number 1
   ```

6. Suspend and background a job:
   ```bash
   # Press Ctrl+Z to suspend the current foreground job
   bg %1  # Put job 1 in the background
   ```

7. Kill a background job:
   ```bash
   kill %2  # Kill job number 2
   ```

## Exercise 4: Managing Processes

### Solution:
1. Start a continuous process:
   ```bash
   yes > /dev/null &
   ```

2. Find its PID:
   ```bash
   jobs -l
   # Or
   pgrep yes
   ```

3. Terminate the process:
   ```bash
   kill <PID>
   ```

4. Using killall:
   ```bash
   yes > /dev/null &
   killall yes
   ```

5. Force kill with signal 9:
   ```bash
   yes > /dev/null &
   kill -9 <PID>
   ```

6. Using pkill:
   ```bash
   yes > /dev/null &
   pkill yes
   ```

## Exercise 5: Process Priorities

### Solution:
1. Start a process with lower priority:
   ```bash
   nice -n 10 yes > /dev/null &
   ```

2. Check the niceness value:
   ```bash
   ps -o pid,nice,cmd -p <PID>
   ```

3. Change the priority:
   ```bash
   sudo renice -n 15 -p <PID>
   ```

4. Start multiple processes with different priorities:
   ```bash
   nice -n 5 yes > /dev/null &
   nice -n 10 yes > /dev/null &
   nice -n 15 yes > /dev/null &
   ```

5. Observe CPU usage:
   ```bash
   top
   # Or
   htop
   ```

## Exercise 6: System Monitoring

### Solution:
1. Use vmstat:
   ```bash
   vmstat 1 5  # 5 reports, 1 second apart
   ```

2. Use iostat (install if needed):
   ```bash
   # Install on Debian/Ubuntu
   sudo apt install sysstat
   # Install on RHEL/CentOS
   sudo yum install sysstat
   
   # Run iostat
   iostat
   ```

3. Check memory usage:
   ```bash
   free -h
   ```

4. Check load average:
   ```bash
   uptime
   # Or 
   cat /proc/loadavg
   ```

5. Check I/O usage:
   ```bash
   # Install iotop on Debian/Ubuntu
   sudo apt install iotop
   # Install on RHEL/CentOS
   sudo yum install iotop
   
   # Run iotop
   sudo iotop
   ```

6. List open files:
   ```bash
   lsof -p <PID>
   ```

## Exercise 7: Process Limits and Control

### Solution:
1. Check process limits:
   ```bash
   ulimit -a
   ```

2. Create the signal handling script:
   ```bash
   cat > signal_test.sh << 'EOF'
   #!/bin/bash
   echo "PID: $$"
   trap 'echo "Received SIGTERM, cleaning up..."; exit' TERM
   echo "Running... Press Ctrl+C to stop"
   while true; do
     sleep 1
   done
   EOF
   
   chmod +x signal_test.sh
   ```

3. Run and send SIGTERM:
   ```bash
   ./signal_test.sh &
   # Note the PID from the output
   kill <PID>
   ```

4. Modify script to ignore SIGTERM:
   ```bash
   cat > signal_ignore.sh << 'EOF'
   #!/bin/bash
   echo "PID: $$"
   trap '' TERM
   echo "Running... Ignoring SIGTERM. Use SIGKILL (kill -9) to terminate"
   while true; do
     sleep 1
   done
   EOF
   
   chmod +x signal_ignore.sh
   ./signal_ignore.sh &
   # Try to terminate
   kill <PID>
   # It won't terminate, so force it
   kill -9 <PID>
   ```

5. Use the timeout command:
   ```bash
   timeout 10s ./signal_test.sh
   ```

## Bonus Challenge Solution:

```bash
#!/bin/bash

# Script to monitor system and process information
# Usage: ./monitor.sh [username]

# Check if a username is provided
USER_FILTER=${1:-$(whoami)}

# Function to clear screen and show header
show_header() {
    clear
    echo "==========================="
    echo "System Monitor - $(date)"
    echo "==========================="
    echo ""
}

# Function to show top CPU processes
show_top_cpu() {
    echo "Top 5 processes by CPU usage:"
    ps aux --sort=-%cpu | head -n 6
    echo ""
}

# Function to show top memory processes
show_top_memory() {
    echo "Top 5 processes by memory usage:"
    ps aux --sort=-%mem | head -n 6
    echo ""
}

# Function to show system load and memory
show_system_stats() {
    echo "System load (1, 5, 15 min averages):"
    uptime
    echo ""
    
    echo "Memory usage:"
    free -h
    echo ""
}

# Function to show user processes
show_user_processes() {
    echo "Processes for user: $USER_FILTER"
    ps -u "$USER_FILTER"
    echo ""
}

# Main loop
trap 'echo "Monitor terminated."; exit 0' INT
while true; do
    show_header
    show_top_cpu
    show_top_memory
    show_system_stats
    show_user_processes
    
    echo "Refreshing in 5 seconds... Press Ctrl+C to quit."
    sleep 5
done
```

To use the script:
```bash
chmod +x monitor.sh
./monitor.sh
# Or specify a username
./monitor.sh root
``` 