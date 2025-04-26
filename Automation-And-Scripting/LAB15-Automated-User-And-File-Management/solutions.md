# LAB15 - Automated User and File Management Solutions

This file contains solutions to the exercises in LAB15. Try to solve the exercises yourself before looking at these solutions.

## Exercise 1: Basic User Creation Script

```bash
#!/bin/bash
# create_user.sh - Script to create a new user with basic settings

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Check if username is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <username> [comment]" >&2
    exit 1
fi

USERNAME=$1
COMMENT=${2:-"User $USERNAME"}

# Create the user with home directory
useradd -m -c "$COMMENT" "$USERNAME"

if [ $? -eq 0 ]; then
    echo "User $USERNAME created successfully"
    
    # Generate a random password
    PASSWORD=$(openssl rand -base64 12)
    
    # Set the password for the user
    echo "$USERNAME:$PASSWORD" | chpasswd
    
    echo "Password for $USERNAME set to: $PASSWORD"
    echo "Please change this password at first login"
else
    echo "Failed to create user $USERNAME" >&2
    exit 1
fi

exit 0
```

## Exercise 2: User Management from CSV File

```bash
#!/bin/bash
# batch_user_create.sh - Create multiple users from a CSV file

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Check if CSV file is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <csv_file>" >&2
    echo "CSV format should be: username,comment,group" >&2
    exit 1
fi

CSV_FILE=$1

# Check if file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "File $CSV_FILE does not exist" >&2
    exit 1
fi

# Log file
LOG_FILE="/var/log/user_creation_$(date +%Y%m%d_%H%M%S).log"
touch "$LOG_FILE" || { echo "Cannot create log file"; exit 1; }

echo "Starting user creation process at $(date)" | tee -a "$LOG_FILE"

# Read the CSV file line by line
while IFS=, read -r username comment group
do
    # Skip header or empty lines
    if [[ "$username" == "username" || -z "$username" ]]; then
        continue
    fi
    
    echo "Processing user: $username" | tee -a "$LOG_FILE"
    
    # Check if user already exists
    if id "$username" &>/dev/null; then
        echo "User $username already exists, skipping" | tee -a "$LOG_FILE"
        continue
    fi
    
    # Create user
    useradd -m -c "$comment" "$username" 2>&1 | tee -a "$LOG_FILE"
    
    # Generate random password
    password=$(openssl rand -base64 12)
    echo "$username:$password" | chpasswd
    
    # Add to group if specified
    if [ ! -z "$group" ]; then
        # Check if group exists, create if not
        if ! getent group "$group" &>/dev/null; then
            groupadd "$group" 2>&1 | tee -a "$LOG_FILE"
            echo "Group $group created" | tee -a "$LOG_FILE"
        fi
        
        # Add user to group
        usermod -a -G "$group" "$username" 2>&1 | tee -a "$LOG_FILE"
        echo "User $username added to group $group" | tee -a "$LOG_FILE"
    fi
    
    echo "User $username created with password: $password" | tee -a "$LOG_FILE"
    echo "----------------------------------------" | tee -a "$LOG_FILE"
    
done < "$CSV_FILE"

echo "User creation process completed at $(date)" | tee -a "$LOG_FILE"
echo "Log file available at: $LOG_FILE"

exit 0
```

## Exercise 3: Project Directory Structure Creation

```bash
#!/bin/bash
# create_project.sh - Script to create a standardized project directory structure

# Check if project name is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <project_name> [owner]" >&2
    exit 1
fi

PROJECT_NAME=$1
OWNER=${2:-$(whoami)}

# Check if owner exists
if ! id "$OWNER" &>/dev/null; then
    echo "User $OWNER does not exist" >&2
    exit 1
fi

# Base directory for projects
PROJECTS_DIR="/opt/projects"

# Create projects directory if it doesn't exist
if [ ! -d "$PROJECTS_DIR" ]; then
    sudo mkdir -p "$PROJECTS_DIR"
    echo "Created base projects directory: $PROJECTS_DIR"
fi

# Full path to the project
PROJECT_DIR="$PROJECTS_DIR/$PROJECT_NAME"

# Check if project already exists
if [ -d "$PROJECT_DIR" ]; then
    echo "Project directory already exists: $PROJECT_DIR" >&2
    exit 1
fi

# Create project directory and subdirectories
echo "Creating project structure for $PROJECT_NAME..."

sudo mkdir -p "$PROJECT_DIR"
sudo mkdir -p "$PROJECT_DIR/src"
sudo mkdir -p "$PROJECT_DIR/docs"
sudo mkdir -p "$PROJECT_DIR/tests"
sudo mkdir -p "$PROJECT_DIR/data"
sudo mkdir -p "$PROJECT_DIR/logs"

# Create README file
cat > /tmp/README.md << EOF
# $PROJECT_NAME

Project created on $(date)
Owner: $OWNER

## Description
Add project description here.

## Structure
- src/: Source code
- docs/: Documentation
- tests/: Test files and scripts
- data/: Data files
- logs/: Log files
EOF

sudo mv /tmp/README.md "$PROJECT_DIR/README.md"

# Set ownership and permissions
sudo chown -R "$OWNER:$OWNER" "$PROJECT_DIR"
sudo chmod -R 750 "$PROJECT_DIR"
sudo chmod -R 770 "$PROJECT_DIR/logs"

echo "Project created successfully at $PROJECT_DIR"
echo "Owner set to $OWNER"
echo "Standard directories created: src, docs, tests, data, logs"

exit 0
```

## Exercise 4: File Cleanup Script

```bash
#!/bin/bash
# file_cleanup.sh - Script to find and manage old files

# Check for required arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <directory> <days> [action]" >&2
    echo "  directory: Directory to scan for old files" >&2
    echo "  days: Files older than this many days will be processed" >&2
    echo "  action: (optional) What to do with old files - list, archive, or delete (default: list)" >&2
    exit 1
fi

DIRECTORY=$1
DAYS=$2
ACTION=${3:-"list"}

# Validate directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Directory does not exist: $DIRECTORY" >&2
    exit 1
fi

# Validate days is a number
if ! [[ "$DAYS" =~ ^[0-9]+$ ]]; then
    echo "Days must be a positive number" >&2
    exit 1
fi

# Validate action
if [[ ! "$ACTION" =~ ^(list|archive|delete)$ ]]; then
    echo "Invalid action: $ACTION" >&2
    echo "Action must be one of: list, archive, delete" >&2
    exit 1
fi

# Create log file
LOG_FILE="/tmp/file_cleanup_$(date +%Y%m%d_%H%M%S).log"
echo "Starting file cleanup in $DIRECTORY at $(date)" > "$LOG_FILE"
echo "Finding files older than $DAYS days for action: $ACTION" >> "$LOG_FILE"

# Find old files
OLD_FILES=$(find "$DIRECTORY" -type f -mtime +$DAYS)

# Check if any files were found
if [ -z "$OLD_FILES" ]; then
    echo "No files found older than $DAYS days in $DIRECTORY" | tee -a "$LOG_FILE"
    exit 0
fi

# Count files found
FILE_COUNT=$(echo "$OLD_FILES" | wc -l)
echo "Found $FILE_COUNT files older than $DAYS days" | tee -a "$LOG_FILE"

# Process files based on action
case "$ACTION" in
    list)
        echo "Listing files older than $DAYS days:" | tee -a "$LOG_FILE"
        echo "$OLD_FILES" | tee -a "$LOG_FILE"
        ;;
    archive)
        ARCHIVE_DIR="$DIRECTORY/archived_$(date +%Y%m%d)"
        mkdir -p "$ARCHIVE_DIR"
        
        echo "Archiving files to $ARCHIVE_DIR" | tee -a "$LOG_FILE"
        
        while IFS= read -r file; do
            if [ -f "$file" ]; then
                mv "$file" "$ARCHIVE_DIR/"
                echo "Moved: $file -> $ARCHIVE_DIR/" >> "$LOG_FILE"
            fi
        done <<< "$OLD_FILES"
        
        # Create an archive if there are files
        if [ "$(ls -A "$ARCHIVE_DIR")" ]; then
            tar -czf "${ARCHIVE_DIR}.tar.gz" "$ARCHIVE_DIR"
            rm -rf "$ARCHIVE_DIR"
            echo "Created archive: ${ARCHIVE_DIR}.tar.gz" | tee -a "$LOG_FILE"
        else
            rmdir "$ARCHIVE_DIR"
            echo "No files to archive" | tee -a "$LOG_FILE"
        fi
        ;;
    delete)
        echo "Deleting files older than $DAYS days:" | tee -a "$LOG_FILE"
        echo "Are you sure you want to delete these files? (y/n)"
        read -r CONFIRM
        
        if [ "$CONFIRM" = "y" ]; then
            while IFS= read -r file; do
                if [ -f "$file" ]; then
                    rm "$file"
                    echo "Deleted: $file" >> "$LOG_FILE"
                fi
            done <<< "$OLD_FILES"
            echo "Deletion complete" | tee -a "$LOG_FILE"
        else
            echo "Deletion cancelled" | tee -a "$LOG_FILE"
        fi
        ;;
esac

echo "File cleanup completed at $(date)" | tee -a "$LOG_FILE"
echo "Log file available at: $LOG_FILE"

exit 0
```

## Exercise 5: User Activity Monitor

```bash
#!/bin/bash
# user_activity.sh - Monitor and report user activity

# Log file
LOG_FILE="/var/log/user_activity_$(date +%Y%m%d).log"

# Function to get active users
get_active_users() {
    echo "Active users as of $(date):"
    who
    echo ""
}

# Function to get login history
get_login_history() {
    local days=$1
    echo "Login history for the past $days days:"
    last -n 20 | head -n 20
    echo ""
}

# Function to get user process info
get_user_processes() {
    local user=$1
    echo "Processes for user $user:"
    ps -u "$user" -o pid,ppid,cmd,%cpu,%mem,start
    echo ""
}

# Function to check disk usage by user
check_home_usage() {
    echo "Home directory usage by user:"
    du -sh /home/* 2>/dev/null | sort -hr
    echo ""
}

# Main execution
echo "User Activity Report - $(date)" | tee -a "$LOG_FILE"
echo "==================================" | tee -a "$LOG_FILE"

# Get active users
get_active_users | tee -a "$LOG_FILE"

# Get login history for past 7 days
get_login_history 7 | tee -a "$LOG_FILE"

# Get process info for each active user
for user in $(who | cut -d' ' -f1 | sort -u); do
    get_user_processes "$user" | tee -a "$LOG_FILE"
done

# Check disk usage
check_home_usage | tee -a "$LOG_FILE"

echo "Report completed at $(date)" | tee -a "$LOG_FILE"
echo "Log file available at: $LOG_FILE"

exit 0
```

## Bonus Challenge: Comprehensive User Management System

```bash
#!/bin/bash
# user_management_system.sh - Comprehensive user management system

# Log file and configuration directory
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
CONFIG_DIR="$SCRIPT_DIR/config"
LOG_DIR="$SCRIPT_DIR/logs"
USER_DB="$CONFIG_DIR/users.db"

# Create directories if they don't exist
mkdir -p "$CONFIG_DIR" "$LOG_DIR"

# Initialize log file
LOG_FILE="$LOG_DIR/user_management_$(date +%Y%m%d).log"
touch "$LOG_FILE"

# Function to log messages
log_message() {
    local level=$1
    local message=$2
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] [$level] $message" >> "$LOG_FILE"
}

# Function to display usage
usage() {
    echo "Usage: $0 [option] [arguments]"
    echo "Options:"
    echo "  -c, --create USERNAME   Create a new user"
    echo "  -d, --delete USERNAME   Delete an existing user"
    echo "  -m, --modify USERNAME   Modify user attributes"
    echo "  -l, --list              List all users"
    echo "  -i, --import FILE       Import users from CSV file"
    echo "  -b, --backup            Backup user configuration"
    echo "  -r, --report            Generate user report"
    echo "  -h, --help              Display this help message"
    exit 1
}

# Function to create a user
create_user() {
    local username=$1
    
    # Check if user already exists
    if id "$username" &>/dev/null; then
        log_message "ERROR" "User $username already exists"
        echo "User $username already exists"
        return 1
    fi
    
    # Get user information
    read -p "Full Name: " full_name
    read -p "Group (default: users): " group
    group=${group:-users}
    
    # Check if group exists, create if not
    if ! getent group "$group" &>/dev/null; then
        groupadd "$group"
        log_message "INFO" "Group $group created"
    fi
    
    # Create user
    useradd -m -c "$full_name" -g "$group" "$username"
    
    if [ $? -eq 0 ]; then
        # Generate a random password
        password=$(openssl rand -base64 12)
        echo "$username:$password" | chpasswd
        
        # Force password change at next login
        passwd -e "$username" >/dev/null
        
        # Save user to database
        echo "$username:$full_name:$group:$(date +%Y-%m-%d)" >> "$USER_DB"
        
        log_message "INFO" "User $username created successfully"
        echo "User $username created successfully"
        echo "Temporary password: $password"
        echo "User will be required to change password at next login"
    else
        log_message "ERROR" "Failed to create user $username"
        echo "Failed to create user $username"
        return 1
    fi
}

# Function to delete a user
delete_user() {
    local username=$1
    
    # Check if user exists
    if ! id "$username" &>/dev/null; then
        log_message "ERROR" "User $username does not exist"
        echo "User $username does not exist"
        return 1
    fi
    
    read -p "Delete home directory? (y/n): " delete_home
    
    if [ "$delete_home" = "y" ]; then
        userdel -r "$username"
    else
        userdel "$username"
    fi
    
    if [ $? -eq 0 ]; then
        # Remove from database
        sed -i "/^${username}:/d" "$USER_DB"
        
        log_message "INFO" "User $username deleted successfully"
        echo "User $username deleted successfully"
    else
        log_message "ERROR" "Failed to delete user $username"
        echo "Failed to delete user $username"
        return 1
    fi
}

# Function to modify a user
modify_user() {
    local username=$1
    
    # Check if user exists
    if ! id "$username" &>/dev/null; then
        log_message "ERROR" "User $username does not exist"
        echo "User $username does not exist"
        return 1
    fi
    
    echo "Modify user $username:"
    echo "1) Change full name"
    echo "2) Change group"
    echo "3) Reset password"
    echo "4) Back to main menu"
    
    read -p "Select option: " option
    
    case $option in
        1)
            read -p "New full name: " full_name
            usermod -c "$full_name" "$username"
            
            # Update database
            sed -i "s/^${username}:[^:]*:/${username}:${full_name}:/g" "$USER_DB"
            
            log_message "INFO" "Changed full name for user $username"
            echo "Full name changed successfully"
            ;;
        2)
            read -p "New group: " group
            
            # Check if group exists, create if not
            if ! getent group "$group" &>/dev/null; then
                groupadd "$group"
                log_message "INFO" "Group $group created"
            fi
            
            usermod -g "$group" "$username"
            
            # Update database
            sed -i "s/^${username}:[^:]*:[^:]*:/${username}:$(grep "^${username}:" "$USER_DB" | cut -d: -f2):${group}:/g" "$USER_DB"
            
            log_message "INFO" "Changed group for user $username to $group"
            echo "Group changed successfully"
            ;;
        3)
            # Generate a random password
            password=$(openssl rand -base64 12)
            echo "$username:$password" | chpasswd
            
            # Force password change at next login
            passwd -e "$username" >/dev/null
            
            log_message "INFO" "Reset password for user $username"
            echo "Password reset successfully"
            echo "Temporary password: $password"
            echo "User will be required to change password at next login"
            ;;
        4)
            return 0
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
}

# Function to list users
list_users() {
    if [ -f "$USER_DB" ]; then
        echo "User list:"
        echo "---------------------------------"
        echo "Username | Full Name | Group | Created"
        echo "---------------------------------"
        cat "$USER_DB" | while IFS=: read -r username full_name group created; do
            echo "$username | $full_name | $group | $created"
        done
    else
        echo "No users in database"
    fi
}

# Function to import users from CSV
import_users() {
    local csv_file=$1
    
    # Check if file exists
    if [ ! -f "$csv_file" ]; then
        log_message "ERROR" "File $csv_file does not exist"
        echo "File $csv_file does not exist"
        return 1
    fi
    
    echo "Importing users from $csv_file..."
    
    # Read CSV file line by line
    cat "$csv_file" | while IFS=, read -r username full_name group; do
        # Skip header or empty lines
        if [[ "$username" == "username" || -z "$username" ]]; then
            continue
        fi
        
        # Check if user already exists
        if id "$username" &>/dev/null; then
            log_message "WARNING" "User $username already exists, skipping"
            echo "User $username already exists, skipping"
            continue
        fi
        
        # Check if group exists, create if not
        if ! getent group "$group" &>/dev/null; then
            groupadd "$group"
            log_message "INFO" "Group $group created"
        fi
        
        # Create user
        useradd -m -c "$full_name" -g "$group" "$username"
        
        if [ $? -eq 0 ]; then
            # Generate a random password
            password=$(openssl rand -base64 12)
            echo "$username:$password" | chpasswd
            
            # Force password change at next login
            passwd -e "$username" >/dev/null
            
            # Save user to database
            echo "$username:$full_name:$group:$(date +%Y-%m-%d)" >> "$USER_DB"
            
            log_message "INFO" "User $username imported successfully"
            echo "User $username imported successfully (Password: $password)"
        else
            log_message "ERROR" "Failed to import user $username"
            echo "Failed to import user $username"
        fi
    done
    
    echo "Import completed"
}

# Function to backup user configuration
backup_users() {
    local backup_dir="$SCRIPT_DIR/backups"
    local backup_file="$backup_dir/user_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
    
    # Create backup directory if it doesn't exist
    mkdir -p "$backup_dir"
    
    # Create backup
    tar -czf "$backup_file" "$CONFIG_DIR" "$LOG_DIR"
    
    if [ $? -eq 0 ]; then
        log_message "INFO" "Backup created: $backup_file"
        echo "Backup created: $backup_file"
    else
        log_message "ERROR" "Failed to create backup"
        echo "Failed to create backup"
        return 1
    fi
}

# Function to generate user report
generate_report() {
    local report_file="$LOG_DIR/user_report_$(date +%Y%m%d).txt"
    
    echo "User Management Report - $(date)" > "$report_file"
    echo "=================================" >> "$report_file"
    
    # Total users
    echo "Total users: $(wc -l < "$USER_DB")" >> "$report_file"
    echo "" >> "$report_file"
    
    # List all users
    echo "User List:" >> "$report_file"
    echo "---------------------------------" >> "$report_file"
    echo "Username | Full Name | Group | Created" >> "$report_file"
    echo "---------------------------------" >> "$report_file"
    cat "$USER_DB" | while IFS=: read -r username full_name group created; do
        echo "$username | $full_name | $group | $created" >> "$report_file"
    done
    echo "" >> "$report_file"
    
    # Disk usage by user
    echo "Home Directory Usage:" >> "$report_file"
    echo "---------------------------------" >> "$report_file"
    du -sh /home/* 2>/dev/null | sort -hr >> "$report_file"
    
    log_message "INFO" "Report generated: $report_file"
    echo "Report generated: $report_file"
    
    # Display report
    less "$report_file"
}

# Main execution
if [[ $# -eq 0 ]]; then
    usage
fi

# Process command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--create)
            if [ "$(id -u)" -ne 0 ]; then
                echo "This option must be run as root"
                exit 1
            fi
            create_user "$2"
            shift 2
            ;;
        -d|--delete)
            if [ "$(id -u)" -ne 0 ]; then
                echo "This option must be run as root"
                exit 1
            fi
            delete_user "$2"
            shift 2
            ;;
        -m|--modify)
            if [ "$(id -u)" -ne 0 ]; then
                echo "This option must be run as root"
                exit 1
            fi
            modify_user "$2"
            shift 2
            ;;
        -l|--list)
            list_users
            shift
            ;;
        -i|--import)
            if [ "$(id -u)" -ne 0 ]; then
                echo "This option must be run as root"
                exit 1
            fi
            import_users "$2"
            shift 2
            ;;
        -b|--backup)
            backup_users
            shift
            ;;
        -r|--report)
            if [ "$(id -u)" -ne 0 ]; then
                echo "This option must be run as root"
                exit 1
            fi
            generate_report
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            usage
            ;;
    esac
done

exit 0
```

## Cleanup

To remove the files created in this lab, run the following commands:

```bash
# Remove scripts
rm -f create_user.sh batch_user_create.sh create_project.sh file_cleanup.sh user_activity.sh user_management_system.sh

# Remove any project directories created (if applicable)
sudo rm -rf /opt/projects/*

# Remove any log files created
rm -f /tmp/file_cleanup_*.log
rm -f /var/log/user_creation_*.log
rm -f /var/log/user_activity_*.log

# Remove any backup files or directories created
rm -rf backups/
rm -rf config/
rm -rf logs/
``` 