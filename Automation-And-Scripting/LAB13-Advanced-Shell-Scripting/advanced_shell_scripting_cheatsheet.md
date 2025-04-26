# Advanced Shell Scripting Cheatsheet

## Functions

| Concept | Syntax | Example |
|---------|--------|---------|
| Basic function | `function_name() { commands; }` | `greet() { echo "Hello!"; }` |
| Function with arguments | Use `$1`, `$2`, etc. | `greet() { echo "Hello, $1!"; }` |
| Local variables | `local var_name=value` | `local count=0` |
| Return values (0-255) | `return value` | `return 0  # Success` |
| Return string values | Use `echo` | `echo "Result"` |
| Function call | `function_name arg1 arg2` | `greet "John"` |
| Capture function output | `var=$(function_name)` | `result=$(calculate 5)` |

## Script Arguments

| Concept | Description | Example |
|---------|-------------|---------|
| Number of arguments | `$#` | `if [ $# -eq 0 ]; then echo "No args"; fi` |
| All arguments | `$@` or `$*` | `for arg in "$@"; do echo "$arg"; done` |
| Script name | `$0` | `echo "Script name: $0"` |
| N-th argument | `$N` (where N is 1, 2, etc.) | `echo "First arg: $1"` |
| All args as one string | `$*` | `echo $*` |
| All args as separate strings | `$@` | `echo $@` |
| Processing with getopts | `while getopts "options" var` | See detailed example below |

### Getopts Example
```bash
while getopts ":a:b:c" opt; do
  case $opt in
    a) # Option with argument (-a value)
      ARG_A="$OPTARG"
      ;;
    b) # Option with argument (-b value)
      ARG_B="$OPTARG"
      ;;
    c) # Option without argument (-c)
      FLAG_C=true
      ;;
    \?) # Invalid option
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :) # Option missing required argument
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Shift to non-option arguments
shift $((OPTIND-1))
```

## Error Handling

| Concept | Description | Example |
|---------|-------------|---------|
| Check exit status | `$?` | `if [ $? -ne 0 ]; then echo "Error"; fi` |
| Exit script | `exit N` | `exit 1  # Error exit` |
| Set error options | `set -e`, `set -u`, etc. | `set -e  # Exit on any error` |
| Error redirection | Redirect to stderr | `echo "Error" >&2` |
| Conditional execution | `&&` for success, `||` for failure | `command && echo "Success" || echo "Failed"` |
| Trap commands | React to signals | `trap 'echo "Exiting"; exit' INT TERM EXIT` |

### Common set Options
```bash
set -e  # Exit immediately if a command exits with non-zero status
set -u  # Treat unset variables as an error
set -o pipefail  # Return value is that of last error in pipeline
set -x  # Print commands and arguments as they are executed
```

### Trap Example
```bash
# Clean up on exit
trap 'rm -f "$TEMP_FILE"; echo "Cleanup done"' EXIT

# Handle Ctrl+C
trap 'echo "Script interrupted"; exit 1' INT

# Disable trap
trap - EXIT
```

## Debugging Techniques

| Technique | Description | Example |
|-----------|-------------|---------|
| Enable trace mode | Display commands as executed | `set -x` |
| Disable trace mode | Turn off command display | `set +x` |
| Debug specific section | Enable for specific code | `set -x; commands; set +x` |
| Run script with debug | Debug entire script | `bash -x script.sh` |
| Use debug output | Print debug messages | `echo "DEBUG: value=$var" >&2` |
| Debug variables | Print variable values | `echo "var=$var"` |

## Advanced Text Processing

### AWK
```bash
# Print specific fields
awk '{print $1, $3}' file.txt

# Filter lines based on condition
awk '$3 > 10 {print $1, $3}' file.txt

# Calculate sum
awk '{sum += $1} END {print "Sum:", sum}' file.txt

# Process with custom field separator
awk -F: '{print $1}' /etc/passwd
```

### SED
```bash
# Replace text
sed 's/old/new/g' file.txt

# Delete lines matching pattern
sed '/pattern/d' file.txt

# Print specific lines
sed -n '10,20p' file.txt

# Multiple operations
sed -e 's/old/new/g' -e '/pattern/d' file.txt
```

### GREP
```bash
# Search for pattern
grep "pattern" file.txt

# Case insensitive search
grep -i "pattern" file.txt

# Show line numbers
grep -n "pattern" file.txt

# Show only matching part
grep -o "pattern" file.txt

# Recursive search
grep -r "pattern" directory/
```

## Best Practices

### Code Organization
1. Start with a shebang line: `#!/bin/bash`
2. Include a script description comment
3. Define constants and configuration variables
4. Define functions
5. Main script logic

### Variable Naming
- Use descriptive names: `USER_COUNT` instead of `uc`
- Use uppercase for constants: `MAX_RETRIES=5`
- Use lowercase for variables: `current_date=$(date)`
- Use underscores to separate words: `file_name`

### Error Handling Best Practices
1. Always check return values: `if [ $? -ne 0 ]; then ...`
2. Exit with meaningful codes: `exit 1` for errors
3. Use `set -e` to exit on errors (but be careful)
4. Redirect error messages to stderr: `echo "Error" >&2`
5. Clean up with trap commands

### Input Validation
1. Check if required arguments are provided
2. Validate argument format (e.g., numeric, alphanumeric)
3. Check if files/directories exist before using them
4. Use default values for optional arguments

### Security Best Practices
1. Quote variables to prevent word splitting: `echo "$var"`
2. Use restrictive file permissions: `chmod 700 script.sh`
3. Validate and sanitize user input
4. Be careful with commands that execute strings
5. Use full paths for commands in security-sensitive scripts
6. Set a secure PATH: `PATH="/usr/local/bin:/usr/bin:/bin"`
7. Avoid using `eval` when possible
8. Use read-only for constants: `readonly MAX_ATTEMPTS=5`

## String Manipulation

| Operation | Syntax | Example |
|-----------|--------|---------|
| Substring | `${string:start:length}` | `${var:0:5}` (first 5 chars) |
| Length | `${#string}` | `${#var}` |
| Replace first match | `${string/pattern/replacement}` | `${var/old/new}` |
| Replace all matches | `${string//pattern/replacement}` | `${var//old/new}` |
| Remove prefix | `${string#pattern}` | `${path#*/}` |
| Remove longest prefix | `${string##pattern}` | `${path##*/}` |
| Remove suffix | `${string%pattern}` | `${file%.*}` |
| Remove longest suffix | `${string%%pattern}` | `${file%%.*}` |
| Uppercase | `${string^^}` | `${var^^}` |
| Lowercase | `${string,,}` | `${var,,}` |

## Array Operations

```bash
# Create an array
array=("one" "two" "three")

# Access elements
echo "${array[0]}"      # First element
echo "${array[-1]}"     # Last element
echo "${array[@]}"      # All elements
echo "${#array[@]}"     # Number of elements

# Iterate over array
for item in "${array[@]}"; do
  echo "$item"
done

# Iterate with index
for i in "${!array[@]}"; do
  echo "Index $i: ${array[$i]}"
done

# Add element
array+=("four")

# Remove element
unset array[1]

# Slice array
echo "${array[@]:1:2}"  # Elements 1 and 2
```

## Process Management

```bash
# Run command in background
command &

# Get PID of last background command
echo $!

# Wait for background processes
wait

# Wait for specific PID
wait $PID

# Kill a process
kill $PID

# Send specific signal
kill -SIGTERM $PID

# Run multiple commands in background
(command1; command2) &
```

## Here Documents and Here Strings

```bash
# Here document (multi-line input)
cat << EOF > file.txt
Line 1
Line 2
Line 3
EOF

# Here document with variable substitution disabled
cat << 'EOF' > file.txt
$VAR will not be substituted
EOF

# Here string (single-line input)
grep "pattern" <<< "input string"
``` 