# LAB09 - System Startup and Services Exercises

These exercises will help you practice managing system startup processes and services using systemd. Complete each task to build essential service management skills for system administration.

## Exercise 1: Understanding System Boot Process

### TODO:
1. Reboot your system and observe the boot process (if possible).

2. Check the system boot time.

3. View a detailed breakdown of boot time by components.

4. Generate a graphical visualization of the boot sequence (if SVG viewer available).

5. Check the system's current runlevel or target.

6. List the available systemd targets (equivalent to runlevels).

## Exercise 2: Basic Service Management

### TODO:
1. List all active services on your system.

2. Check the status of a specific service (e.g., SSH).

3. Start a service (if it's not running).

4. Stop a running service.

5. Restart a service.

6. Reload a service's configuration without restarting it.

## Exercise 3: Managing Service Boot Behavior

### TODO:
1. Check if a service is set to start at boot.

2. Enable a service to start automatically at boot.

3. Disable a service from starting at boot.

4. Re-enable the service for boot.

5. Mask a service to prevent it from being started.

6. Unmask a service to allow it to be started again.

## Exercise 4: Analyzing Service Logs

### TODO:
1. View the system journal for all logs.

2. View logs for a specific service.

3. View logs since the last boot.

4. Follow logs in real-time.

5. View logs within a specific time range.

6. View logs for a specific priority level (e.g., errors and above).

## Exercise 5: Creating a Simple Service

### TODO:
1. Create a simple shell script that we'll run as a service. The script should:
   - Run in an infinite loop
   - Log a timestamp to a file every minute

2. Create a systemd service file for your script that includes:
   - A description
   - Appropriate dependencies
   - The command to execute
   - Restart behavior
   - User context for running the service

3. Reload systemd to recognize the new service.

4. Start your new service.

5. Check the status of your service.

6. View the log file created by your service.

## Exercise 6: Modifying Service Configuration

### TODO:
1. Examine the configuration of a service.

2. Find the location of a service's configuration file.

3. Make a backup of the service file before editing.

4. Modify your simple service to change the logging interval.

5. Check if the changes took effect.

6. Create an override configuration for a service.

## Exercise 7: Troubleshooting Service Issues

### TODO:
1. Check if a service is currently running.

2. View failed services on your system.

3. Check a service's last few log entries.

4. Find services that depend on a specific service.

5. Learn how to restart a service in debug mode.

6. Check for error messages in the system journal.

## Bonus Challenge:
Create a more complex systemd service that:
1. Monitors disk space usage
2. Sends a notification or email when disk space exceeds 80%
3. Logs the date, time, and disk usage to a log file
4. Runs the check every hour
5. Includes proper service dependencies and documentation 