# LAB04 - File Searching and Archiving

In this lab, you'll learn how to **find files efficiently** and **manage archives** (compressed files) on a Linux system. These are critical skills for handling large projects, backups, and server maintenance.

---

## 🎯 Objectives

By the end of this lab, you will:
- Search for files and text within files
- Create and extract archive files
- Use compression utilities like `tar`, `gzip`, and `zip`

---

## 🧰 Prerequisites

- Completion of LAB03 - File Editing and Management
- A Linux terminal

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `find` | Search for files by name or type |
| `grep` | Search inside files for specific text |
| `tar -cvf archive.tar files/` | Create a tar archive |
| `tar -xvf archive.tar` | Extract a tar archive |
| `gzip file` | Compress a single file |
| `gunzip file.gz` | Decompress a `.gz` file |
| `zip archive.zip files/` | Create a zip archive |
| `unzip archive.zip` | Extract a zip archive |

---

## 🚀 Getting Started

### 1. Search for files:
```bash
# Find all .txt files in your home directory
find ~ -name "*.txt"

# Find files modified in the last 1 day
find ~ -mtime -1
```

### 2. Search inside files:
```bash
# Search for the word 'hello' inside all .txt files
grep 'hello' *.txt
```

### 3. Create and extract tar archives:
```bash
# Create a tar archive
mkdir archive_test
touch archive_test/file{1..3}.txt
tar -cvf archive.tar archive_test/

# Extract it
tar -xvf archive.tar
```

### 4. Compress and decompress files:
```bash
# Compress
gzip archive_test/file1.txt

# Decompress
gunzip archive_test/file1.txt.gz
```

---

## ✅ Validation Checklist

- [ ] Successfully find files and search inside files
- [ ] Create and extract tar archives
- [ ] Compress and decompress files using gzip

---

## 🧹 Cleanup
```bash
rm -rf archive_test
rm archive.tar
```

---

## 🧠 Key Concepts

- `find` locates files based on name, type, date, etc.
- `grep` searches inside file content
- `tar`, `gzip`, and `zip` are essential for packaging and transferring files

---

## 🔁 What's Next?
Continue to [LAB05 - Basic Shell Commands](../LAB05-Basic-Shell-Commands/README.md) to strengthen your Linux command-line mastery!

