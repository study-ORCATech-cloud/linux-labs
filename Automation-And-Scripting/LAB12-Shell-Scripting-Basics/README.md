# LAB12 - Shell Scripting Basics

In this lab, you'll learn how to **write basic bash shell scripts** to automate repetitive tasks — a critical skill for any Linux power user or DevOps engineer.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and execute simple bash scripts
- Use variables, conditions, and loops
- Understand basic script structure

---

## 🧰 Prerequisites

- Completion of LAB11 - Scheduling Tasks with Cron and At
- A Linux terminal with text editing capabilities (`nano`, `vim`)

---

## 🗂️ Key Bash Concepts Cheat Sheet

| Concept | Example |
|---------|---------|
| Define variable | `NAME="Linux"` |
| Use variable | `echo $NAME` |
| If statement | `if [ condition ]; then ... fi` |
| For loop | `for item in list; do ... done` |
| While loop | `while condition; do ... done` |
| Script shebang | `#!/bin/bash` |

---

## 🚀 Getting Started

### 1. Create your first script:
```bash
nano first_script.sh
```
Paste this content:
```bash
#!/bin/bash

echo "Hello from your first bash script!"
```
Save and exit (`CTRL+O`, `ENTER`, `CTRL+X`).

Make it executable:
```bash
chmod +x first_script.sh

./first_script.sh
```

### 2. Add variables and conditions:
```bash
nano second_script.sh
```
Paste this content:
```bash
#!/bin/bash

NAME="Linux Student"

if [ "$NAME" == "Linux Student" ]; then
  echo "Welcome, $NAME!"
else
  echo "Who are you?"
fi
```
Save, make executable, and run it.

### 3. Create a loop:
```bash
nano loop_script.sh
```
Paste:
```bash
#!/bin/bash

for fruit in apple banana cherry; do
  echo "I like $fruit"
done
```
Make executable and run it.

---

## ✅ Validation Checklist

- [ ] Wrote and executed a simple script
- [ ] Used variables and conditionals
- [ ] Created a basic loop

---

## 🧹 Cleanup
```bash
rm first_script.sh second_script.sh loop_script.sh
```

---

## 🧠 Key Concepts

- Scripts start with a **shebang** (`#!/bin/bash`)
- Variables store reusable data
- Conditions and loops make scripts dynamic and powerful

---

## 🔁 What's Next?
Continue to [LAB13 - Advanced Shell Scripting](../LAB13-Advanced-Shell-Scripting/README.md) to learn about functions, error handling, and more sophisticated scripting techniques!

