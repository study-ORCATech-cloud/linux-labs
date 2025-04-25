# LAB13 - Advanced Shell Scripting

In this lab, you'll build on your basic scripting skills and dive into **advanced bash scripting concepts** such as functions, script arguments, error handling, and best practices.

---

## 🎯 Objectives

By the end of this lab, you will:
- Write reusable functions in bash
- Handle script arguments dynamically
- Implement basic error handling
- Understand good scripting practices

---

## 🧰 Prerequisites

- Completion of LAB12 - Shell Scripting Basics
- A Linux terminal with a text editor

---

## 🗂️ Key Bash Concepts Cheat Sheet

| Concept | Example |
|---------|---------|
| Define a function | `my_func() { commands; }` |
| Access arguments | `$1`, `$2`, `$@` |
| Check exit status | `$?` |
| Exit script manually | `exit 1` |
| Trap signals | `trap 'commands' SIGNALS` |

---

## 🚀 Getting Started

### 1. Create a script using functions:
```bash
nano advanced_script.sh
```
Paste this content:
```bash
#!/bin/bash

greet_user() {
  echo "Hello, $1!"
}

# Main execution
USER_NAME=$1

if [ -z "$USER_NAME" ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

greet_user "$USER_NAME"
```
Save and exit, then make it executable:
```bash
chmod +x advanced_script.sh

./advanced_script.sh LinuxStudent
```

### 2. Add error handling:
Modify `advanced_script.sh` to include:
```bash
mkdir /root/testfolder 2>/dev/null

if [ $? -ne 0 ]; then
  echo "Failed to create folder. Permission denied or invalid path."
fi
```

### 3. (Optional) Trap a signal (advanced):
```bash
trap 'echo "Script interrupted!"; exit 1' INT

# Simulate a long-running task
sleep 30
```

Run it, and press `CTRL+C` to trigger the trap.

---

## ✅ Validation Checklist

- [ ] Created and used a bash function
- [ ] Handled user input and script arguments
- [ ] Implemented basic error handling
- [ ] (Optional) Added a signal trap

---

## 🧹 Cleanup
```bash
rm advanced_script.sh
```

---

## 🧠 Key Concepts

- Functions promote reusable, modular code
- Always validate input arguments for robustness
- Traps help catch interruptions and errors gracefully

---

## 🔁 What's Next?
Continue to [LAB14 - Environment Variables and Profiles](../LAB14-Environment-Variables-And-Profiles/README.md) to learn how Linux manages runtime environments!

