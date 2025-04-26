# LAB06 - Process and Job Management Exercises

These exercises will help you practice viewing, managing, and controlling processes in Linux. Complete each task to build essential system administration skills.

## Exercise 1: Viewing Processes

### TODO:
1. Display all processes running on the system.

2. Display a customized process list showing only the process ID, user, CPU usage, memory usage, and command.

3. View real-time process statistics.

4. If available, install and use a more user-friendly process viewer.

5. Find all processes owned by your user.

6. Find all processes using more than 0.1% CPU.

## Exercise 2: Process Information and Stats

### TODO:
1. Determine which process is using the most memory on your system.

2. Determine which process is using the most CPU on your system.

3. Find how long the system has been running.

4. Find the process ID of a specific process (e.g., bash).

5. List all processes in a tree view showing the parent-child relationships.

6. Create a file that contains a list of all running processes sorted by memory usage.

## Exercise 3: Background Jobs

### TODO:
1. Start a sleep command that runs for 300 seconds in the background.

2. Verify that the sleep process is running in the background.

3. Start another sleep command that runs for 600 seconds in the background.

4. List all your background jobs with their job numbers.

5. Bring the first sleep job to the foreground.

6. Suspend the job, then put it back in the background.

7. Kill the second sleep job using its job number.

## Exercise 4: Managing Processes

### TODO:
1. Start a process that continuously outputs text to the terminal in the background.

2. Find the process ID (PID) of this process.

3. Terminate the process using the kill command.

4. Start another similar process and kill it using an alternative method.

5. Start a third similar process and force kill it.

6. Kill a process by name instead of by PID.

## Exercise 5: Process Priorities

### TODO:
1. Start a process with a lower priority.

2. Check the priority (niceness) value of this process.

3. Change the priority of the running process.

4. Start multiple processes with different priority levels.

5. Observe how CPU usage changes based on priority.

## Exercise 6: System Monitoring

### TODO:
1. Get a snapshot of system statistics.

2. View I/O statistics.

3. Check memory usage.

4. Check system load average for the past 1, 5, and 15 minutes.

5. Find the process with the highest I/O usage.

6. List all open files by a specific process.

## Exercise 7: Process Limits and Control

### TODO:
1. Check the current limits for your processes.

2. Create a simple script that handles the SIGTERM signal gracefully.

3. Run the script, find its PID, then send it a SIGTERM signal.

4. Modify the script to ignore the SIGTERM signal and test it.

5. Use the timeout command to run a command that automatically terminates after a specific time.

## Bonus Challenge:
Create a shell script called `monitor.sh` that:
1. Shows the top 5 processes by CPU usage
2. Shows the top 5 processes by memory usage
3. Shows the system load and memory usage
4. Displays all processes belonging to a specified user (passed as an argument)
5. Refreshes the information every 5 seconds until terminated with Ctrl+C 