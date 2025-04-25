# LAB03 - File Editing and Management

In this lab, you’ll learn how to **create, view, edit, and manage files** in a Linux system. These operations are core to using Linux effectively and form the backbone of scripting and automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and delete files
- Use `nano`, `vim`, and `cat` to view and edit files
- Copy, move, and rename files and directories

---

## 🧰 Prerequisites

- Completion of LAB02 - Users and Permissions
- A Linux terminal

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `touch filename` | Create an empty file |
| `nano filename` | Edit a file using nano (easier) |
| `vim filename` | Edit a file using vim (advanced) |
| `cat filename` | Display file contents |
| `cp source target` | Copy files or directories |
| `mv source target` | Move or rename files or directories |
| `rm filename` | Delete a file |
| `rm -r foldername` | Recursively delete a directory |

---

## 🚀 Getting Started

### 1. Create and view a file:
```bash
touch testfile.txt
nano testfile.txt
# Type something, then save and exit (CTRL+O, ENTER, CTRL+X)

cat testfile.txt
```

### 2. Copy and rename the file:
```bash
cp testfile.txt backup.txt
mv backup.txt final.txt
```

### 3. Move the file into a new folder:
```bash
mkdir testdir
mv final.txt testdir/
ls testdir
```

### 4. Remove files and directories:
```bash
rm testfile.txt
rm -r testdir
```

---

## ✅ Validation Checklist

- [ ] File successfully created and edited
- [ ] File copied, renamed, and moved
- [ ] File and directory cleanup performed

---

## 🧹 Cleanup
```bash
rm -f testfile.txt
rm -rf testdir
```

---

## 🧠 Key Concepts

- Use `nano` for beginner-friendly file editing
- `vim` is powerful but has a learning curve
- `cat`, `cp`, `mv`, and `rm` are essential for daily file operations

---

## 🔁 What's Next?
Continue to [LAB04 - File Searching and Archiving](../LAB04-File-Searching-And-Archiving/README.md) to learn how to locate files and manage archives.