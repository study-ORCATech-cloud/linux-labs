# LAB18 - Troubleshooting Common Issues - Exercises

This lab will help you develop practical troubleshooting skills for common Linux system issues. Each exercise presents a realistic scenario you might encounter in a production environment. Work through these exercises methodically, documenting your approach and commands.

## Exercise 1: Storage Issues Troubleshooting

### Scenario
You receive an alert that one of your Linux servers is running low on disk space. You need to investigate and resolve the issue.

### Tasks
1. Check the current disk usage on all filesystems to identify which one is running low on space.
2. Find the largest directories in the `/var` directory to narrow down the issue.
3. Look for files larger than 100MB that might be consuming excessive space.
4. Find files that have been created or modified in the last 24 hours in `/var/log`.
5. Check if there are deleted files still being held open by running processes.
6. Create a 100MB test file in `/tmp`, verify the space is used, then delete it and verify the space is reclaimed.

### TODO
- Document the commands you would use for each task
- Explain what output you would expect to see and how you would interpret it
- Describe the actions you would take to resolve the issue based on your findings

## Exercise 2: Memory Issues Troubleshooting

### Scenario
A web application is experiencing performance degradation. You suspect memory-related issues.

### Tasks
1. Check the system's memory usage, including swap space.
2. Identify the processes consuming the most memory.
3. Monitor memory usage in real-time for 5 minutes to detect any patterns or spikes.
4. Create a simple bash script called `memory_report.sh` that generates a memory usage report including:
   - Overall system memory statistics
   - Top 5 memory-consuming processes
   - Memory statistics from `vmstat`
   - Swap space usage

### TODO
- Document the commands for each task
- Create the `memory_report.sh` script
- Analyze the memory usage data and recommend actions to address issues
- Explain what would constitute a memory problem versus normal usage

## Exercise 3: Service Troubleshooting

### Scenario
A critical service on your system has stopped responding to requests. You need to diagnose and fix the issue.

### Tasks
1. Check the status of the SSH service (or another service of your choice).
2. View the logs for the service to identify any errors or warnings.
3. Filter the service logs to show only error messages.
4. List all failed services on the system.
5. Create a test service that will intentionally fail, then diagnose why it failed.

### TODO
- Document the commands used for each task
- Create a simple service file that will fail in a predictable way
- Demonstrate how to diagnose the failure using system tools
- Document the steps to fix the service issue

## Exercise 4: CPU and Process Issues

### Scenario
Users are reporting that the system is slow to respond. You need to investigate possible CPU or process issues.

### Tasks
1. Check the system's load averages to determine if the CPU is overloaded.
2. Identify which processes are consuming the most CPU.
3. Create a script called `cpu_load.sh` that will:
   - Generate CPU load by running multiple intensive processes
   - Show how to monitor these processes
   - Demonstrate how to stop them
4. Experiment with process priority using `nice` and `renice`.

### TODO
- Document the commands for checking CPU usage and load
- Create the `cpu_load.sh` script
- Demonstrate how to manage process priorities effectively
- Explain how you would determine if CPU usage is problematic

## Exercise 5: Permission Problems

### Scenario
An application is failing to access certain files. You suspect permission issues might be the cause.

### Tasks
1. Create a directory structure with various permission settings and trace the permissions through the path.
2. Set up a scenario where a file cannot be accessed due to permission issues.
3. Diagnose the permission problem and fix it.
4. Experiment with special permissions (setuid, setgid, sticky bit) and observe their effects.

### TODO
- Document each permission-related command used
- Explain how permissions are applied through a directory tree
- Demonstrate how to diagnose permission issues methodically
- Show how to fix permission problems correctly

## Exercise 6: Network Troubleshooting

### Scenario
A server is having difficulty connecting to external services. You need to diagnose network issues.

### Tasks
1. Check the network interfaces and their configuration.
2. Test connectivity to external destinations (e.g., google.com, 8.8.8.8).
3. Examine routing table and DNS configuration.
4. Check for listening services and open ports on the local system.
5. Diagnose network performance issues using appropriate tools.

### TODO
- Document network diagnostic commands and their output
- Explain how to interpret the results
- Demonstrate a methodical approach to network troubleshooting
- Provide solutions for common network issues

## Exercise 7: Log Analysis

### Scenario
You need to investigate a system issue that occurred overnight. The logs are the only source of information about what happened.

### Tasks
1. Examine system logs to find error messages from the last 24 hours.
2. Filter logs to find specific types of events (e.g., authentication failures).
3. Use text processing tools (grep, awk, sed) to extract relevant information from logs.
4. Set up real-time log monitoring to watch for specific events.
5. Create a log analysis script called `log_analyzer.sh` that extracts statistics about errors in system logs.

### TODO
- Document log analysis commands and techniques
- Create the `log_analyzer.sh` script
- Demonstrate effective ways to find relevant information in large log files
- Explain how to set up alerts for critical log events

## Bonus Challenge: Comprehensive System Diagnostic

### Scenario
You've been called to troubleshoot a system with unknown issues. You need to create a comprehensive diagnostic report.

### Tasks
Create a bash script called `system_diagnostic.sh` that:

1. Collects system information (hostname, uptime, kernel details)
2. Gathers resource usage statistics (CPU, memory, disk)
3. Lists the top processes by CPU and memory usage
4. Checks service status, particularly failed services
5. Examines network configuration and connectivity
6. Extracts relevant log entries, focusing on errors
7. Checks security information (recent logins, failed logins)
8. Generates a summary report and creates an archive of all collected data

### TODO
- Design and implement the `system_diagnostic.sh` script
- Ensure the script is efficient and doesn't impact system performance
- Organize the output in a way that makes it easy to analyze
- Include error handling in your script

## Cleanup

After completing the exercises, make sure to:

1. Remove any test files you created
2. Stop and remove any test services
3. Clean up any test directories and configurations
4. Remove any temporary files or logs generated during the exercises

Document the cleanup commands you used to restore the system to its original state. 