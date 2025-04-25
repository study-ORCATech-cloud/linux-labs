# LAB15 - Automated User and File Management

In this lab, you'll write bash scripts to **automate user creation, permission assignment, and file setup** — common administrative tasks in real-world Linux systems.

---

## 🎯 Objectives

By the end of this lab, you will:
- Automate user creation with bash scripts
- Create home directories and set permissions automatically
- Build scalable scripts for system administration

---

## 🧰 Prerequisites

- Completion of LAB14 - Environment Variables and Profiles
- A Linux terminal with `sudo` access

> ⚠️ Important: Be cautious when creating/modifying real users on a production system.

---

## 🗂️ Key Concepts Cheat Sheet

| Command | Purpose |
|---------|---------|
| `useradd username` | Add a new user |
| `passwd username` | Set a password |
| `mkdir /path` | Create directories |
| `chown user:group /path` | Change ownership |
| `chmod permissions /path` | Set directory permissions |

---

## 🚀 Getting Started

### 1. Create the automation script:
```bash
nano user_setup.sh
```
Paste this content:
```bash
#!/bin/bash

# Check if username is passed
if [ -z "$1" ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

USERNAME=$1

# Create user and home directory
sudo useradd -m $USERNAME

# Set password (prompt user)
echo "Please set password for $USERNAME"
sudo passwd $USERNAME

# Set ownership and permissions
sudo chown $USERNAME:$USERNAME /home/$USERNAME
sudo chmod 700 /home/$USERNAME

echo "User $USERNAME created and configured."
```
Save and exit, then make it executable:
```bash
chmod +x user_setup.sh
```

### 2. Run the script:
```bash
./user_setup.sh newstudent
```

### 3. Verify:
```bash
ls -ld /home/newstudent
```

---

## ✅ Validation Checklist

- [ ] Created and executed the user setup script
- [ ] Verified user home directory and permissions

---

## 🧹 Cleanup

To remove the test user:
```bash
sudo userdel -r newstudent
```

Delete the script:
```bash
rm user_setup.sh
```

---

## 🧠 Key Concepts

- Automation saves time and ensures consistency in system setup
- Scripts can safely manage users and permissions when carefully written
- Always validate input parameters for safe scripting

---

## 🔁 What's Next?
You have now completed the **Automation and Scripting** track! 🚀

Next, continue to [Monitoring, Troubleshooting, and Security Labs](../../Monitoring-Troubleshooting-And-Security/README.md) to master system reliability and protection!

