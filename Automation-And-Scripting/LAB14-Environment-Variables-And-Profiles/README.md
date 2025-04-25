# LAB14 - Environment Variables and Profiles

In this lab, you'll learn how **environment variables and profile files** manage user sessions, system configuration, and runtime behavior in Linux.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how environment variables work
- View, create, and modify environment variables
- Edit user profile scripts like `.bashrc` and `.profile`

---

## 🧰 Prerequisites

- Completion of LAB13 - Advanced Shell Scripting
- Basic familiarity with bash shell and Linux filesystem

---

## 🗂️ Key Concepts Cheat Sheet

| Concept | Example |
|---------|---------|
| View environment | `printenv`, `env` |
| Set temporary variable | `export VAR=value` |
| Set permanent variable | Add `export VAR=value` to `.bashrc` |
| Source a file manually | `source ~/.bashrc` or `. ~/.bashrc` |

---

## 🚀 Getting Started

### 1. View current environment variables:
```bash
env
printenv
printenv PATH
```

### 2. Create a temporary variable:
```bash
export MY_VAR="Hello World"
echo $MY_VAR
```
(Will disappear after closing the session.)

### 3. Make a variable permanent:
```bash
echo 'export MY_VAR="Persistent Hello"' >> ~/.bashrc

# Reload the file
source ~/.bashrc

# Verify
echo $MY_VAR
```

### 4. Customize your shell prompt (optional fun!):
```bash
echo 'export PS1="[MyLinuxLab] \u@\h:\w$ "' >> ~/.bashrc
source ~/.bashrc
```

---

## ✅ Validation Checklist

- [ ] Viewed current environment variables
- [ ] Created and used a temporary environment variable
- [ ] Made a variable persist across sessions
- [ ] Customized shell behavior with `.bashrc`

---

## 🧹 Cleanup
```bash
# Remove test environment lines manually from ~/.bashrc if needed
nano ~/.bashrc
# Delete the lines you added and save
source ~/.bashrc
```

---

## 🧠 Key Concepts

- Environment variables configure your shell and applications
- `.bashrc` and `.profile` load automatically when you start a session
- `export` makes variables available to subprocesses

---

## 🔁 What's Next?
Continue to [LAB15 - Automated User and File Management](../LAB15-Automated-User-And-File-Management/README.md) to automate common admin tasks using scripts!