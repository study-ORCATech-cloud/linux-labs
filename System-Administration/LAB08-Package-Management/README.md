# LAB08 - Package Management

In this lab, you’ll learn how to **install, update, and manage software packages** on a Linux system using package managers like `apt` and `yum`.

---

## 🎯 Objectives

By the end of this lab, you will:
- Install new software packages
- Update existing packages and system dependencies
- Remove unwanted packages cleanly
- Understand repositories and package management basics

---

## 🧰 Prerequisites

- Completion of LAB07 - Networking Basics
- A Linux terminal with internet access

---

## 🗂️ Key Commands Cheat Sheet

| Command (Ubuntu/Debian) | Purpose |
|-------------------------|---------|
| `sudo apt update` | Update package list |
| `sudo apt upgrade` | Upgrade all upgradable packages |
| `sudo apt install package` | Install a specific package |
| `sudo apt remove package` | Remove a specific package |
| `sudo apt purge package` | Remove package and config files |
| `sudo apt autoremove` | Clean up unnecessary dependencies |

| Command (RHEL/CentOS) | Purpose |
|----------------------|---------|
| `sudo yum update` | Update all packages |
| `sudo yum install package` | Install a package |
| `sudo yum remove package` | Remove a package |

---

## 🚀 Getting Started

### 1. Update the system:
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install a sample package:
```bash
sudo apt install cowsay
```

Test it:
```bash
cowsay "Hello Linux Labs!"
```

### 3. Remove the package:
```bash
sudo apt remove cowsay

# Also clean any leftovers
sudo apt autoremove
```

---

## ✅ Validation Checklist

- [ ] Successfully updated the system package list
- [ ] Installed and ran a test package
- [ ] Removed the package and cleaned dependencies

---

## 🧹 Cleanup

If needed, remove any extra packages:
```bash
sudo apt autoremove
```

---

## 🧠 Key Concepts

- `apt` and `yum` manage software installation on Linux
- Regular updates are important for security and stability
- Cleaning unused packages keeps the system light and secure

---

## 🔁 What's Next?
Continue to [LAB09 - System Startup and Services](../LAB09-System-Startup-And-Services/README.md) to learn how Linux manages services and system boot processes!

