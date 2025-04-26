# Shell Scripting Basics - Solutions

This document contains solutions to the exercises in the Shell Scripting Basics lab. Use these as a reference after attempting the exercises yourself.

## Exercise 1: Your First Script

### Solution for 1.1: Hello World Script

```bash
#!/bin/bash
# A simple hello world script
echo "Hello, World!"
```

### Solution for 1.2: Date and Time Script

```bash
#!/bin/bash
# Script to display current date and time
echo "Current date and time: $(date)"
```

## Exercise 2: Working with Variables

### Solution for 2.1: Setting and Using Variables

```bash
#!/bin/bash
# Script demonstrating variables

# Set variables
NAME="Linux User"
CURRENT_DIR=$(pwd)
FILE_COUNT=$(ls | wc -l)

# Display variables
echo "Hello, $NAME!"
echo "You are currently in: $CURRENT_DIR"
echo "This directory contains $FILE_COUNT files/directories."
```

### Solution for 2.2: User Input

```bash
#!/bin/bash
# Script demonstrating user input

# Prompt for user input
read -p "Enter your name: " USER_NAME
read -p "Enter your favorite color: " FAV_COLOR

# Display personalized message
echo "Hello, $USER_NAME! Your favorite color is $FAV_COLOR."
```

### Solution for 2.3: Command-Line Arguments

```bash
#!/bin/bash
# Script demonstrating command-line arguments

# Check if at least one argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <name> [age]"
    exit 1
fi

# Get arguments
NAME=$1
AGE=$2

# Display message
echo "Hello, $NAME!"

# Check if age was provided
if [ -n "$AGE" ]; then
    echo "You are $AGE years old."
fi

# Display all arguments
echo "All arguments: $@"
echo "Number of arguments: $#"
```

## Exercise 3: Conditional Statements

### Solution for 3.1: Basic If Statement

```bash
#!/bin/bash
# Script demonstrating basic if statement

# Get user input
read -p "Enter a number: " NUMBER

# Check if the number is positive, negative, or zero
if [ $NUMBER -gt 0 ]; then
    echo "The number is positive."
elif [ $NUMBER -lt 0 ]; then
    echo "The number is negative."
else
    echo "The number is zero."
fi
```

### Solution for 3.2: File Check

```bash
#!/bin/bash
# Script demonstrating file checks

# Get filename from user
read -p "Enter a filename: " FILENAME

# Check if the file exists
if [ -e "$FILENAME" ]; then
    echo "File '$FILENAME' exists."
    
    # Check file type
    if [ -f "$FILENAME" ]; then
        echo "It is a regular file."
    elif [ -d "$FILENAME" ]; then
        echo "It is a directory."
    else
        echo "It is neither a regular file nor a directory."
    fi
    
    # Check permissions
    if [ -r "$FILENAME" ]; then
        echo "You have read permission."
    fi
    if [ -w "$FILENAME" ]; then
        echo "You have write permission."
    fi
    if [ -x "$FILENAME" ]; then
        echo "You have execute permission."
    fi
else
    echo "File '$FILENAME' does not exist."
fi
```

### Solution for 3.3: Case Statement

```bash
#!/bin/bash
# Script demonstrating case statement

# Get user input
read -p "Enter a fruit name (apple, banana, orange): " FRUIT

# Convert to lowercase
FRUIT=$(echo "$FRUIT" | tr '[:upper:]' '[:lower:]')

# Use case statement to provide information about the fruit
case $FRUIT in
    "apple")
        echo "Apples are red or green."
        ;;
    "banana")
        echo "Bananas are yellow."
        ;;
    "orange")
        echo "Oranges are orange."
        ;;
    *)
        echo "I don't know about that fruit."
        ;;
esac
```

## Exercise 4: Looping Constructs

### Solution for 4.1: For Loop

```bash
#!/bin/bash
# Script demonstrating for loop

# Using a list
echo "Looping through a list:"
for fruit in Apple Banana Cherry Orange; do
    echo "- $fruit"
done

# Using a range
echo -e "\nLooping through a range:"
for i in {1..5}; do
    echo "Number: $i"
done

# Looping through files
echo -e "\nFiles in current directory:"
for file in $(ls); do
    if [ -f "$file" ]; then
        echo "File: $file"
    elif [ -d "$file" ]; then
        echo "Directory: $file"
    fi
done
```

### Solution for 4.2: While Loop

```bash
#!/bin/bash
# Script demonstrating while loop

# Initialize counter
count=1

# Loop while count is less than or equal to 5
echo "Counting with while loop:"
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Reading file line by line
echo -e "\nReading file line by line:"
if [ -f "/etc/passwd" ]; then
    line_num=1
    while read -r line; do
        echo "Line $line_num: $line"
        line_num=$((line_num + 1))
        # Only read the first 5 lines
        if [ $line_num -gt 5 ]; then
            break
        fi
    done < "/etc/passwd"
else
    echo "File not found."
fi
```

### Solution for 4.3: Until Loop

```bash
#!/bin/bash
# Script demonstrating until loop

# Initialize counter
count=5

# Loop until count is less than 1
echo "Countdown with until loop:"
until [ $count -lt 1 ]; do
    echo "$count..."
    ((count--))
done
echo "Blast off!"
```

## Exercise 5: Working with Functions

### Solution for 5.1: Basic Function

```bash
#!/bin/bash
# Script demonstrating basic functions

# Define greeting function
greeting() {
    echo "Hello, welcome to shell scripting!"
}

# Define goodbye function
goodbye() {
    echo "Thank you for using this script. Goodbye!"
}

# Main script
echo "Script starting..."
greeting
echo "Performing some tasks..."
echo "Script ending..."
goodbye
```

### Solution for 5.2: Functions with Parameters

```bash
#!/bin/bash
# Script demonstrating functions with parameters

# Define a function with parameters
greet_person() {
    echo "Hello, $1!"
    if [ -n "$2" ]; then
        echo "Your age is $2."
    fi
}

# Define a function to calculate sum
calculate_sum() {
    local num1=$1
    local num2=$2
    echo "Sum of $num1 and $num2 is $((num1 + num2))."
}

# Main script
greet_person "Alice" 25
greet_person "Bob"
calculate_sum 10 20
```

### Solution for 5.3: Functions with Return Values

```bash
#!/bin/bash
# Script demonstrating functions with return values

# Function that returns a numeric value (0-255)
is_even() {
    if [ $(($1 % 2)) -eq 0 ]; then
        return 0  # True (even)
    else
        return 1  # False (odd)
    fi
}

# Function that returns a string
get_day_type() {
    local day=$(date +%u)  # 1-7, Monday is 1
    
    if [ $day -lt 6 ]; then
        echo "Today is a weekday."
    else
        echo "Today is a weekend day."
    fi
}

# Main script
read -p "Enter a number: " NUM

# Using numeric return value
is_even $NUM
if [ $? -eq 0 ]; then
    echo "$NUM is even."
else
    echo "$NUM is odd."
fi

# Using string return value (command substitution)
DAY_TYPE=$(get_day_type)
echo "$DAY_TYPE"
```

## Exercise 6: Practical Script - File Operations

### Solution: Backup Script

```bash
#!/bin/bash
# Backup script

# Get the source directory from user or use current directory
read -p "Enter the directory to backup [$(pwd)]: " SOURCE_DIR
SOURCE_DIR=${SOURCE_DIR:-$(pwd)}

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Generate backup filename with timestamp
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.tar.gz"

# Create backup directory if it doesn't exist
BACKUP_DIR="./backups"
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Created backup directory: $BACKUP_DIR"
fi

# Create the backup
echo "Creating backup of '$SOURCE_DIR'..."
tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup created successfully: $BACKUP_DIR/$BACKUP_FILE"
    echo "Backup size: $(du -h "$BACKUP_DIR/$BACKUP_FILE" | cut -f1)"
else
    echo "Error: Backup failed."
    exit 1
fi
```

## Exercise 7: Debugging and Error Handling

### Solution for 7.1: Debugging Script

```bash
#!/bin/bash
# Script demonstrating debugging techniques

# Turn on debugging
set -x

# Some operations
echo "Debugging is on"
NUM1=5
NUM2=10
SUM=$((NUM1 + NUM2))
echo "Sum: $SUM"

# Turn off debugging
set +x

echo "Debugging is off"

# Using bash -x to debug
echo "You can also run this script with: bash -x $0"
```

### Solution for 7.2: Error Handling Script

```bash
#!/bin/bash
# Script demonstrating error handling

# Error handling function
handle_error() {
    echo "Error: $1" >&2
    exit 1
}

# Create a directory
DIR_NAME="test_dir"
mkdir $DIR_NAME || handle_error "Failed to create directory $DIR_NAME"
echo "Directory $DIR_NAME created successfully."

# Try to create a file in a non-existent directory
echo "Content" > "/nonexistent_dir/test.txt" 2>/dev/null || handle_error "Failed to create file in /nonexistent_dir/"

# This line won't execute if the previous command fails
echo "Script completed successfully."
```

## Bonus Challenge: System Info Script

```bash
#!/bin/bash
# System Information Script

# Function to print section header
print_header() {
    echo "===== $1 ====="
}

# Function to get OS information
get_os_info() {
    print_header "SYSTEM INFORMATION"
    echo "Hostname: $(hostname)"
    echo "OS: $(cat /etc/os-release | grep "PRETTY_NAME" | cut -d'"' -f2)"
    echo "Kernel: $(uname -r)"
    echo "Uptime: $(uptime -p)"
}

# Function to get CPU information
get_cpu_info() {
    print_header "CPU INFORMATION"
    echo "CPU Model: $(grep "model name" /proc/cpuinfo | head -n1 | cut -d':' -f2 | sed 's/^[ \t]*//')"
    echo "CPU Cores: $(grep -c "processor" /proc/cpuinfo)"
    echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')"
}

# Function to get memory information
get_memory_info() {
    print_header "MEMORY INFORMATION"
    echo "Total Memory: $(free -h | grep "Mem:" | awk '{print $2}')"
    echo "Used Memory: $(free -h | grep "Mem:" | awk '{print $3}')"
    echo "Free Memory: $(free -h | grep "Mem:" | awk '{print $4}')"
}

# Function to get disk information
get_disk_info() {
    print_header "DISK INFORMATION"
    df -h | grep -E "^/dev/[a-z]" | awk '{print $1 " Size: " $2 " Used: " $3 " Available: " $4 " Use%: " $5 " Mounted: " $6}'
}

# Function to get network information
get_network_info() {
    print_header "NETWORK INFORMATION"
    echo "IP Address:"
    ip -4 addr show | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v "127.0.0.1"
    echo "Network Interfaces:"
    ip link show | grep -E "^[0-9]" | awk -F': ' '{print $2}'
}

# Function to get user information
get_user_info() {
    print_header "USER INFORMATION"
    echo "Current User: $(whoami)"
    echo "Users Logged In:"
    who
}

# Function to get process information
get_process_info() {
    print_header "PROCESS INFORMATION"
    echo "Total Running Processes: $(ps aux | wc -l)"
    echo "Top 5 CPU-Consuming Processes:"
    ps aux --sort=-%cpu | head -n 6
}

# Main function
main() {
    echo "System Information Report - $(date)"
    echo
    
    get_os_info
    echo
    
    get_cpu_info
    echo
    
    get_memory_info
    echo
    
    get_disk_info
    echo
    
    get_network_info
    echo
    
    get_user_info
    echo
    
    get_process_info
}

# Run the main function
main
```

## Cleanup

Remember to clean up all the files created during this lab:

```bash
# Remove all script files created during this lab
rm -f hello_world.sh date_time.sh
rm -f variables.sh user_input.sh command_line_args.sh
rm -f if_statement.sh file_check.sh case_statement.sh
rm -f for_loop.sh while_loop.sh until_loop.sh
rm -f functions_basic.sh functions_params.sh functions_return.sh
rm -f backup.sh
rm -f debug_script.sh error_handling.sh
rm -f system_info.sh

# Remove any test directories created
rm -rf test_dir backups
``` 