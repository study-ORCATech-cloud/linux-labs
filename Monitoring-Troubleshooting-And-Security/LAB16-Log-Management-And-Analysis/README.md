# LAB16 - Log Management and Analysis

In this lab, you'll learn how to **analyze, manage, and troubleshoot system logs** — critical for maintaining healthy Linux systems.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand the Linux logging system and important log files
- Use tools to read and search logs
- Configure basic log rotation

---

## 🧰 Prerequisites

- Completion of LAB15 - Automated User and File Management
- A Linux system with `sudo` access

---

## 🗂️ Key Concepts Cheat Sheet

| Concept | Example |
|---------|---------|
| View syslog | `cat /var/log/syslog` (Ubuntu) |
| View systemd logs | `journalctl` |
| Follow live logs | `tail -f /var/log/syslog` |
| Search logs | `grep 'error' /var/log/syslog` |
| Rotate logs manually | `logrotate` (advanced)

> ⚙️ Note: Log locations may vary slightly by distribution (e.g., `/var/log/messages` on CentOS).

---

## 🚀 Getting Started

### 1. View system logs:
```bash
# View general system logs (Ubuntu)
sudo less /var/log/syslog

# View systemd-managed logs
sudo journalctl
```

### 2. Search for keywords in logs:
```bash
# Find lines containing 'error'
grep -i 'error' /var/log/syslog
```

### 3. Monitor logs live:
```bash
# Watch logs update in real-time
tail -f /var/log/syslog
```
(Press `CTRL+C` to stop.)

### 4. View rotated logs:
```bash
ls -lh /var/log/
```
Look for rotated logs like `syslog.1`, `syslog.2.gz`.

---

## ✅ Validation Checklist

- [ ] Viewed live and static system logs
- [ ] Searched for specific events inside log files
- [ ] Located rotated/compressed old logs

---

## 🧹 Cleanup

No cleanup needed — reading logs doesn't modify anything.

---

## 🧠 Key Concepts

- Linux logs are centralized in `/var/log/`
- `journalctl` provides powerful log filtering options
- Monitoring and analyzing logs is key for troubleshooting

---

## 🔁 What's Next?
Continue to [LAB17 - System Performance Monitoring](../LAB17-System-Performance-Monitoring/README.md) to learn how to track CPU, memory, and disk usage in real-time!