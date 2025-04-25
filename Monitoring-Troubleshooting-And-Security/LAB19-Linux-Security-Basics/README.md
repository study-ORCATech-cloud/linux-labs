# LAB19 - Linux Security Basics

In this lab, you'll learn how to **improve the security of a Linux system** by managing users, permissions, password policies, and basic hardening techniques.

---

## 🎯 Objectives

By the end of this lab, you will:
- Enforce stronger password policies
- Manage user permissions securely
- Disable unnecessary services
- Understand basic system hardening steps

---

## 🧰 Prerequisites

- Completion of LAB18 - Troubleshooting Common Issues
- A Linux system with `sudo` access

---

## 🗂️ Key Security Tools Cheat Sheet

| Tool | Purpose |
|------|---------|
| `passwd` | Change user password |
| `chage` | Manage password aging policies |
| `sudo` | Execute commands with elevated privileges |
| `ufw` | Configure simple firewalls (Ubuntu) |
| `sshd_config` | Secure SSH settings |

---

## 🚀 Getting Started

### 1. Set Stronger Password Policies:
```bash
# Force password change after 90 days
sudo chage -M 90 username

# View password aging information
sudo chage -l username
```

### 2. Remove or lock unnecessary accounts:
```bash
# Lock an unused account
sudo usermod -L olduser

# Remove a user account completely
sudo userdel -r olduser
```

### 3. Harden SSH access:
```bash
sudo nano /etc/ssh/sshd_config
```
Edit or add:
```bash
PermitRootLogin no
PasswordAuthentication no
```
Restart SSH:
```bash
sudo systemctl restart sshd
```

### 4. Enable basic firewall protection (Ubuntu example):
```bash
sudo apt install ufw -y
sudo ufw enable
sudo ufw allow ssh
sudo ufw status
```

---

## ✅ Validation Checklist

- [ ] Password expiration policy set
- [ ] Disabled or removed unnecessary users
- [ ] Hardened SSH configuration
- [ ] Enabled a basic firewall

---

## 🧹 Cleanup

- Review any user changes to avoid accidentally locking yourself out.
- Ensure your SSH settings are tested before closing your current session.

---

## 🧠 Key Concepts

- Regularly updating password policies improves account security
- Limiting SSH access and managing active users reduces risk exposure
- A basic firewall provides a first line of defense

---

## 🔁 What's Next?
Continue to [LAB20 - SSH Configuration and Hardening](../LAB20-SSH-Configuration-And-Hardening/README.md) to learn advanced techniques for securing remote access to your servers!

