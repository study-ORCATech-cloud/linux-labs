# LAB18 - Troubleshooting Common Issues

In this lab, you'll learn how to **diagnose and resolve typical Linux system problems** such as full disks, memory exhaustion, service failures, and permission issues.

---

## 🎯 Objectives

By the end of this lab, you will:
- Diagnose storage, memory, and CPU-related issues
- Investigate service failures using logs and status commands
- Resolve common permission errors

---

## 🧰 Prerequisites

- Completion of LAB17 - System Performance Monitoring
- Familiarity with basic Linux commands and troubleshooting tools

---

## 🗂️ Troubleshooting Tools Cheat Sheet

| Tool | Purpose |
|------|---------|
| `df -h` | Check disk usage |
| `du -sh *` | Check folder sizes |
| `free -h` | Check memory usage |
| `top` / `htop` | Monitor resource-heavy processes |
| `systemctl status service` | Check service status |
| `journalctl -xe` | Review detailed logs |
| `ls -l` | Check file permissions |

---

## 🚀 Getting Started

### 1. Diagnose Disk Space Issues:
```bash
df -h

# Identify which directories use most space
du -sh /*
```
Look for nearly full partitions.

### 2. Diagnose Memory Issues:
```bash
free -h
top
```
Look for swap usage or processes consuming excess memory.

### 3. Troubleshoot a Failed Service:
```bash
# Example: SSH service
sudo systemctl status ssh

# View service-specific logs
sudo journalctl -u ssh
```

### 4. Resolve Permission Problems:
```bash
# Check permissions
ls -l /path/to/file

# Fix ownership if needed
sudo chown correctuser:correctgroup /path/to/file

# Adjust permissions
sudo chmod 644 /path/to/file
```

---

## ✅ Validation Checklist

- [ ] Diagnosed full disk or memory issues
- [ ] Inspected and resolved a service failure
- [ ] Fixed a file permission problem

---

## 🧹 Cleanup

No cleanup needed — this lab involves diagnosis and minor corrections only.

---

## 🧠 Key Concepts

- Always check disk space and memory usage first when troubleshooting
- Use logs (`journalctl`) and `systemctl` status output to debug service problems
- Correct permissions are vital for file accessibility and security

---

## 🔁 What's Next?
Continue to [LAB19 - Linux Security Basics](../LAB19-Linux-Security-Basics/README.md) to start learning fundamental Linux system hardening and security practices!