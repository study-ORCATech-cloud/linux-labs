# LAB11 - Scheduling Tasks with Cron and At

In this lab, you'll learn how to **schedule recurring or one-time tasks** on a Linux system using `cron` and `at` — key tools for automation and maintenance.

---

## 🎯 Objectives

By the end of this lab, you will:
- Schedule recurring jobs with `cron`
- Schedule one-time jobs with `at`
- Manage and view scheduled tasks

---

## 🧰 Prerequisites

- Completion of LAB10 - Device and Disk Management
- A Linux terminal with `cron` and `at` services available

> 🛠️ If needed, install `at`:
```bash
sudo apt install at
sudo systemctl start atd
sudo systemctl enable atd
```

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `crontab -e` | Edit user’s crontab (scheduler) |
| `crontab -l` | List scheduled cron jobs |
| `crontab -r` | Remove all cron jobs for user |
| `at time` | Schedule a one-time task |
| `atq` | View pending `at` jobs |
| `atrm jobnumber` | Remove a pending `at` job |

---

## 🚀 Getting Started

### 1. Create a recurring job using `cron`:
```bash
# Open your personal crontab editor
crontab -e
```
Add this line to run a simple task every minute:
```bash
* * * * * echo "Cron job executed at $(date)" >> ~/cron_test.log
```
Save and exit.

View scheduled jobs:
```bash
crontab -l
```

Check the log after a few minutes:
```bash
cat ~/cron_test.log
```

### 2. Create a one-time job using `at`:
```bash
# Schedule a job 2 minutes from now
at now + 2 minutes
```
Inside the prompt, type:
```bash
echo "At job executed at $(date)" >> ~/at_test.log
CTRL+D
```

View pending jobs:
```bash
atq
```

Check the log after 2–3 minutes:
```bash
cat ~/at_test.log
```

---

## ✅ Validation Checklist

- [ ] Created a recurring job with `cron`
- [ ] Created a one-time job with `at`
- [ ] Verified logs for successful execution

---

## 🧹 Cleanup

Remove the test cron job:
```bash
crontab -r
```

Remove the test files:
```bash
rm ~/cron_test.log ~/at_test.log
```

---

## 🧠 Key Concepts

- `cron` is ideal for recurring, periodic tasks
- `at` is perfect for one-off, scheduled tasks
- Automation reduces manual workload and improves reliability

---

## 🔁 What's Next?
Continue to [LAB12 - Shell Scripting Basics](../LAB12-Shell-Scripting-Basics/README.md) to start writing powerful bash scripts to automate even more tasks!

