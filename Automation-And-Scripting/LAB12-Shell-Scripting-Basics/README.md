# LAB12 - Shell Scripting Basics

In this lab, you'll learn how to **write basic bash shell scripts** to automate repetitive tasks — a critical skill for any Linux power user or DevOps engineer.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and execute basic shell scripts
- Work with variables, input/output, and command-line arguments
- Implement conditional statements and loops
- Define and use functions in shell scripts
- Create practical scripts for file operations
- Apply debugging and error handling techniques

---

## 🧰 Prerequisites

- Completion of LAB11 - Scheduling Tasks with Cron and At
- A Linux terminal with text editing capabilities (`nano`, `vim`)

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `chmod +x script.sh` | Make a script executable |
| `./script.sh` | Run a script in the current directory |
| `bash script.sh` | Run a script with bash (no execute permission needed) |
| `echo $VAR` | Print a variable's value |
| `read VAR` | Read user input into a variable |
| `if [ condition ]; then` | Start a conditional block |
| `for item in list; do` | Start a for loop |
| `function_name() { commands; }` | Define a function |

---

## 🚀 Getting Started

### 1. Create your first script:
```bash
# Create a new script file
nano hello_world.sh
```

Add this content:
```bash
#!/bin/bash

# My first bash script
echo "Hello, World!"
```

Make it executable and run it:
```bash
chmod +x hello_world.sh
./hello_world.sh
```

### 2. Use variables and user input:
```bash
# Create another script
nano greeting.sh
```

Add this content:
```bash
#!/bin/bash

# Script with variables and user input
NAME="Linux Student"
echo "Hello, $NAME!"

echo "What's your name?"
read USER_NAME
echo "Nice to meet you, $USER_NAME!"
```

Make it executable and run it:
```bash
chmod +x greeting.sh
./greeting.sh
```

### 3. Add conditionals:
```bash
# Create a script with conditions
nano check_number.sh
```

Add this content:
```bash
#!/bin/bash

# Conditional script
echo "Enter a number:"
read NUMBER

if [ "$NUMBER" -gt 0 ]; then
  echo "You entered a positive number."
elif [ "$NUMBER" -lt 0 ]; then
  echo "You entered a negative number."
else
  echo "You entered zero."
fi
```

Make it executable and run it:
```bash
chmod +x check_number.sh
./check_number.sh
```

### 4. Create a loop:
```bash
# Create a script with a loop
nano count.sh
```

Add this content:
```bash
#!/bin/bash

# Loop script
echo "Counting from 1 to 5:"
for i in 1 2 3 4 5; do
  echo "Number: $i"
done
```

Make it executable and run it:
```bash
chmod +x count.sh
./count.sh
```

---

## ✅ Validation Checklist

- [ ] Created and executed a Hello World script
- [ ] Created a script using variables and user input
- [ ] Written a script with conditional statements
- [ ] Implemented a script with loops
- [ ] (Optional) Created a script with functions

---

## 🧹 Cleanup
```bash
# Remove the scripts created in this exercise
rm hello_world.sh greeting.sh check_number.sh count.sh
```

---

## 🧠 Key Concepts

- Scripts start with a **shebang** line (`#!/bin/bash`) to specify the interpreter
- Variables store data that can be reused throughout your script
- Conditions (`if`, `elif`, `else`) let scripts make decisions
- Loops (`for`, `while`) let scripts repeat actions
- Functions group related commands for better organization

---

## 🔁 What's Next?
Continue to [LAB13 - Advanced Shell Scripting](../LAB13-Advanced-Shell-Scripting/README.md) to learn more advanced scripting techniques, including functions, error handling, and script debugging!

