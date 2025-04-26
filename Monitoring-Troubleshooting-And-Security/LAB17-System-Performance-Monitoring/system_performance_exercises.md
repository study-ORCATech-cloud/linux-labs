# LAB17 - System Performance Monitoring Exercises

These exercises will help you develop skills in monitoring system performance metrics in Linux. Complete each task to strengthen your ability to diagnose and resolve performance issues.

## Exercise 1: Basic System Monitoring

### TODO:
1. Use the `top` command to view current system resource usage.

2. Identify the most CPU-intensive processes currently running on the system.

3. Sort the process list by memory usage instead of CPU.

4. Find and terminate a process using high CPU (you can create one for this exercise).

5. Analyze the system load average and explain what the three values represent.

## Exercise 2: Advanced Process Monitoring with htop

### TODO:
1. Install htop if not already available.

2. Launch htop and observe the more detailed and colorful interface.

3. Sort processes by different metrics (CPU, memory, time).

4. Use filtering to show only processes owned by a specific user.

5. Use htop to change the priority (nice value) of a running process.

## Exercise 3: Memory Analysis

### TODO:
1. Use the `free` command to display memory usage in a human-readable format.

2. Analyze the buffer and cache memory usage and explain their purpose.

3. Observe memory usage over time using the `watch` command combined with `free`.

4. Use `vmstat` to gather statistics about memory, CPU, and I/O.

5. Create a script to alert when free memory falls below 20%.

## Exercise 4: Disk I/O Monitoring

### TODO:
1. Use `iotop` to monitor disk read/write operations by processes (install if needed).

2. Monitor disk I/O performance using the `iostat` command.

3. Create a high disk I/O situation and observe it (e.g., copying large files).

4. Use `df` and `du` to analyze disk space usage and identify large directories.

5. Write a script that reports the top 5 directories consuming disk space.

## Exercise 5: Network Performance Monitoring

### TODO:
1. Use `netstat` or `ss` to list all active network connections.

2. Monitor network traffic in real-time using `iftop` (install if needed).

3. Check bandwidth usage by process using `nethogs` (install if needed).

4. Use `ping` to measure network latency to a remote server.

5. Write a simple script to monitor network connectivity and log any outages.

## Exercise 6: System Load Analysis

### TODO:
1. Use `uptime` to display the current system load.

2. Install and use `stress` or `stress-ng` to create high CPU, memory, and I/O load.

3. Monitor the impact of the stress test using multiple tools (top, htop, vmstat).

4. Identify which subsystem (CPU, memory, I/O, or network) is the bottleneck.

5. Use the `nice` command to run a CPU-intensive process with lower priority.

## Exercise 7: Performance Data Collection and Visualization

### TODO:
1. Install and configure `sysstat` package for collecting performance data.

2. Set up periodic data collection using `sar`.

3. Collect performance metrics for CPU, memory, disk, and network over 1 hour.

4. Generate reports and analyze the collected data.

5. Create a simple script to generate a basic performance dashboard using collected data.

## Bonus Challenge:
Create a comprehensive system monitoring script that:
- Collects key performance metrics (CPU, memory, disk, network)
- Identifies potential bottlenecks automatically
- Suggests possible solutions for performance issues
- Generates alerts when thresholds are exceeded
- Produces a daily report with performance trends

This challenge will test your ability to integrate various monitoring concepts and tools into a unified solution.

## Cleanup:
1. Stop any stress tests or high-load processes you created.
2. Remove any temporary files created during the exercises.
3. Uninstall any packages that were installed purely for these exercises (optional).
4. Remove any scripts created for the exercises (or keep them for future use). 