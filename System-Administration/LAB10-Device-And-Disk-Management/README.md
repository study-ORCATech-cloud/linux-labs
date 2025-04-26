# LAB10 - Device and Disk Management

In this lab, you'll learn how to **manage storage devices and disks** in Linux — essential skills for maintaining and configuring Linux systems.

---

## 🎯 Objectives

By the end of this lab, you will:
- List and identify storage devices in the system
- Mount and unmount filesystems manually
- Create and manage disk partitions
- Format filesystems (ext4, XFS, etc.)
- Implement Logical Volume Management (LVM)
- Perform basic disk health checks and troubleshooting

---

## 🧰 Prerequisites

- Completion of LAB09 - System Startup and Services
- A Linux terminal (preferably with an extra disk or test volume attached)

> ⚠️ **Important:** Many commands in this lab can permanently delete data if used incorrectly. Always double-check device names and commands before executing them.

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
| `pvcreate`, `vgcreate`, `lvcreate` | LVM management commands |

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

### 6. Basic partitioning:
```bash
sudo fdisk /dev/sdb
# (Use 'm' for help inside fdisk)
```

---

## ✅ Validation Checklist

- [ ] Listed block devices and partitions
- [ ] Mounted and unmounted a device
- [ ] Created a partition (on a safe test device only)
- [ ] Formatted a filesystem (on a safe test device only)
- [ ] Explored disk usage with appropriate commands

---

## 🧹 Cleanup
```bash
# Unmount any test filesystems
sudo umount /mnt/testmount

# Remove test mount points
sudo rmdir /mnt/testmount
```

---

## 🧠 Key Concepts

- Block devices represent physical or virtual storage in Linux
- Partitioning divides disks into manageable sections
- Filesystems (ext4, XFS, etc.) organize data on partitions
- LVM provides flexible logical volume management
- Proper mounting/unmounting prevents data corruption

---

## 🔁 What's Next?
Congratulations! You've completed the **Linux Fundamentals** and **System Administration** tracks. 🚀

Continue to [LAB11 - Scheduling Tasks With Cron At](../../Automation-And-Scripting/LAB11-Scheduling-Tasks-With-Cron-At/README.md) to begin learning automation and scripting in Linux!