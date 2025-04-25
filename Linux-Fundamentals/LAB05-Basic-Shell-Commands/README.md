# LAB05 - Basic Shell Commands

In this lab, you’ll practice **essential Linux shell commands** that are used every day for file handling, text processing, and basic system management.

---

## 🎯 Objectives

By the end of this lab, you will:
- Display and manipulate file contents
- Understand how to sort, filter, and summarize text data
- Use redirection and pipes effectively

---

## 🧰 Prerequisites

- Completion of LAB04 - File Searching and Archiving
- A Linux terminal ready for practice

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `cat filename` | View the content of a file |
| `head filename` | View the first few lines of a file |
| `tail filename` | View the last few lines of a file |
| `cut -d':' -f1 filename` | Cut fields from a file |
| `sort filename` | Sort file contents |
| `uniq filename` | Filter out duplicate lines |
| `wc filename` | Count words, lines, characters |
| `|` | Pipe output from one command to another |

---

## 🚀 Getting Started

### 1. Create a sample file:
```bash
cat > data.txt << EOF
apple
banana
apple
cherry
banana
EOF
```

### 2. View file contents:
```bash
cat data.txt
head data.txt
tail data.txt
```

### 3. Process the file:
```bash
# Sort lines alphabetically
sort data.txt

# Remove duplicates
tsort data.txt | uniq

# Count lines, words, and characters
wc data.txt
```

### 4. Use pipes to chain commands:
```bash
# Sort and then count unique lines
sort data.txt | uniq | wc -l
```

---

## ✅ Validation Checklist

- [ ] Successfully created a sample file
- [ ] Viewed and processed file contents
- [ ] Used pipes to chain multiple commands

---

## 🧹 Cleanup
```bash
rm data.txt
```

---

## 🧠 Key Concepts

- Redirection (`>`, `>>`) and piping (`|`) are powerful Linux features
- Sorting, filtering, and counting are common tasks in shell scripts
- Chaining commands saves time and automates data handling

---

## 🔁 What's Next?
Continue to [LAB06 - Process and Job Management](../../System-Administration/LAB06-Process-And-Job-Management/README.md) to learn how to control system processes and jobs effectively!