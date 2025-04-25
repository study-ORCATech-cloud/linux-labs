# LAB02 - Users and Permissions

In this lab, you’ll learn how to **manage users, groups, and permissions** in a Linux system. Controlling access is critical for system security and daily operations.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and delete users and groups
- Modify user passwords and group membership
- Understand and change file permissions

---

## 🧰 Prerequisites

- Completion of LAB01 - File System Navigation
- A Linux terminal with `sudo` privileges

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `useradd username` | Add a new user |
| `passwd username` | Set or change user password |
| `groupadd groupname` | Add a new group |
| `usermod -aG groupname username` | Add user to a group |
| `chmod permissions file` | Change file permissions |
| `chown owner:group file` | Change file ownership |
| `ls -l` | List files with permissions |

---

## 🚀 Getting Started

### 1. Create a new user:
```bash
sudo useradd devuser
sudo passwd devuser
```

### 2. Create a new group and add the user:
```bash
sudo groupadd devgroup
sudo usermod -aG devgroup devuser
```

### 3. Check group membership:
```bash
groups devuser
```

### 4. File permissions exercise:
```bash
# Create a file
sudo touch /tmp/testfile

# Set specific permissions (read/write owner only)
sudo chmod 600 /tmp/testfile

# Change owner to devuser
sudo chown devuser:devgroup /tmp/testfile

# Verify changes
ls -l /tmp/testfile
```

---

## ✅ Validation Checklist

- [ ] New user created successfully
- [ ] New group created and user added
- [ ] File created, permissions set, and ownership changed

---

## 🧹 Cleanup

Remove the test user, group, and file:
```bash
sudo userdel devuser
sudo groupdel devgroup
sudo rm /tmp/testfile
```

---

## 🧠 Key Concepts

- Users and groups manage system access
- Permissions define who can read, write, or execute files
- Ownership determines user and group control of files

---

## 🔁 What's Next?
Continue to [LAB03 - File Editing and Management](../LAB03-File-Editing-And-Management/README.md) to work with file creation, editing, and manipulation!