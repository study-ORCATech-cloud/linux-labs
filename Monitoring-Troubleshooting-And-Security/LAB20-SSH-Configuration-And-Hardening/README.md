# LAB20 - SSH Configuration and Hardening

In this lab, you'll learn how to **secure SSH access** — protecting your Linux servers from unauthorized access and brute-force attacks.

---

## 🎯 Objectives

By the end of this lab, you will:
- Configure SSH for key-based authentication
- Disable password-based SSH login
- Harden SSH configurations for better security

---

## 🧰 Prerequisites

- Completion of LAB19 - Linux Security Basics
- A Linux system with `sudo` access
- SSH access or terminal access to the server

> ⚠️ Important: Test all SSH changes carefully to avoid locking yourself out!

---

## 🗂️ Key SSH Hardening Cheat Sheet

| Setting | Purpose |
|---------|---------|
| `PasswordAuthentication no` | Disable password logins |
| `PermitRootLogin no` | Prevent root login via SSH |
| `AllowUsers user1 user2` | Limit SSH access to specific users |
| `Port 2222` | Change default SSH port (optional) |

---

## 🚀 Getting Started

### 1. Set up SSH Key Authentication:
On your local machine:
```bash
ssh-keygen -t rsa -b 4096
```
Copy your public key to the server:
```bash
ssh-copy-id username@server_ip
```
Test SSH login:
```bash
ssh username@server_ip
```

### 2. Harden the SSH configuration:
```bash
sudo nano /etc/ssh/sshd_config
```
Edit the following:
```bash
PermitRootLogin no
PasswordAuthentication no
AllowUsers yourusername
```
(Optional) Change SSH port:
```bash
Port 2222
```
Restart SSH:
```bash
sudo systemctl restart sshd
```

> ✅ Always keep an active session open when restarting SSH to avoid being locked out.

### 3. Verify SSH Hardening:
```bash
ssh username@server_ip -p 2222
```
If you changed the port.

---

## ✅ Validation Checklist

- [ ] SSH keys successfully generated and deployed
- [ ] PasswordAuthentication disabled
- [ ] Root login disabled
- [ ] SSH connection tested and working

---

## 🧹 Cleanup

If testing with a non-standard port (like 2222), remember to:
- Update your firewall rules
- Inform users or automate configuration management

---

## 🧠 Key Concepts

- Key-based authentication is vastly more secure than passwords
- Disabling root login minimizes attack surface
- Restricting SSH access and changing ports adds another security layer

---

## 🎉 Congratulations!
You have completed the **Linux Fundamentals**, **System Administration**, **Automation and Scripting**, and **Monitoring, Troubleshooting, and Security** lab tracks!

You are now much closer to Linux mastery. 🐧💻🚀

