# LAB17 - System Performance Monitoring

In this lab, you'll learn how to **monitor system performance** — tracking CPU, memory, disk, and network usage in real time on a Linux system.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use system monitoring tools like `top`, `htop`, and `iotop`
- Analyze CPU, memory, disk I/O, and network activity
- Understand resource bottlenecks and basic troubleshooting

---

## 🧰 Prerequisites

- Completion of LAB16 - Log Management and Analysis
- A Linux system with `sudo` access

> ⚙️ Note: Some tools (like `htop` or `iotop`) may need installation:
```bash
sudo apt install htop iotop -y
```

---

## 🗂️ Key Monitoring Tools Cheat Sheet

| Tool | Purpose |
|------|---------|
| `top` | Monitor CPU, memory, and processes live |
| `htop` | Enhanced top with better UI and controls |
| `iotop` | Monitor disk I/O by process |
| `vmstat` | System performance overview |
| `free -h` | Quick memory usage overview |

---

## 🚀 Getting Started

### 1. Monitor system usage with `top`:
```bash
top
```
- Press `q` to quit.

### 2. Use `htop` for an enhanced view:
```bash
htop
```
- Arrow keys to navigate, `F10` to quit.

### 3. Monitor disk I/O activity with `iotop`:
```bash
sudo iotop
```
- Shows processes doing most I/O.

### 4. Get quick memory and swap usage:
```bash
free -h
```

### 5. Summarize system performance:
```bash
vmstat 2 5
```
- Captures system performance snapshots every 2 seconds, 5 times.

---

## ✅ Validation Checklist

- [ ] Used `top` or `htop` to view live CPU/memory usage
- [ ] Monitored disk I/O with `iotop`
- [ ] Analyzed memory status with `free` and `vmstat`

---

## 🧹 Cleanup

No cleanup needed — these are read-only monitoring tools.

---

## 🧠 Key Concepts

- CPU, memory, and disk I/O bottlenecks impact system performance
- `htop` and `iotop` make it easier to diagnose issues visually
- Proactive monitoring prevents downtime and failures

---

## 🔁 What's Next?
Continue to [LAB18 - Troubleshooting Common Issues](../LAB18-Troubleshooting-Common-Issues/README.md) to practice diagnosing and solving real-world Linux problems!
