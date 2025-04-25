# LAB09 - System Startup and Services

In this lab, you'll learn how Linux systems **start up** and **manage background services** using `systemd` — a crucial part of understanding system administration.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand the Linux boot and service management system
- List, start, stop, enable, and disable services
- Analyze logs and troubleshoot service issues

---

## 🧰 Prerequisites

- Completion of LAB08 - Package Management
- A Linux system with `systemd` installed (most modern distributions)

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `systemctl` | Manage system services |
| `systemctl status service` | Check the status of a service |
| `systemctl start service` | Start a service manually |
| `systemctl stop service` | Stop a running service |
| `systemctl restart service` | Restart a service |
| `systemctl enable service` | Enable service to start on boot |
| `systemctl disable service` | Disable service from starting on boot |
| `journalctl -xe` | View detailed system and service logs |

---

## 🚀 Getting Started

### 1. Explore current services:
```bash
systemctl list-units --type=service
```

### 2. Check the status of a specific service:
```bash
# Example: Check SSH service
systemctl status ssh
```

### 3. Manage a service:
```bash
# Start SSH service
sudo systemctl start ssh

# Restart it
sudo systemctl restart ssh

# Stop it
sudo systemctl stop ssh
```

### 4. Enable a service to start automatically at boot:
```bash
sudo systemctl enable ssh

# Disable it
sudo systemctl disable ssh
```

### 5. Analyze service logs:
```bash
# View recent system and service logs
journalctl -xe
```

---

## ✅ Validation Checklist

- [ ] Listed active services
- [ ] Checked and controlled a service's state
- [ ] Enabled and disabled a service for boot
- [ ] Viewed service logs

---

## 🧹 Cleanup

No cleanup required — but you can revert any service settings you changed if desired.

---

## 🧠 Key Concepts

- `systemd` is the standard service manager on modern Linux systems
- Services can be manually started, stopped, or set to run automatically
- System logs (`journalctl`) are critical for troubleshooting service failures

---

## 🔁 What's Next?
Continue to [LAB10 - Device and Disk Management](../LAB10-Device-And-Disk-Management/README.md) to learn how Linux handles storage devices and partitions!