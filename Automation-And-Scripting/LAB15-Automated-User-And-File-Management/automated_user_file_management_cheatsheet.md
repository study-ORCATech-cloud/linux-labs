# LAB15 - Automated User and File Management Cheatsheet

This cheatsheet provides a quick reference for scripting user creation, file management, and other system administration tasks in Linux.

## User Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `useradd` | Create a new user | `useradd -m username` |
| `usermod` | Modify user properties | `usermod -aG sudo username` |
| `userdel` | Delete a user | `userdel -r username` |
| `passwd` | Set or change password | `passwd username` |
| `groupadd` | Create a new group | `groupadd developers` |
| `groupmod` | Modify group properties | `groupmod -n newname oldname` |
| `groupdel` | Delete a group | `groupdel groupname` |
| `id` | Display user/group information | `id username` |
| `chage` | Change user password expiry | `chage -d 0 username` |

## User Management Options

| Option | Description | Example |
|--------|-------------|---------|
| `-m` | Create home directory | `useradd -m john` |
| `-d` | Specify home directory | `useradd -d /custom/dir john` |
| `-s` | Specify shell | `useradd -s /bin/bash john` |
| `-G` | Add to secondary groups | `useradd -G admins,devs john` |
| `-c` | Add comment (full name) | `useradd -c "John Smith" john` |
| `-e` | Set account expiration date | `useradd -e 2023-12-31 john` |
| `-p` | Set encrypted password | `useradd -p $(openssl passwd -1 "password") john` |
| `-r` | Create system user | `useradd -r sysuser` |
| `-u` | Specify user ID | `useradd -u 1500 john` |
| `-g` | Specify primary group | `useradd -g developers john` |

## Password Management

| Command | Description | Example |
|---------|-------------|---------|
| `openssl passwd` | Generate encrypted password | `openssl passwd -1 "password"` |
| `chage -d 0` | Force password change on login | `chage -d 0 username` |
| `chage -l` | List password aging info | `chage -l username` |
| `chage -M` | Set maximum password age | `chage -M 90 username` |
| `chage -m` | Set minimum password age | `chage -m 7 username` |
| `chage -W` | Set password expiry warning | `chage -W 7 username` |

## File and Directory Management

| Command | Description | Example |
|---------|-------------|---------|
| `mkdir` | Create directory | `mkdir -p /path/to/dir` |
| `cp` | Copy files | `cp -R source destination` |
| `chown` | Change file owner | `chown user:group file` |
| `chmod` | Change file permissions | `chmod 755 file` |
| `find` | Find files | `find /path -name "*.txt"` |
| `rsync` | Sync files | `rsync -av source/ destination/` |
| `setfacl` | Set file ACLs | `setfacl -m u:user:rwx file` |
| `getfacl` | Get file ACLs | `getfacl file` |
| `umask` | Set default permissions | `umask 022` |

## Permission Shortcuts

| Permission | Numeric | Symbolic | Meaning |
|------------|---------|----------|---------|
| Read | 4 | r | Read file or list directory |
| Write | 2 | w | Write to file or create/delete files in directory |
| Execute | 1 | x | Execute file or access directory |
| Read + Write | 6 | rw | Read and write |
| Read + Execute | 5 | rx | Read and execute |
| Write + Execute | 3 | wx | Write and execute |
| Full | 7 | rwx | Read, write, and execute |

## Special Permissions

| Permission | Numeric | Description | Example |
|------------|---------|-------------|---------|
| setuid | 4000 | Run as file owner | `chmod u+s file` or `chmod 4755 file` |
| setgid | 2000 | Run as group owner / inherit group | `chmod g+s file` or `chmod 2755 file` |
| sticky bit | 1000 | Prevent deletion by others | `chmod +t directory` or `chmod 1777 directory` |

## Scripting for User Management

### Basic User Creation Script
```bash
#!/bin/bash
# Basic user creation script

# Check if username provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 username"
  exit 1
fi

USERNAME=$1

# Create user and home directory
sudo useradd -m "$USERNAME"

# Set permissions
sudo chmod 700 /home/$USERNAME
```

### Random Password Generation
```bash
# Generate a random 12-character password
PASS=$(openssl rand -base64 12)

# Set the password for a user
echo "$USERNAME:$PASS" | sudo chpasswd

# Force password change on first login
sudo chage -d 0 "$USERNAME"
```

### Check if User Exists
```bash
# Check if user already exists
if id "$USERNAME" &>/dev/null; then
  echo "User $USERNAME already exists!"
  exit 1
fi
```

### Adding User to Groups
```bash
# Add user to multiple groups
GROUPS="sudo,developers,docker"
sudo usermod -aG "$GROUPS" "$USERNAME"
```

## Scripting for File Management

### Create Standard Directories
```bash
# Create standard directories for a user
DIRS="Documents Downloads Pictures Videos Projects .ssh"
for dir in $DIRS; do
  mkdir -p "/home/$USERNAME/$dir"
  chown "$USERNAME:$USERNAME" "/home/$USERNAME/$dir"
done
```

### Recursively Set Permissions
```bash
# Set permissions recursively, different for files and directories
find /path/to/dir -type f -exec chmod 644 {} \;
find /path/to/dir -type d -exec chmod 755 {} \;
```

### Setting Default File Permissions
```bash
# Set default permissions via umask in user's .profile
echo "umask 022" >> "/home/$USERNAME/.profile"
```

### Logging Tools and Techniques

```bash
# Define log file
LOG_FILE="/var/log/user_management.log"

# Log function
log() {
  local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$timestamp] $1" | tee -a "$LOG_FILE"
}

# Example usage
log "Creating user $USERNAME"
sudo useradd -m "$USERNAME" && log "User created successfully" || log "ERROR: Failed to create user"
```

## Reading from CSV Files

### Basic CSV Processing
```bash
#!/bin/bash
# Process users from CSV file

CSV_FILE="users.csv"

# Skip header line and process each user
tail -n +2 "$CSV_FILE" | while IFS=, read -r username groups home_dir; do
  echo "Creating user: $username"
  echo "Groups: $groups"
  echo "Home directory: $home_dir"
  
  # Create user with specified home directory
  sudo useradd -m -d "$home_dir" "$username"
  
  # Add to groups
  sudo usermod -aG "$groups" "$username"
done
```

## Error Handling in Scripts

```bash
# Set bash to exit on error
set -e

# Handle errors with a trap
trap 'echo "Error occurred at line $LINENO"; exit 1' ERR

# Check command success
if ! sudo useradd -m "$USERNAME"; then
  echo "Failed to create user $USERNAME"
  exit 1
fi

# Use conditional execution
mkdir -p /path/to/dir && echo "Directory created" || echo "Failed to create directory"
```

## Safety Measures for System Scripts

```bash
# Prevent running as normal user for tasks requiring sudo
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root or with sudo"
  exit 1
fi

# Confirm destructive actions
read -p "Are you sure you want to delete user $USERNAME? (y/n) " -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Operation cancelled."
  exit 1
fi

# Backup before changes
cp /etc/passwd /etc/passwd.bak

# Check for system directories before changing permissions
if [[ "$DIRECTORY" == "/" || "$DIRECTORY" == "/etc" || "$DIRECTORY" == "/bin" ]]; then
  echo "ERROR: Will not modify system directory $DIRECTORY"
  exit 1
fi
```

## Finding and Managing Files

```bash
# Find large files (> 100MB)
find /path/to/search -type f -size +100M

# Find files not accessed in 30 days
find /path/to/search -type f -atime +30

# Find files by owner
find /path/to/search -user username

# Find files with specific permissions
find /path/to/search -type f -perm 0777

# Count files in each subdirectory
find /path/to/search -type d -exec sh -c 'echo -n "{}: "; find "{}" -type f | wc -l' \;
```

## Best Practices for System Administration Scripts

1. **Always include a usage message**
2. **Check for required privileges**
3. **Validate all inputs**
4. **Include error handling**
5. **Log all significant actions**
6. **Include a dry-run option for destructive operations**
7. **Back up files before modifying them**
8. **Use comments liberally**
9. **Test extensively on non-production systems**
10. **Include cleanup procedures** 