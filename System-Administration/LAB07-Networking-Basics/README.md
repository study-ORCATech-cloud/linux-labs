# LAB07 - Networking Basics

In this lab, you’ll explore **essential networking concepts and tools** available in Linux — critical for managing servers, troubleshooting connectivity, and configuring cloud environments.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand IP addresses, DNS, and routing basics
- Check network configurations
- Use basic network diagnostic tools (`ping`, `curl`, etc.)

---

## 🧰 Prerequisites

- Completion of LAB06 - Process and Job Management
- A Linux terminal with internet access

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `ip addr` | View network interfaces and IP addresses |
| `ip route` | View routing table |
| `ping host` | Test connectivity to another host |
| `curl url` | Fetch web content via HTTP |
| `traceroute host` | Show path packets take to a host |
| `nslookup domain` | Query DNS information |
| `netstat -tuln` | Show open ports and listening services |

> If not installed, you can install tools:
```bash
sudo apt install traceroute net-tools dnsutils -y
```

---

## 🚀 Getting Started

### 1. View your network configuration:
```bash
ip addr

ip route
```

### 2. Test basic network connectivity:
```bash
# Ping a public server
ping 8.8.8.8 -c 4

# Ping a domain
ping google.com -c 4
```

### 3. Fetch data from a web server:
```bash
curl https://example.com
```

### 4. Diagnose network paths:
```bash
traceroute google.com
```

### 5. Check DNS resolution:
```bash
nslookup example.com
```

### 6. View listening ports:
```bash
netstat -tuln
```

---

## ✅ Validation Checklist

- [ ] Viewed local IP address and routes
- [ ] Successfully pinged a server and domain
- [ ] Used curl to fetch a webpage
- [ ] Ran a traceroute to diagnose packet paths
- [ ] Performed DNS lookup with nslookup

---

## 🧹 Cleanup

No cleanup is required for this lab.

---

## 🧠 Key Concepts

- `ip` manages network interfaces and routes
- `ping` and `curl` diagnose network reachability
- DNS resolution is critical for internet communication

---

## 🔁 What's Next?
Continue to [LAB08 - Package Management](../LAB08-Package-Management/README.md) to learn how to install and manage software on your Linux system!

