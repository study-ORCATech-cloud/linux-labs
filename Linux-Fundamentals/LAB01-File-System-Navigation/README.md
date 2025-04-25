# LAB01 - File System Navigation

Welcome to your first Linux lab! 🐧

This lab will teach you how to **navigate the Linux file system** using essential commands. Mastering these basics is critical for all further Linux work.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand absolute vs relative paths
- Use basic navigation commands (`pwd`, `cd`, `ls`)
- Create, explore, and remove directories

---

## 🧰 Prerequisites

- Access to a Linux terminal (Ubuntu/Debian preferred)
- Basic familiarity with opening a terminal session

---

## 🗂️ Folder Structure Example

```bash
/home/ubuntu/
├── Documents/
├── Downloads/
├── Projects/
└── linux-labs/
```

---

## 🚀 Getting Started

### 1. Open your terminal.

### 2. Practice navigation:
```bash
# Show your current directory
pwd

# List the contents of the current directory
ls

# Move into a system folder
cd /home

# Move into your user folder (example: ubuntu)
cd ubuntu

# List contents in long format
ls -la
```

### 3. Create and move into a directory:
```bash
mkdir test-navigation
cd test-navigation
```

### 4. Move up one directory:
```bash
cd ..

# Confirm your location
pwd
```

---

## ✅ Validation Checklist

- [ ] Successfully moved into and out of multiple folders
- [ ] Used `pwd` to confirm current location
- [ ] Created and removed a test directory

---

## 🧹 Cleanup

After practicing:
```bash
rmdir test-navigation
```

---

## 🧠 Key Concepts

- **pwd**: Print the current working directory
- **cd**: Change directory (navigate)
- **ls**: List the contents of a directory
- **mkdir**: Create a new directory
- **rmdir**: Remove an empty directory

Paths can be:
- **Absolute** (starting from `/`, like `/home/ubuntu`)
- **Relative** (starting from your current position, like `../Documents`)

---

## 🔁 What's Next?
Continue to [LAB02 - Users and Permissions](../LAB02-Users-And-Permissions/README.md) to learn how Linux manages user accounts and file access!

