# System Startup and Services Cheatsheet

## Boot Process Commands

| Command | Description | Example |
|---------|-------------|---------|
| `systemd-analyze` | Analyze boot time | `systemd-analyze time` |
| `systemd-analyze blame` | Show time taken by each service | `systemd-analyze blame` |
| `systemd-analyze critical-chain` | Show critical chain of boot sequence | `systemd-analyze critical-chain` |
| `systemd-analyze plot` | Generate visualization of boot process | `systemd-analyze plot > boot.svg` |
| `dmesg` | Display kernel ring buffer messages | `dmesg` |
| `journalctl -b` | View boot messages from systemd journal | `journalctl -b` |
| `last reboot` | Show system reboot history | `last reboot` |

## Systemd Targets (Runlevels)

| Target | Traditional Runlevel | Description |
|--------|----------------------|-------------|
| `poweroff.target` | 0 | Shutdown system |
| `rescue.target` | 1 | Single-user mode (rescue) |
| `multi-user.target` | 2, 3, 4 | Multi-user, non-graphical |
| `graphical.target` | 5 | Multi-user, graphical |
| `reboot.target` | 6 | Reboot |
| `emergency.target` | - | Emergency shell |

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl get-default` | Show default target | `systemctl get-default` |
| `systemctl set-default` | Set default target | `sudo systemctl set-default multi-user.target` |
| `systemctl isolate` | Change to a different target | `sudo systemctl isolate rescue.target` |
| `systemctl list-units --type=target` | List all targets | `systemctl list-units --type=target` |

## Basic Service Management

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl status` | Check status of a service | `systemctl status sshd` |
| `systemctl start` | Start a service | `sudo systemctl start nginx` |
| `systemctl stop` | Stop a service | `sudo systemctl stop nginx` |
| `systemctl restart` | Restart a service | `sudo systemctl restart nginx` |
| `systemctl reload` | Reload configuration without restart | `sudo systemctl reload nginx` |
| `systemctl try-restart` | Restart only if service is running | `sudo systemctl try-restart nginx` |
| `systemctl reload-or-restart` | Reload if supported, otherwise restart | `sudo systemctl reload-or-restart nginx` |
| `systemctl kill` | Send signal to service | `sudo systemctl kill -s SIGTERM nginx` |

## Listing Services and Units

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl list-units` | List all loaded units | `systemctl list-units` |
| `systemctl list-units --type=service` | List loaded service units | `systemctl list-units --type=service` |
| `systemctl list-units --state=running` | List running units | `systemctl list-units --state=running` |
| `systemctl list-unit-files` | List all unit files | `systemctl list-unit-files` |
| `systemctl list-unit-files --state=enabled` | List enabled unit files | `systemctl list-unit-files --state=enabled` |
| `systemctl list-dependencies` | Show unit dependencies | `systemctl list-dependencies sshd` |
| `systemctl --failed` | List failed units | `systemctl --failed` |

## Service Autostart Management

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl is-enabled` | Check if service is enabled at boot | `systemctl is-enabled nginx` |
| `systemctl enable` | Enable service to start at boot | `sudo systemctl enable nginx` |
| `systemctl disable` | Disable service from starting at boot | `sudo systemctl disable nginx` |
| `systemctl mask` | Completely disable a service | `sudo systemctl mask nginx` |
| `systemctl unmask` | Remove masking from a service | `sudo systemctl unmask nginx` |
| `systemctl enable --now` | Enable and start service | `sudo systemctl enable --now nginx` |
| `systemctl disable --now` | Disable and stop service | `sudo systemctl disable --now nginx` |

## Service Configuration

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl show` | Show unit properties | `systemctl show sshd` |
| `systemctl cat` | Show unit file content | `systemctl cat sshd` |
| `systemctl edit` | Create snippet override file | `sudo systemctl edit sshd` |
| `systemctl edit --full` | Edit full unit file | `sudo systemctl edit --full sshd` |
| `systemctl daemon-reload` | Reload unit files | `sudo systemctl daemon-reload` |
| `systemctl preset` | Reset unit to default state | `sudo systemctl preset sshd` |
| `systemctl revert` | Revert unit file to original version | `sudo systemctl revert sshd` |

## Journal and Logging

| Command | Description | Example |
|---------|-------------|---------|
| `journalctl` | View systemd journal | `journalctl` |
| `journalctl -u` | View logs for specific unit | `journalctl -u nginx` |
| `journalctl -f` | Follow journal in real-time | `journalctl -f` |
| `journalctl -b` | Show logs from current boot | `journalctl -b` |
| `journalctl -b -1` | Show logs from previous boot | `journalctl -b -1` |
| `journalctl --since` | Show logs since time | `journalctl --since "2023-01-01 12:00:00"` |
| `journalctl --until` | Show logs until time | `journalctl --until "2023-01-01 13:00:00"` |
| `journalctl -p` | Filter by priority | `journalctl -p err` |
| `journalctl -k` | Show kernel messages | `journalctl -k` |
| `journalctl --disk-usage` | Show journal disk usage | `journalctl --disk-usage` |
| `journalctl --vacuum-size` | Reduce journal size | `sudo journalctl --vacuum-size=1G` |
| `journalctl --vacuum-time` | Delete old journal entries | `sudo journalctl --vacuum-time=1weeks` |

## System Control and Power Management

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl reboot` | Reboot system | `sudo systemctl reboot` |
| `systemctl poweroff` | Power off system | `sudo systemctl poweroff` |
| `systemctl suspend` | Suspend system | `sudo systemctl suspend` |
| `systemctl hibernate` | Hibernate system | `sudo systemctl hibernate` |
| `systemctl hybrid-sleep` | Hybrid sleep system | `sudo systemctl hybrid-sleep` |
| `systemctl rescue` | Enter rescue mode | `sudo systemctl rescue` |
| `systemctl emergency` | Enter emergency mode | `sudo systemctl emergency` |
| `loginctl` | Manage user logins | `loginctl list-users` |

## Creating Systemd Services

### Service Unit File Sections

| Section | Purpose |
|---------|---------|
| `[Unit]` | Metadata, dependencies, description |
| `[Service]` | Service behavior, command to execute |
| `[Install]` | Installation information for enabling |

### Common Unit Section Options

| Option | Description | Example |
|--------|-------------|---------|
| `Description` | Human-readable description | `Description=OpenSSH server daemon` |
| `Documentation` | URLs to documentation | `Documentation=man:sshd(8) man:sshd_config(5)` |
| `After` | Start after these units | `After=network.target` |
| `Requires` | Hard dependency units | `Requires=mysql.service` |
| `Wants` | Soft dependency units | `Wants=network-online.target` |
| `Conflicts` | Cannot run with these units | `Conflicts=sendmail.service` |

### Common Service Section Options

| Option | Description | Example |
|--------|-------------|---------|
| `Type` | Type of service startup | `Type=simple` |
| `ExecStart` | Command to execute on start | `ExecStart=/usr/sbin/sshd -D` |
| `ExecStop` | Command to execute on stop | `ExecStop=/bin/kill -TERM $MAINPID` |
| `ExecReload` | Command to reload configuration | `ExecReload=/bin/kill -HUP $MAINPID` |
| `Restart` | When to restart service | `Restart=on-failure` |
| `RestartSec` | Time to wait before restart | `RestartSec=5` |
| `User` | User to run service as | `User=www-data` |
| `Group` | Group to run service as | `Group=www-data` |
| `WorkingDirectory` | Working directory for service | `WorkingDirectory=/var/www` |
| `Environment` | Environment variables | `Environment="DEBUG=true"` |
| `EnvironmentFile` | File with environment variables | `EnvironmentFile=/etc/default/nginx` |
| `LimitNOFILE` | File descriptor limit | `LimitNOFILE=65535` |
| `TimeoutStartSec` | Timeout for starting | `TimeoutStartSec=30` |
| `TimeoutStopSec` | Timeout for stopping | `TimeoutStopSec=30` |

### Common Install Section Options

| Option | Description | Example |
|--------|-------------|---------|
| `WantedBy` | Target that wants this service | `WantedBy=multi-user.target` |
| `RequiredBy` | Target that requires this service | `RequiredBy=graphical.target` |
| `Also` | Units to also enable/disable | `Also=nginx-config-check.service` |
| `Alias` | Alternative names for unit | `Alias=http.service https.service` |

## Advanced Systemd Examples

```bash
# Creating a simple timer service (runs hourly)
cat > /etc/systemd/system/myscript.service << EOF
[Unit]
Description=My Custom Script
After=network.target

[Service]
Type=oneshot
ExecStart=/path/to/myscript.sh
User=myuser

[Install]
WantedBy=multi-user.target
EOF

cat > /etc/systemd/system/myscript.timer << EOF
[Unit]
Description=Run myscript hourly

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Enable and start the timer
systemctl enable --now myscript.timer

# Analyze system time at boot
systemd-analyze time

# Find which services take the most time to start
systemd-analyze blame | head -10

# Filter the journal by time range and service
journalctl -u nginx --since "2023-01-01" --until "2023-01-02"

# Find which service owns a specific process
systemctl status $PID

# Create a drop-in configuration file
mkdir -p /etc/systemd/system/sshd.service.d/
echo -e "[Service]\nLimitNOFILE=65535" > /etc/systemd/system/sshd.service.d/limits.conf
systemctl daemon-reload
systemctl restart sshd

# View service resource usage
systemd-cgtop

# Find all unit files with a specific string
grep -r "network" /lib/systemd/system/

# Monitor service resource usage
systemctl status nginx --continuous
``` 