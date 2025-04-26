# Bash Shell Scripting Cheatsheet

## Script Basics

| Concept | Description | Example |
|---------|-------------|---------|
| Shebang | First line of script that specifies the interpreter | `#!/bin/bash` |
| Comments | Lines starting with # are ignored | `# This is a comment` |
| Execution | Make script executable & run it | `chmod +x script.sh` then `./script.sh` |
| Exit codes | Return value of script (0=success) | `exit 0` or `exit 1` |

## Variables

| Concept | Description | Example |
|---------|-------------|---------|
| Assignment | Assign a value to a variable | `NAME="John"` |
| Using variables | Reference a variable with $ | `echo $NAME` or `echo ${NAME}` |
| Command substitution | Store command output in variable | `DIRS=$(ls -la)` or ``FILES=`ls` `` |
| Arithmetic | Perform math operations | `RESULT=$((5 + 3))` |
| Environment variables | System variables | `$HOME`, `$PATH`, `$USER`, `$PWD` |
| Exporting | Make variable available to child processes | `export VARNAME=value` |
| Read-only | Prevent variable from being changed | `readonly VARNAME=value` |
| Local variables | Variables local to functions | `local VARNAME=value` |

## Special Variables

| Variable | Description |
|----------|-------------|
| `$0` | Script name |
| `$1` to `$9` | First 9 command line arguments |
| `${10}` and up | Command line arguments beyond 9 |
| `$#` | Number of command line arguments |
| `$@` | All command line arguments (preserves quoting) |
| `$*` | All command line arguments (as a single word) |
| `$?` | Exit status of the last command |
| `$$` | Process ID of the current script |
| `$!` | Process ID of the last background command |

## String Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| Concatenation | Join strings | `FULL="$FIRST $LAST"` |
| Length | Get string length | `${#STRING}` |
| Substring | Extract part of string | `${STRING:0:5}` (first 5 chars) |
| Replace | Replace text in string | `${STRING/pattern/replacement}` |
| Uppercase | Convert to uppercase | `${STRING^^}` |
| Lowercase | Convert to lowercase | `${STRING,,}` |

## Conditional Statements

### If Statements

```bash
if [ condition ]; then
    # commands
elif [ condition ]; then
    # commands
else
    # commands
fi
```

### Case Statements

```bash
case $VARIABLE in
    pattern1)
        # commands
        ;;
    pattern2)
        # commands
        ;;
    *)
        # default commands
        ;;
esac
```

## Comparison Operators

### File Test Operators

| Operator | Description |
|----------|-------------|
| `-e file` | True if file exists |
| `-f file` | True if file exists and is a regular file |
| `-d file` | True if file exists and is a directory |
| `-r file` | True if file exists and is readable |
| `-w file` | True if file exists and is writable |
| `-x file` | True if file exists and is executable |
| `-s file` | True if file exists and has size greater than zero |

### String Comparison

| Operator | Description |
|----------|-------------|
| `str1 = str2` | True if strings are equal |
| `str1 != str2` | True if strings are not equal |
| `-z str` | True if string is empty |
| `-n str` | True if string is not empty |

### Numeric Comparison

| Operator | Description |
|----------|-------------|
| `num1 -eq num2` | True if numbers are equal |
| `num1 -ne num2` | True if numbers are not equal |
| `num1 -lt num2` | True if num1 < num2 |
| `num1 -le num2` | True if num1 <= num2 |
| `num1 -gt num2` | True if num1 > num2 |
| `num1 -ge num2` | True if num1 >= num2 |

### Logical Operators

| Operator | Description |
|----------|-------------|
| `! expr` | Negation (NOT) |
| `expr1 -a expr2` | Logical AND |
| `expr1 -o expr2` | Logical OR |
| `expr1 && expr2` | Logical AND (short-circuit) |
| `expr1 || expr2` | Logical OR (short-circuit) |

## Loops

### For Loop

```bash
# Basic for loop
for i in 1 2 3 4 5; do
    echo $i
done

# Range-based for loop
for i in {1..5}; do
    echo $i
done

# C-style for loop
for ((i=1; i<=5; i++)); do
    echo $i
done
```

### While Loop

```bash
# While loop
count=1
while [ $count -le 5 ]; do
    echo $count
    ((count++))
done
```

### Until Loop

```bash
# Until loop
count=1
until [ $count -gt 5 ]; do
    echo $count
    ((count++))
done
```

### Loop Control

| Command | Description |
|---------|-------------|
| `break` | Exit the loop immediately |
| `continue` | Skip to the next iteration |

## Functions

### Function Definition and Calling

```bash
# Define a function
function_name() {
    # commands
    return value  # Optional, returns an exit code
}

# Alternative syntax
function function_name {
    # commands
}

# Call a function
function_name
```

### Function Parameters

```bash
function_name() {
    echo "First parameter: $1"
    echo "Second parameter: $2"
    echo "All parameters: $@"
    echo "Number of parameters: $#"
}

function_name arg1 arg2 arg3
```

### Local Variables

```bash
function_name() {
    local var1="Local variable"  # Only accessible within function
    echo $var1
}
```

### Returning Values

```bash
# Return via exit code (0-255 only)
function_name() {
    return 0  # Success
}

# Return via output capture
get_sum() {
    echo $(($1 + $2))  # Output the result
}

sum=$(get_sum 5 3)  # Capture the output
echo "Sum: $sum"
```

## Input and Output

### User Input

```bash
echo "Enter your name:"
read NAME

# Read with prompt
read -p "Enter your age: " AGE

# Read without showing input (for passwords)
read -sp "Enter password: " PASSWORD
echo  # New line after hidden input
```

### Output

```bash
# Standard output
echo "This is standard output"

# Standard error
echo "This is an error message" >&2

# Formatted output
printf "Name: %s, Age: %d\n" "$NAME" "$AGE"
```

### Redirection

| Operator | Description |
|----------|-------------|
| `command > file` | Redirect stdout to file (overwrite) |
| `command >> file` | Redirect stdout to file (append) |
| `command 2> file` | Redirect stderr to file |
| `command &> file` | Redirect both stdout and stderr to file |
| `command < file` | Use file as input for command |
| `command1 \| command2` | Pipe stdout of command1 to stdin of command2 |

## Arrays

### Array Operations

```bash
# Define an array
FRUITS=("Apple" "Banana" "Cherry")

# Access elements
echo ${FRUITS[0]}        # First element
echo ${FRUITS[-1]}       # Last element
echo ${FRUITS[@]}        # All elements
echo ${#FRUITS[@]}       # Number of elements
echo ${!FRUITS[@]}       # All indices

# Modify arrays
FRUITS[1]="Blueberry"    # Change element
FRUITS+=("Dragonfruit")  # Add element
unset FRUITS[2]          # Remove element
```

### Iterating Over Arrays

```bash
for fruit in "${FRUITS[@]}"; do
    echo "Fruit: $fruit"
done

# With index
for i in "${!FRUITS[@]}"; do
    echo "Index $i: ${FRUITS[$i]}"
done
```

## Debugging

### Debugging Options

| Option | Description |
|--------|-------------|
| `set -x` | Print commands before execution |
| `set -e` | Exit if any command fails |
| `set -u` | Treat unset variables as errors |
| `set -o pipefail` | Return value reflects any command failure in pipes |

### Debugging Commands

```bash
# Run with debug mode
bash -x script.sh

# Debug specific parts
set -x  # Start debugging
command1
command2
set +x  # Stop debugging
```

## Error Handling

```bash
# Check exit status
if [ $? -ne 0 ]; then
    echo "Previous command failed"
fi

# Error handling function
handle_error() {
    echo "Error: $1" >&2
    exit 1
}

# Use with || (or)
command || handle_error "Command failed"

# Trap signals
trap 'echo "Script interrupted."; exit 1' INT
```

## Common Bash Commands

| Command | Description | Example |
|---------|-------------|---------|
| `echo` | Display text | `echo "Hello World"` |
| `cd` | Change directory | `cd /path/to/dir` |
| `pwd` | Print working directory | `pwd` |
| `ls` | List files | `ls -la` |
| `cp` | Copy files | `cp file1 file2` |
| `mv` | Move/rename files | `mv file1 file2` |
| `rm` | Remove files | `rm file` |
| `mkdir` | Create directory | `mkdir dir` |
| `rmdir` | Remove empty directory | `rmdir dir` |
| `touch` | Create empty file | `touch file` |
| `cat` | Display file contents | `cat file` |
| `grep` | Search text | `grep pattern file` |
| `sed` | Stream editor | `sed 's/old/new/g' file` |
| `awk` | Text processing | `awk '{print $1}' file` |
| `sort` | Sort lines | `sort file` |
| `uniq` | Remove duplicates | `uniq file` |
| `wc` | Count lines/words/chars | `wc -l file` |
| `find` | Find files | `find . -name "*.txt"` |
| `xargs` | Build command lines | `find . -name "*.txt" | xargs cat` |
| `cut` | Extract columns | `cut -d':' -f1 /etc/passwd` |
| `head` | Show first lines | `head -n 10 file` |
| `tail` | Show last lines | `tail -n 10 file` |

## Best Practices

1. **Always use shebang**: Start scripts with `#!/bin/bash`
2. **Use proper indentation**: Improves readability
3. **Add comments**: Document what your script does
4. **Quote variables**: Use `"$VARIABLE"` to prevent word splitting
5. **Use meaningful variable names**: Self-documenting code
6. **Validate input**: Check arguments and input before processing
7. **Provide useful error messages**: Redirect errors to stderr
8. **Use exit codes**: Return appropriate exit codes
9. **Use functions**: Break complex scripts into functions
10. **Handle errors**: Check return values and implement error handling
11. **Cleanup temporary files**: Use `trap` to ensure cleanup on exit
12. **Test your scripts**: Test with different inputs and edge cases

## Advanced Topics

### Here Documents (Multiline Strings)

```bash
cat << EOF > output.txt
This is a
multiline
text
EOF
```

### Process Substitution

```bash
diff <(sort file1) <(sort file2)
```

### Subshells

```bash
(cd /tmp && ls -la)  # Current directory unchanged
```

### Background Processes

```bash
long_running_command &  # Run in background
wait  # Wait for all background processes
```

### Command Grouping

```bash
# Execute commands in the current shell
{ command1; command2; command3; }

# Execute commands in a subshell
( command1; command2; command3 )
``` 