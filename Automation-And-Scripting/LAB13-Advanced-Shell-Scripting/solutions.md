# LAB13 - Advanced Shell Scripting Solutions

Below are the solutions to the advanced shell scripting exercises. Remember to try solving them on your own first!

## Exercise 1: Advanced Function Usage

### Solution:

```bash
#!/bin/bash

# Simple function with return value
check_number() {
    local num=$1
    
    if [[ $num -gt 10 ]]; then
        return 0  # Success/true
    else
        return 1  # Failure/false
    fi
}

# Function that returns a value through echo
get_square() {
    local num=$1
    local result=$((num * num))
    echo $result
}

# Function with multiple arguments
calculate() {
    local operation=$1
    local num1=$2
    local num2=$3
    local result
    
    case $operation in
        "add")
            result=$((num1 + num2))
            ;;
        "subtract")
            result=$((num1 - num2))
            ;;
        "multiply")
            result=$((num1 * num2))
            ;;
        "divide")
            if [[ $num2 -eq 0 ]]; then
                echo "Error: Division by zero"
                return 1
            fi
            result=$((num1 / num2))
            ;;
        *)
            echo "Invalid operation: $operation"
            return 1
            ;;
    esac
    
    echo "Result of $operation: $result"
    return 0
}

# Main script execution
echo "Testing function with return value:"
check_number 15
if [[ $? -eq 0 ]]; then
    echo "Number is greater than 10"
else
    echo "Number is less than or equal to 10"
fi

check_number 5
if [[ $? -eq 0 ]]; then
    echo "Number is greater than 10"
else
    echo "Number is less than or equal to 10"
fi

echo -e "\nTesting function that returns a value:"
square_result=$(get_square 7)
echo "Square of 7 is $square_result"

echo -e "\nTesting function with multiple arguments:"
calculate add 10 5
calculate subtract 20 8
calculate multiply 6 7
calculate divide 100 5
calculate divide 10 0
calculate invalid_op 5 5
```

## Exercise 2: Advanced Script Arguments

### Solution:

```bash
#!/bin/bash

# Initialize variables with defaults
verbose=0
output_file=""
input_file=""
mode="default"

# Function to display help
show_help() {
    echo "Usage: $0 [OPTIONS] [ARGUMENTS]"
    echo "Process files with various options."
    echo
    echo "Options:"
    echo "  -h, --help            Display this help and exit"
    echo "  -v, --verbose         Enable verbose mode"
    echo "  -o, --output FILE     Specify output file"
    echo "  -i, --input FILE      Specify input file"
    echo "  -m, --mode MODE       Specify mode (default, standard, advanced)"
    echo
}

# Parse command-line options
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--verbose)
            verbose=1
            shift
            ;;
        -o|--output)
            if [[ -z $2 || $2 == -* ]]; then
                echo "Error: -o|--output requires a file argument"
                exit 1
            fi
            output_file=$2
            shift 2
            ;;
        -i|--input)
            if [[ -z $2 || $2 == -* ]]; then
                echo "Error: -i|--input requires a file argument"
                exit 1
            fi
            input_file=$2
            shift 2
            ;;
        -m|--mode)
            if [[ -z $2 || $2 == -* ]]; then
                echo "Error: -m|--mode requires an argument"
                exit 1
            fi
            mode=$2
            shift 2
            ;;
        -*)
            echo "Error: Unknown option: $1"
            show_help
            exit 1
            ;;
        *)
            # Handle positional arguments
            if [[ -z $input_file ]]; then
                input_file=$1
            elif [[ -z $output_file ]]; then
                output_file=$1
            else
                echo "Warning: Ignoring additional argument: $1"
            fi
            shift
            ;;
    esac
done

# Validate inputs
if [[ -z $input_file ]]; then
    echo "Error: Input file is required"
    show_help
    exit 1
fi

# Check if input file exists
if [[ ! -f $input_file ]]; then
    echo "Error: Input file '$input_file' does not exist"
    exit 1
fi

# Apply default output file name if not provided
if [[ -z $output_file ]]; then
    output_file="${input_file}.processed"
    if [[ $verbose -eq 1 ]]; then
        echo "Using default output file: $output_file"
    fi
fi

# Display settings in verbose mode
if [[ $verbose -eq 1 ]]; then
    echo "Settings:"
    echo "- Verbose mode: Enabled"
    echo "- Input file: $input_file"
    echo "- Output file: $output_file"
    echo "- Mode: $mode"
fi

# Process the file according to the mode
case $mode in
    "default")
        if [[ $verbose -eq 1 ]]; then
            echo "Processing in default mode..."
        fi
        # Simple copy for default mode
        cp "$input_file" "$output_file"
        ;;
    "standard")
        if [[ $verbose -eq 1 ]]; then
            echo "Processing in standard mode..."
        fi
        # Copy and add timestamp
        echo "# Processed on $(date)" > "$output_file"
        cat "$input_file" >> "$output_file"
        ;;
    "advanced")
        if [[ $verbose -eq 1 ]]; then
            echo "Processing in advanced mode..."
        fi
        # Copy, add timestamp, and line numbers
        echo "# Processed on $(date)" > "$output_file"
        nl -ba "$input_file" >> "$output_file"
        ;;
    *)
        echo "Error: Unknown mode: $mode"
        exit 1
        ;;
esac

echo "Processing complete. Output saved to $output_file"
```

## Exercise 3: Error Handling and Debugging

### Solution:

```bash
#!/bin/bash

# Enable error tracing for debugging
# Uncomment the following line to enable
# set -x

# Exit on error
set -e

# Make unset variables an error
set -u

# Trap for cleanup
trap cleanup EXIT

# Variables
log_file="error_handling_demo.log"
temp_dir="temp_demo_dir"

# Function to log messages
log_message() {
    local level=$1
    local message=$2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" | tee -a "$log_file"
}

# Function for cleanup
cleanup() {
    log_message "INFO" "Cleaning up..."
    if [[ -d "$temp_dir" ]]; then
        rm -rf "$temp_dir"
        log_message "INFO" "Removed temporary directory: $temp_dir"
    fi
    log_message "INFO" "Cleanup completed"
}

# Function that might fail
risky_operation() {
    local filename=$1
    
    # Check if file exists
    if [[ ! -f "$filename" ]]; then
        log_message "ERROR" "File not found: $filename"
        return 1
    fi
    
    # Try to process the file
    log_message "INFO" "Processing file: $filename"
    
    # Simulate a command that might fail
    cat "$filename" > /dev/null
    if [[ $? -ne 0 ]]; then
        log_message "ERROR" "Failed to process file: $filename"
        return 2
    fi
    
    log_message "INFO" "Successfully processed file: $filename"
    return 0
}

# Function to handle errors
handle_error() {
    local status=$1
    local operation=$2
    
    if [[ $status -eq 0 ]]; then
        log_message "INFO" "$operation completed successfully"
    else
        log_message "ERROR" "$operation failed with status $status"
        # Depending on your requirement, you might want to exit or continue
        # exit $status
    fi
}

# Create log file if it doesn't exist
touch "$log_file"
log_message "INFO" "Starting script"

# Create temporary directory safely
if [[ -d "$temp_dir" ]]; then
    log_message "WARN" "Temporary directory already exists: $temp_dir"
    rm -rf "$temp_dir"
fi

mkdir -p "$temp_dir"
log_message "INFO" "Created temporary directory: $temp_dir"

# Create a test file
echo "This is a test file" > "$temp_dir/test.txt"
log_message "INFO" "Created test file: $temp_dir/test.txt"

# Try operations with error handling
log_message "INFO" "Attempting to process existing file"
risky_operation "$temp_dir/test.txt"
handle_error $? "Processing existing file"

log_message "INFO" "Attempting to process non-existent file"
# Temporarily disable exit on error for this operation
set +e
risky_operation "$temp_dir/nonexistent.txt"
handle_error $? "Processing non-existent file"
# Re-enable exit on error
set -e

log_message "INFO" "Script completed successfully"
```

## Exercise 4: Working with Advanced Text Processing

### Solution:

```bash
#!/bin/bash

# Sample data file
data_file="sample_data.txt"

# Create sample data
cat > "$data_file" << 'EOF'
John,Doe,35,New York,Engineer,75000
Jane,Smith,28,Los Angeles,Designer,65000
Bob,Johnson,42,Chicago,Manager,85000
Alice,Williams,31,Boston,Developer,72000
Charlie,Brown,39,Seattle,Architect,95000
Diana,Miller,27,Austin,Analyst,62000
Edward,Davis,45,Denver,Director,110000
Fiona,Wilson,33,Portland,Programmer,78000
George,Moore,29,Atlanta,Designer,67000
Helen,Taylor,38,Miami,Manager,88000
EOF

echo "Created sample data file: $data_file"

# 1. Extract and display all names (first and last)
echo -e "\n1. All names (first and last):"
awk -F, '{print $1 " " $2}' "$data_file"

# 2. Display people older than 35
echo -e "\n2. People older than 35:"
awk -F, '$3 > 35 {print $1 " " $2 ", Age: " $3}' "$data_file"

# 3. Calculate and display average salary
echo -e "\n3. Average salary:"
awk -F, '{ sum += $6; count++ } END { printf "Average salary: $%.2f\n", sum/count }' "$data_file"

# 4. List all unique job titles
echo -e "\n4. Unique job titles:"
awk -F, '{ print $5 }' "$data_file" | sort | uniq

# 5. Display records sorted by salary (highest to lowest)
echo -e "\n5. Records sorted by salary (highest to lowest):"
sort -t, -k6,6 -nr "$data_file" | awk -F, '{printf "%-10s %-10s $%s\n", $1, $2, $6}'

# 6. Format the data as a proper table using column
echo -e "\n6. Data formatted as a table:"
echo "First Name,Last Name,Age,City,Position,Salary" > header.txt
cat header.txt "$data_file" | sed 's/,/|/g' | column -t -s '|'
rm header.txt

# 7. Extract information using sed
echo -e "\n7. Extract cities with sed:"
sed -n 's/.*,\(.*\),.*,.*/\1/p' "$data_file"

# 8. Replace job titles
echo -e "\n8. Replace 'Designer' with 'UI/UX Designer':"
sed 's/Designer/UI\/UX Designer/g' "$data_file"

# 9. Extract with grep
echo -e "\n9. Records from New York or Boston:"
grep -E '(New York|Boston)' "$data_file"

# 10. Combine tools
echo -e "\n10. Combined processing - Developers and Programmers sorted by age:"
grep -E '(Developer|Programmer)' "$data_file" | sort -t, -k3,3 -n | 
  awk -F, '{printf "%-10s %-10s Age: %s, Position: %s\n", $1, $2, $3, $5}'

# Clean up
echo -e "\nCleaning up..."
rm "$data_file"
echo "Done."
```

## Exercise 5: Process Management

### Solution:

```bash
#!/bin/bash

# File to save PIDs
pid_file="background_processes.pid"

# Function to display help
show_help() {
    echo "Process Management Demo"
    echo "Usage: $0 [command]"
    echo "Commands:"
    echo "  start   - Start background processes"
    echo "  status  - Check status of running processes"
    echo "  stop    - Stop all running processes"
    echo "  help    - Show this help message"
}

# Function to start background processes
start_processes() {
    echo "Starting background processes..."
    
    # Create PID file or clear if it exists
    > "$pid_file"
    
    # Start first background process - simulate CPU work
    (
        while true; do
            for i in {1..1000}; do
                echo "CPU work $i" > /dev/null
            done
            sleep 1
        done
    ) &
    echo $! >> "$pid_file"
    echo "Started CPU work process with PID: $!"
    
    # Start second background process - simulate disk I/O
    (
        while true; do
            dd if=/dev/zero of=/tmp/temp_file bs=1M count=10 2>/dev/null
            rm /tmp/temp_file
            sleep 2
        done
    ) &
    echo $! >> "$pid_file"
    echo "Started disk I/O process with PID: $!"
    
    # Start third background process - simulate periodic task
    (
        counter=0
        while true; do
            counter=$((counter + 1))
            echo "Task iteration $counter" > /tmp/task_status
            sleep 5
        done
    ) &
    echo $! >> "$pid_file"
    echo "Started periodic task process with PID: $!"
    
    echo "All processes started. PIDs saved to $pid_file"
}

# Function to check process status
check_status() {
    echo "Checking status of background processes..."
    
    if [[ ! -f "$pid_file" ]]; then
        echo "PID file not found. No processes are running."
        return 1
    fi
    
    while read -r pid; do
        if ps -p "$pid" > /dev/null; then
            echo "Process $pid is running"
            echo "Details:"
            ps -f -p "$pid"
        else
            echo "Process $pid is not running"
        fi
    done < "$pid_file"
    
    # Check resource usage
    echo -e "\nResource usage summary:"
    top -b -n 1 | head -15
}

# Function to stop processes
stop_processes() {
    echo "Stopping background processes..."
    
    if [[ ! -f "$pid_file" ]]; then
        echo "PID file not found. No processes to stop."
        return 1
    fi
    
    while read -r pid; do
        if ps -p "$pid" > /dev/null; then
            echo "Stopping process $pid"
            kill "$pid"
            # Wait a bit and check if process is still running
            sleep 1
            if ps -p "$pid" > /dev/null; then
                echo "Process $pid is still running, forcing kill..."
                kill -9 "$pid"
            fi
        else
            echo "Process $pid is not running"
        fi
    done < "$pid_file"
    
    # Remove PID file
    rm "$pid_file"
    echo "All processes stopped and PID file removed"
}

# Main script execution
case "${1:-help}" in
    start)
        start_processes
        ;;
    status)
        check_status
        ;;
    stop)
        stop_processes
        ;;
    *)
        show_help
        ;;
esac
```

## Bonus Challenge: Advanced Script Analysis Tool

### Solution:

```bash
#!/bin/bash

# Script analysis tool
# Analyzes shell scripts for common issues and provides recommendations

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if a script file is provided
if [[ $# -eq 0 ]]; then
    echo -e "${RED}Error: No script file provided${NC}"
    echo "Usage: $0 <script_file>"
    exit 1
fi

SCRIPT_FILE=$1

# Check if the file exists
if [[ ! -f "$SCRIPT_FILE" ]]; then
    echo -e "${RED}Error: File not found: $SCRIPT_FILE${NC}"
    exit 1
fi

# Check if the file is a shell script
if [[ ! $(head -n1 "$SCRIPT_FILE") =~ ^#!.*sh ]]; then
    echo -e "${YELLOW}Warning: File does not have a shell script shebang line${NC}"
fi

echo -e "${BLUE}=== Shell Script Analysis: $SCRIPT_FILE ===${NC}"

# Function to check script size
check_size() {
    local size=$(wc -l < "$SCRIPT_FILE")
    echo -e "\n${BLUE}Script Size:${NC}"
    echo "Total lines: $size"
    
    if [[ $size -gt 300 ]]; then
        echo -e "${YELLOW}Warning: Script is quite large ($size lines). Consider breaking it into smaller modules.${NC}"
    elif [[ $size -lt 10 ]]; then
        echo -e "${YELLOW}Note: Script is very small. Make sure it's complete.${NC}"
    else
        echo -e "${GREEN}Size seems reasonable.${NC}"
    fi
}

# Function to check for error handling
check_error_handling() {
    echo -e "\n${BLUE}Error Handling:${NC}"
    
    if grep -q "set -e" "$SCRIPT_FILE"; then
        echo -e "${GREEN}✓ Script uses 'set -e' (exit on error)${NC}"
    else
        echo -e "${YELLOW}× No 'set -e' found. Consider adding to exit on error.${NC}"
    fi
    
    if grep -q "set -u" "$SCRIPT_FILE"; then
        echo -e "${GREEN}✓ Script uses 'set -u' (treat unset variables as errors)${NC}"
    else
        echo -e "${YELLOW}× No 'set -u' found. Consider adding to catch undefined variables.${NC}"
    fi
    
    if grep -q "trap.*EXIT" "$SCRIPT_FILE"; then
        echo -e "${GREEN}✓ Script uses trap for cleanup on exit${NC}"
    else
        echo -e "${YELLOW}× No trap EXIT handler found. Consider adding for proper cleanup.${NC}"
    fi
    
    error_checks=$(grep -c "if \[\[ .*\$?.*!= 0" "$SCRIPT_FILE")
    if [[ $error_checks -gt 0 ]]; then
        echo -e "${GREEN}✓ Script checks command exit status ($error_checks checks found)${NC}"
    else
        echo -e "${YELLOW}× No explicit command exit status checks found.${NC}"
    fi
}

# Function to check variables and quoting
check_variables() {
    echo -e "\n${BLUE}Variables and Quoting:${NC}"
    
    unquoted=$(grep -E '\$[A-Za-z0-9_]+[^"]' "$SCRIPT_FILE" | grep -v '\${\w\+}' | wc -l)
    if [[ $unquoted -gt 0 ]]; then
        echo -e "${YELLOW}× Found approximately $unquoted potentially unquoted variables.${NC}"
        echo "Example lines:"
        grep -E '\$[A-Za-z0-9_]+[^"]' "$SCRIPT_FILE" | grep -v '\${\w\+}' | head -3
    else
        echo -e "${GREEN}✓ No obvious unquoted variables found.${NC}"
    fi
    
    if grep -q '#!/bin/bash' "$SCRIPT_FILE" && grep -q '\[\[ ' "$SCRIPT_FILE"; then
        echo -e "${GREEN}✓ Script uses [[ ]] for tests (more robust than [ ])${NC}"
    elif grep -q '#!/bin/sh' "$SCRIPT_FILE" && grep -q '\[ ' "$SCRIPT_FILE"; then
        echo -e "${GREEN}✓ Script uses [ ] for tests (appropriate for /bin/sh)${NC}"
    fi
}

# Function to check for functions
check_functions() {
    echo -e "\n${BLUE}Functions:${NC}"
    
    func_count=$(grep -c "^[[:space:]]*function[[:space:]]\+.*[[:space:]]*{" "$SCRIPT_FILE")
    func_count2=$(grep -c "^[[:space:]]*[a-zA-Z0-9_]\+[[:space:]]*()[[:space:]]*{" "$SCRIPT_FILE")
    total_funcs=$((func_count + func_count2))
    
    if [[ $total_funcs -eq 0 ]]; then
        echo -e "${YELLOW}× No functions found. Consider structuring code into functions.${NC}"
    else
        echo -e "${GREEN}✓ Script defines $total_funcs functions${NC}"
        
        # Check for local variables
        local_vars=$(grep -c "^[[:space:]]*local[[:space:]]\+" "$SCRIPT_FILE")
        if [[ $local_vars -eq 0 && $total_funcs -gt 0 ]]; then
            echo -e "${YELLOW}× No local variables found. Consider using 'local' in functions.${NC}"
        elif [[ $local_vars -gt 0 ]]; then
            echo -e "${GREEN}✓ Script uses local variables in functions${NC}"
        fi
    fi
}

# Function to check for shellcheck issues
check_shellcheck() {
    echo -e "\n${BLUE}ShellCheck Analysis:${NC}"
    
    if command -v shellcheck >/dev/null 2>&1; then
        echo "Running ShellCheck..."
        shellcheck_output=$(shellcheck "$SCRIPT_FILE" 2>&1)
        shellcheck_status=$?
        
        if [[ $shellcheck_status -eq 0 ]]; then
            echo -e "${GREEN}✓ No ShellCheck issues found${NC}"
        else
            error_count=$(echo "$shellcheck_output" | grep -c "^In .* line .*:")
            echo -e "${YELLOW}× ShellCheck found $error_count issues${NC}"
            echo "$shellcheck_output" | head -10
            if [[ $(echo "$shellcheck_output" | wc -l) -gt 10 ]]; then
                echo "... (more issues not shown)"
            fi
        fi
    else
        echo -e "${YELLOW}ShellCheck not installed. Install it for more detailed analysis.${NC}"
    fi
}

# Function to provide recommendations
provide_recommendations() {
    echo -e "\n${BLUE}Recommendations:${NC}"
    
    # Create a list of recommendations based on findings
    recommendations=()
    
    # Check for comments
    comment_count=$(grep -c "^[[:space:]]*#" "$SCRIPT_FILE")
    lines=$(wc -l < "$SCRIPT_FILE")
    comment_ratio=$(( comment_count * 100 / lines ))
    
    if [[ $comment_ratio -lt 10 && $lines -gt 50 ]]; then
        recommendations+=("Add more comments to explain complex sections of the script")
    fi
    
    # Check for help/usage function
    if ! grep -q "usage\(\)|show_help\(\)|--help" "$SCRIPT_FILE"; then
        recommendations+=("Add a usage/help function to display script usage information")
    fi
    
    # Check for version information
    if ! grep -q "VERSION=|version=|--version" "$SCRIPT_FILE"; then
        recommendations+=("Add version information to the script")
    fi
    
    # Check for logging
    if ! grep -q "log_|logger|logging" "$SCRIPT_FILE"; then
        recommendations+=("Consider adding a logging mechanism for better troubleshooting")
    fi
    
    # Check for configuration handling
    if ! grep -q "config|conf|settings|\.cfg|\.conf" "$SCRIPT_FILE"; then
        recommendations+=("Consider using a separate configuration file for better maintainability")
    fi
    
    # Display recommendations
    if [[ ${#recommendations[@]} -eq 0 ]]; then
        echo -e "${GREEN}No specific recommendations at this time.${NC}"
    else
        for i in "${!recommendations[@]}"; do
            echo -e "${YELLOW}$((i+1)). ${recommendations[$i]}${NC}"
        done
    fi
}

# Run all checks
check_size
check_error_handling
check_variables
check_functions
check_shellcheck
provide_recommendations

echo -e "\n${BLUE}=== Analysis Complete ===${NC}"
```

## Cleanup

### Solution:

```bash
#!/bin/bash

# Find and remove all script files created during the exercises
echo "Cleaning up script files..."

# Remove the function script
if [[ -f "advanced_functions.sh" ]]; then
    rm advanced_functions.sh
    echo "Removed advanced_functions.sh"
fi

# Remove argument handling script
if [[ -f "argument_handler.sh" ]]; then
    rm argument_handler.sh
    echo "Removed argument_handler.sh"
fi

# Remove error handling script
if [[ -f "error_handling_demo.sh" ]]; then
    rm error_handling_demo.sh
    echo "Removed error_handling_demo.sh"
fi

# Remove text processing script
if [[ -f "text_processor.sh" ]]; then
    rm text_processor.sh
    echo "Removed text_processor.sh"
fi

# Remove process management script
if [[ -f "process_manager.sh" ]]; then
    rm process_manager.sh
    echo "Removed process_manager.sh"
fi

# Remove script analyzer
if [[ -f "script_analyzer.sh" ]]; then
    rm script_analyzer.sh
    echo "Removed script_analyzer.sh"
fi

# Remove any log files
rm -f error_handling_demo.log background_processes.pid

# Remove any temporary files created
rm -f /tmp/temp_file /tmp/task_status sample_data.txt

echo "Cleanup complete!"
```

Remember, these solutions are provided for reference. It's best to first try solving the exercises on your own to get the most benefit from the learning experience. 