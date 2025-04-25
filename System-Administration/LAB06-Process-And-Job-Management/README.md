# LAB06 - Process and Job Management

In this lab, you’ll learn how to **view, control, and manage processes and background jobs** in a Linux system — a vital skill for administration and troubleshooting.

---

## 🎯 Objectives

By the end of this lab, you will:
- List and inspect running processes
- Manage foreground and background jobs
- Kill misbehaving processes
- Adjust process priorities

---

## 🧰 Prerequisites

- Completion of LAB05 - Basic Shell Commands
- A Linux terminal with a few running applications

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `ps aux` | Show all processes |
| `top` or `htop` | Real-time process monitoring |
| `kill PID` | Terminate a process by ID |
| `killall process_name` | Kill all instances of a process |
| `nice -n priority command` | Run a command with a set priority |
| `renice PID` | Change the priority of a running process |
| `jobs` | List background jobs |
| `bg %jobnumber` | Resume a job in background |
| `fg %jobnumber` | Resume a job in foreground |

---

## 🚀 Getting Started

### 1. View running processes:
```bash
ps aux

# Or use a live monitoring tool
top
# (Use q to quit top)
```

### 2. Start and manage background jobs:
```bash
# Start a long-running process
sleep 500 &

# List background jobs
jobs

# Bring a background job to foreground
fg %1

# Move a running job back to background (CTRL+Z then bg)
```

### 3. Kill a process:
```bash
# Find the process ID (PID)
ps aux | grep sleep

# Kill it
kill <PID>

# If stubborn, force kill
kill -9 <PID>
```

### 4. Nice and renice:
```bash
# Start a process with lower priority
nice -n 10 sleep 1000 &

# Change priority of a running process
renice -n 5 -p <PID>
```

---

## ✅ Validation Checklist

- [ ] Listed active processes
- [ ] Started and managed background jobs
- [ ] Killed a process by PID
- [ ] Adjusted process priority

---

## 🧹 Cleanup
```bash
# Kill any remaining sleep processes
killall sleep
```

---

## 🧠 Key Concepts

- Processes are programs running in the system memory
- Jobs are processes started by your shell session
- Priorities (`nice`/`renice`) affect CPU scheduling fairness

---

## 🔁 What's Next?
Continue to [LAB07 - Networking Basics](../LAB07-Networking-Basics/README.md) to learn the essentials of Linux networking and connectivity!