# LAB09 - System Startup and Services Solutions

Below are the solutions to the system startup and services exercises. Remember to try solving them on your own first!

## Exercise 1: Understanding System Boot Process

### Solution:
1. Reboot your system and observe boot process:
   ```bash
   # Reboot the system (make sure to save any work first!)
   sudo systemctl reboot
   ```

2. Check system boot time:
   ```bash
   systemd-analyze time
   ```
   Output example:
   ```
   Startup finished in 3.383s (kernel) + 12.286s (userspace) = 15.669s
   graphical.target reached after 12.279s in userspace
   ```

3. View boot time detailed breakdown:
   ```bash
   systemd-analyze blame
   ```
   Output example:
   ```
   5.208s NetworkManager-wait-online.service
   4.332s snapd.service
   2.683s dev-sda1.device
   1.832s udisks2.service
   1.770s accounts-daemon.service
   ...
   ```

4. Generate boot sequence visualization:
   ```bash
   systemd-analyze plot > boot-sequence.svg
   # View with a browser or image viewer
   ```

5. Check current runlevel/target:
   ```bash
   systemctl get-default
   ```
   Output example:
   ```
   graphical.target
   ```

6. List available systemd targets:
   ```bash
   ls -l /lib/systemd/system/runlevel*.target
   ```
   Output example:
   ```
   lrwxrwxrwx 1 root root 15 Apr 20 2020 /lib/systemd/system/runlevel0.target -> poweroff.target
   lrwxrwxrwx 1 root root 13 Apr 20 2020 /lib/systemd/system/runlevel1.target -> rescue.target
   lrwxrwxrwx 1 root root 17 Apr 20 2020 /lib/systemd/system/runlevel2.target -> multi-user.target
   ...
   ```

## Exercise 2: Basic Service Management

### Solution:
1. List all active services:
   ```bash
   systemctl list-units --type=service --state=active
   ```
   Output example:
   ```
   UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
   accounts-daemon.service            loaded active running Accounts Service
   apparmor.service                   loaded active exited  AppArmor initialization
   apport.service                     loaded active exited  LSB: automatic crash report generation
   ...
   ```

2. Check status of SSH service:
   ```bash
   systemctl status sshd
   # On Ubuntu/Debian, the service may be named ssh instead of sshd
   systemctl status ssh
   ```
   Output example:
   ```
   ● ssh.service - OpenBSD Secure Shell server
      Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
      Active: active (running) since Tue 2023-01-10 14:23:45 UTC; 3h 26min ago
     Process: 1039 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
    Main PID: 1087 (sshd)
      Tasks: 1 (limit: 4657)
     Memory: 5.6M
        CPU: 250ms
     CGroup: /system.slice/ssh.service
             └─1087 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
   ```

3. Start a service:
   ```bash
   # First check if service is running
   systemctl status sshd
   # If not running, start it
   sudo systemctl start sshd
   ```

4. Stop a running service:
   ```bash
   sudo systemctl stop sshd
   # Verify it's stopped
   systemctl status sshd
   ```
   Output example after stopping:
   ```
   ● ssh.service - OpenBSD Secure Shell server
      Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
      Active: inactive (dead) since Tue 2023-01-10 17:52:23 UTC; 5s ago
   ```

5. Restart a service:
   ```bash
   # Start the service again if it's stopped
   sudo systemctl start sshd
   # Then restart it
   sudo systemctl restart sshd
   ```

6. Reload service configuration:
   ```bash
   sudo systemctl reload sshd
   ```

## Exercise 3: Managing Service Boot Behavior

### Solution:
1. Check if a service is set to start at boot:
   ```bash
   systemctl is-enabled sshd
   ```
   Output example:
   ```
   enabled
   ```

2. Enable a service to start at boot:
   ```bash
   sudo systemctl enable sshd
   ```
   Output example:
   ```
   Synchronizing state of ssh.service with SysV service script with /lib/systemd/systemd-sysv-install.
   Executing: /lib/systemd/systemd-sysv-install enable ssh
   ```

3. Disable a service from starting at boot:
   ```bash
   sudo systemctl disable sshd
   ```
   Output example:
   ```
   Synchronizing state of ssh.service with SysV service script with /lib/systemd/systemd-sysv-install.
   Executing: /lib/systemd/systemd-sysv-install disable ssh
   ```

4. Re-enable the service for boot:
   ```bash
   sudo systemctl enable sshd
   ```

5. Mask a service:
   ```bash
   # First install cups if not already installed for this example
   sudo apt install cups -y   # For Debian/Ubuntu
   # or
   sudo yum install cups -y   # For RHEL/CentOS
   
   # Now mask the service
   sudo systemctl mask cups.service
   ```
   Output example:
   ```
   Created symlink /etc/systemd/system/cups.service → /dev/null.
   ```

6. Unmask a service:
   ```bash
   sudo systemctl unmask cups.service
   ```
   Output example:
   ```
   Removed /etc/systemd/system/cups.service.
   ```

## Exercise 4: Analyzing Service Logs

### Solution:
1. View the system journal:
   ```bash
   journalctl
   # Press Space to page through, q to quit
   ```

2. View logs for a specific service:
   ```bash
   journalctl -u sshd
   # Or on some systems:
   journalctl -u ssh
   ```

3. View logs since the last boot:
   ```bash
   journalctl -b
   ```

4. Follow logs in real-time:
   ```bash
   journalctl -f
   # Press Ctrl+C to exit
   ```

5. View logs within a time range:
   ```bash
   # Replace with actual dates
   journalctl --since "2023-01-01" --until "2023-01-02"
   ```

6. View logs for errors and above:
   ```bash
   journalctl -p err
   ```
   Priority levels are: emerg, alert, crit, err, warning, notice, info, debug

## Exercise 5: Creating a Simple Service

### Solution:
1. Create a simple shell script for the service:
   ```bash
   mkdir -p ~/scripts
   cat > ~/scripts/simple-service.sh << 'EOF'
   #!/bin/bash
   
   while true; do
     echo "Service running at $(date)" >> /tmp/simple-service.log
     sleep 60
   done
   EOF
   
   chmod +x ~/scripts/simple-service.sh
   ```

2. Create a systemd service file:
   ```bash
   sudo bash -c 'cat > /etc/systemd/system/simple-service.service << EOF
   [Unit]
   Description=Simple Example Service
   After=network.target
   
   [Service]
   Type=simple
   ExecStart='$HOME'/scripts/simple-service.sh
   Restart=on-failure
   User='$USER'
   
   [Install]
   WantedBy=multi-user.target
   EOF'
   ```

3. Reload systemd to recognize the new service:
   ```bash
   sudo systemctl daemon-reload
   ```

4. Start the new service:
   ```bash
   sudo systemctl start simple-service
   ```

5. Check the status of the service:
   ```bash
   systemctl status simple-service
   ```
   Output example:
   ```
   ● simple-service.service - Simple Example Service
      Loaded: loaded (/etc/systemd/system/simple-service.service; disabled; vendor preset: enabled)
      Active: active (running) since Tue 2023-01-10 18:15:23 UTC; 5s ago
    Main PID: 12345 (simple-service.s)
       Tasks: 2 (limit: 4657)
      Memory: 1.0M
         CPU: 5ms
      CGroup: /system.slice/simple-service.service
              └─12345 /bin/bash /home/user/scripts/simple-service.sh
   ```

6. View the log file:
   ```bash
   # Wait a minute for the script to write a log entry
   cat /tmp/simple-service.log
   ```
   Output example:
   ```
   Service running at Tue Jan 10 18:16:23 UTC 2023
   ```

## Exercise 6: Modifying Service Configuration

### Solution:
1. Examine a service configuration:
   ```bash
   systemctl cat sshd
   # or
   systemctl cat ssh
   ```
   Output example:
   ```
   # /lib/systemd/system/ssh.service
   [Unit]
   Description=OpenBSD Secure Shell server
   Documentation=man:sshd(8) man:sshd_config(5)
   After=network.target auditd.service
   ConditionPathExists=!/etc/ssh/sshd_not_to_be_run
   
   [Service]
   EnvironmentFile=-/etc/default/ssh
   ExecStartPre=/usr/sbin/sshd -t
   ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
   ExecReload=/usr/sbin/sshd -t
   ExecReload=/bin/kill -HUP $MAINPID
   KillMode=process
   Restart=on-failure
   RestartPreventExitStatus=255
   Type=exec
   RuntimeDirectory=sshd
   RuntimeDirectoryMode=0755
   
   [Install]
   WantedBy=multi-user.target
   Alias=sshd.service
   ```

2. Find service file location:
   ```bash
   systemctl show -p FragmentPath sshd
   # or
   systemctl show -p FragmentPath ssh
   ```
   Output example:
   ```
   FragmentPath=/lib/systemd/system/ssh.service
   ```

3. Backup the service file:
   ```bash
   sudo cp $(systemctl show -p FragmentPath sshd | cut -d= -f2) ~/sshd.service.backup
   # or
   sudo cp $(systemctl show -p FragmentPath ssh | cut -d= -f2) ~/ssh.service.backup
   ```

4. Edit the simple service to change interval:
   ```bash
   sudo systemctl stop simple-service
   
   # Edit the script to change sleep time
   sed -i 's/sleep 60/sleep 10/' ~/scripts/simple-service.sh
   
   # Start the service again
   sudo systemctl start simple-service
   ```

5. Check if changes took effect:
   ```bash
   sleep 30
   cat /tmp/simple-service.log
   ```
   You should see multiple entries about 10 seconds apart.

6. Create an override configuration:
   ```bash
   sudo systemctl edit simple-service
   
   # Add the following in the editor:
   [Service]
   Environment="LOG_FILE=/tmp/alternate-log.txt"
   
   # Save and exit the editor
   # This creates an override file in /etc/systemd/system/simple-service.service.d/
   ```

## Exercise 7: Troubleshooting Service Issues

### Solution:
1. Check if a service is running:
   ```bash
   systemctl is-active sshd
   # or
   systemctl is-active ssh
   ```
   Output example:
   ```
   active
   ```

2. View failed services:
   ```bash
   systemctl --failed
   ```
   Output example:
   ```
   UNIT            LOAD   ACTIVE SUB    DESCRIPTION
   apache2.service loaded failed failed The Apache HTTP Server
   
   LOAD   = Reflects whether the unit definition was properly loaded.
   ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
   SUB    = The low-level unit activation state, values depend on unit type.
   
   1 loaded units listed.
   ```

3. Check service's last log entries:
   ```bash
   journalctl -u sshd -n 20
   # or
   journalctl -u ssh -n 20
   ```

4. Find service dependencies:
   ```bash
   systemctl list-dependencies sshd
   # or
   systemctl list-dependencies ssh
   ```
   Output example:
   ```
   ssh.service
   ● ├─system.slice
   ● │ ├─apparmor.service
   ● │ ├─dev-hugepages.mount
   ● │ ├─dev-mqueue.mount
   ...
   ```

5. Restart a service in debug mode:
   ```bash
   # Stop the service first
   sudo systemctl stop systemd-networkd
   
   # Run it in debug mode
   sudo sh -c 'SYSTEMD_LOG_LEVEL=debug /usr/lib/systemd/systemd-networkd'
   # Press Ctrl+C to exit debug mode
   
   # Restart the service normally
   sudo systemctl start systemd-networkd
   ```

6. Check for error messages in journal:
   ```bash
   journalctl -p err..alert
   ```

## Bonus Challenge Solution:

Here's a complete solution for the disk space monitoring service:

```bash
# Step 1: Create the disk monitoring script
cat > ~/scripts/disk-monitor.sh << 'EOF'
#!/bin/bash

LOG_FILE="/var/log/disk-monitor.log"
THRESHOLD=80
EMAIL_TO="root"

# Ensure log file exists and is writable
touch "$LOG_FILE"
chmod 644 "$LOG_FILE"

# Get current date and time
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Check disk usage for all mounted filesystems
echo "[$DATE] Running disk space check" >> "$LOG_FILE"

df -h | grep -vE '^Filesystem|tmpfs|cdrom|udev' | while read line; do
    # Extract filesystem name and usage percentage
    fs_name=$(echo "$line" | awk '{print $1}')
    mount_point=$(echo "$line" | awk '{print $6}')
    usage=$(echo "$line" | awk '{print $5}' | sed 's/%//')
    
    echo "[$DATE] Checking $fs_name ($mount_point): $usage%" >> "$LOG_FILE"
    
    # Check if usage exceeds threshold
    if [ "$usage" -gt "$THRESHOLD" ]; then
        message="ALERT: Disk space on $fs_name ($mount_point) is at $usage%, exceeding threshold of $THRESHOLD%"
        echo "[$DATE] $message" >> "$LOG_FILE"
        
        # Send email notification
        echo "$message" | mail -s "Disk Space Alert on $(hostname)" "$EMAIL_TO"
        
        # Also send a system notification (works on desktop environments)
        if command -v notify-send &> /dev/null; then
            notify-send -u critical "Disk Space Alert" "$message"
        fi
    fi
done

echo "[$DATE] Disk space check completed" >> "$LOG_FILE"
EOF

# Make the script executable
chmod +x ~/scripts/disk-monitor.sh

# Step 2: Create the systemd service file
sudo bash -c 'cat > /etc/systemd/system/disk-monitor.service << EOF
[Unit]
Description=Disk Space Monitoring Service
Documentation=https://example.com/disk-monitor-docs
After=network.target

[Service]
Type=oneshot
ExecStart='$HOME'/scripts/disk-monitor.sh
User=root
EOF'

# Step 3: Create a timer to run the service hourly
sudo bash -c 'cat > /etc/systemd/system/disk-monitor.timer << EOF
[Unit]
Description=Run disk space monitoring hourly
Documentation=https://example.com/disk-monitor-docs

[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
Persistent=true
AccuracySec=1min

[Install]
WantedBy=timers.target
EOF'

# Step 4: Enable and start the timer
sudo systemctl daemon-reload
sudo systemctl enable disk-monitor.timer
sudo systemctl start disk-monitor.timer

# Step 5: Verify the timer is scheduled
systemctl list-timers | grep disk-monitor

# Step 6: Run the service once to test
sudo systemctl start disk-monitor.service
tail /var/log/disk-monitor.log
```

To use the service:
```bash
# Check status
systemctl status disk-monitor.timer

# View logs
sudo journalctl -u disk-monitor.service
cat /var/log/disk-monitor.log

# Stop the service
sudo systemctl stop disk-monitor.timer
sudo systemctl disable disk-monitor.timer
``` 