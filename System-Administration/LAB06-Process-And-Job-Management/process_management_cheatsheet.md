# Process and Job Management Cheatsheet

## Process Viewing Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ps` | Show current processes | `ps` |
| `ps aux` | Show all processes for all users | `ps aux` |
| `ps -ef` | Show all processes in full format | `ps -ef` |
| `ps -eo pid,user,%cpu,%mem,cmd` | Show processes with custom columns | `ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu` |
| `ps -u username` | Show processes for a specific user | `ps -u root` |
| `ps -p PID` | Show information for specific PID | `ps -p 1234` |
| `ps --forest` | Show process tree | `ps -ef --forest` |
| `pstree` | Display tree of processes | `pstree -p` |
| `pgrep pattern` | Find processes by name pattern | `pgrep firefox` |

## Real-Time Monitoring

| Command | Description | Example |
|---------|-------------|---------|
| `top` | Interactive process viewer | `top` |
| `top -u username` | Show processes for specific user | `top -u root` |
| `htop` | Enhanced interactive process viewer | `htop` |
| `atop` | Advanced system & process monitor | `atop` |
| `glances` | Cross-platform monitoring tool | `glances` |
| `vmstat` | Report virtual memory statistics | `vmstat 1` |
| `iostat` | Report CPU and I/O statistics | `iostat -x 2` |
| `mpstat` | Report processor statistics | `mpstat -P ALL 2` |
| `iotop` | I/O usage monitor | `sudo iotop` |

## Job Control

| Command | Description | Example |
|---------|-------------|---------|
| `command &` | Run command in background | `sleep 100 &` |
| `jobs` | List background jobs | `jobs -l` |
| `fg` | Bring job to foreground | `fg %1` |
| `bg` | Resume job in background | `bg %1` |
| `Ctrl+Z` | Suspend foreground job | Press Ctrl+Z |
| `Ctrl+C` | Terminate foreground job | Press Ctrl+C |
| `disown` | Detach job from terminal | `disown %1` |
| `nohup command &` | Run command immune to hangups | `nohup ./script.sh &` |
| `screen` | Terminal session manager | `screen -S mysession` |
| `tmux` | Terminal multiplexer | `tmux new -s mysession` |

## Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `kill PID` | Send signal to process (default: TERM) | `kill 1234` |
| `kill -9 PID` | Force kill a process (SIGKILL) | `kill -9 1234` |
| `kill -l` | List available signals | `kill -l` |
| `kill %jobnumber` | Kill a job by its number | `kill %1` |
| `killall pattern` | Kill processes by name | `killall firefox` |
| `pkill pattern` | Kill processes by pattern | `pkill -9 fire` |
| `xkill` | Kill a GUI application by clicking on its window | `xkill` |

## Process Priority

| Command | Description | Example |
|---------|-------------|---------|
| `nice -n value command` | Start process with priority | `nice -n 10 ./script.sh` |
| `renice value -p PID` | Change priority of running process | `renice 10 -p 1234` |
| `renice value -u user` | Change priority for all user processes | `sudo renice 5 -u username` |
| `chrt` | Manipulate real-time attributes | `chrt -f 50 command` |

## System Resource Information

| Command | Description | Example |
|---------|-------------|---------|
| `free` | Display memory usage | `free -h` |
| `uptime` | Show system load and uptime | `uptime` |
| `w` | Show logged in users and load | `w` |
| `lsof` | List open files | `lsof -p 1234` |
| `lsof -i` | List internet connections | `lsof -i :22` |
| `fuser` | Identify processes using files/sockets | `fuser -v /home` |
| `pidstat` | Monitor individual tasks | `pidstat 1` |

## Process Creation and Control

| Command | Description | Example |
|---------|-------------|---------|
| `fork()` | System call to create a process | (Programming API) |
| `exec()` | System call to execute a program | (Programming API) |
| `daemon` | Run as a background service | (Programming concept) |
| `systemd` | System and service manager | `systemctl start service` |
| `cron` | Time-based job scheduler | `crontab -e` |
| `at` | One-time job scheduler | `at now + 5 minutes` |
| `ulimit` | Set/get resource limits | `ulimit -a` |

## Signals

| Signal | Number | Description | Can Be Caught? |
|--------|--------|-------------|----------------|
| `SIGHUP` | 1 | Hangup | Yes |
| `SIGINT` | 2 | Interrupt (Ctrl+C) | Yes |
| `SIGQUIT` | 3 | Quit | Yes |
| `SIGKILL` | 9 | Kill (cannot be caught) | No |
| `SIGTERM` | 15 | Terminate (default for kill) | Yes |
| `SIGSTOP` | 19 | Stop (cannot be caught) | No |
| `SIGTSTP` | 20 | Terminal stop (Ctrl+Z) | Yes |
| `SIGCONT` | 18 | Continue if stopped | Yes |

## Advanced Process Management Examples

```bash
# Find and kill processes using more than 90% CPU
ps aux | awk '$3 > 90.0 {print $2}' | xargs kill

# Run command with lower CPU priority and no I/O impact
ionice -c3 nice -n 19 command

# Monitor a specific process by PID
top -p 1234

# Track child processes
ps --forest -g $(pgrep process_name)

# Find processes using a specific file
lsof /path/to/file

# Monitor process creation in real-time
sudo strace -f -e trace=process -p $(pgrep process_name)

# Set memory limit for a process
ulimit -v 1000000 && command  # Limit to ~1GB

# Start a process that continues after logout
nohup command > output.log 2>&1 &
``` 