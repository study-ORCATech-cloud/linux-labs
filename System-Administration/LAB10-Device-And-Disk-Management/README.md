# LAB10 - Device and Disk Management

In this lab, you'll learn how Linux systems **detect, mount, partition, and manage storage devices** — a fundamental skill for server administration, troubleshooting, and cloud operations.

---

## 🎯 Objectives

By the end of this lab, you will:
- List available block devices
- Mount and unmount disks manually
- Format partitions and filesystems
- Understand basic disk and partitioning tools

---

## 🧰 Prerequisites

- Completion of LAB09 - System Startup and Services
- A Linux terminal (preferably with an extra disk or test volume attached)

> ⚠️ **Important:** Always be careful when modifying partitions on a real system.

---

## 🗂️ Key Commands Cheat Sheet

| Command | Purpose |
|---------|---------|
| `lsblk` | List block devices (disks, partitions) |
| `df -h` | Show mounted filesystems and disk usage |
| `mount device mountpoint` | Mount a filesystem manually |
| `umount mountpoint` | Unmount a filesystem |
| `mkfs.ext4 device` | Create an ext4 filesystem |
| `fdisk device` | Partition a disk (interactive tool) |
| `parted device` | Alternative partition manager |

---

## 🚀 Getting Started

### 1. List available disks:
```bash
lsblk
```

### 2. View mounted filesystems:
```bash
df -h
```

### 3. Mount an external device:
```bash
# Example: mount /dev/sdb1 to /mnt/testmount
sudo mkdir /mnt/testmount
sudo mount /dev/sdb1 /mnt/testmount

# Verify
df -h
```

### 4. Unmount the device:
```bash
sudo umount /mnt/testmount
```

### 5. Format a device with ext4 filesystem (⚠️ Be very careful):
```bash
sudo mkfs.ext4 /dev/sdb1
```

> Replace `/dev/sdb1` with the correct test device on your system.

### 6. Basic partitioning (optional advanced):
```bash
sudo fdisk /dev/sdb
# (Use 'm' for help inside fdisk)
```

---

## ✅ Validation Checklist

- [ ] Listed block devices and partitions
- [ ] Mounted and unmounted a device
- [ ] (Optional) Formatted a device safely

---

## 🧹 Cleanup
```bash
sudo umount /mnt/testmount
sudo rmdir /mnt/testmount
```

---

## 🧠 Key Concepts

- `lsblk` shows disks, partitions, and mount points
- `mount`/`umount` attaches or detaches storage devices
- Partitioning and formatting prepare disks for usage

---

## 🔁 What's Next?
Congratulations! You've completed the **Linux Fundamentals** and **System Administration** tracks. 🚀

Continue to [LAB11 - Scheduling Tasks With Cron At](../../Automation-And-Scripting/LAB11-Scheduling-Tasks-With-Cron-At/README.md) to learn how to schedule Linux tasks with Cron At!