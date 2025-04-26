# Device and Disk Management Cheatsheet

## Device Information Commands

| Command | Description | Example |
|---------|-------------|---------|
| `lsblk` | List block devices | `lsblk` |
| `lsblk -f` | Show filesystems on devices | `lsblk -f` |
| `blkid` | Show block device attributes | `sudo blkid` |
| `fdisk -l` | List partitions on all disks | `sudo fdisk -l` |
| `lshw -class disk` | Hardware info for disks | `sudo lshw -class disk` |
| `hdparm -i` | Show device information | `sudo hdparm -i /dev/sda` |
| `smartctl` | Show SMART disk information | `sudo smartctl -a /dev/sda` |
| `findmnt` | Show mounted filesystems | `findmnt` |
| `parted -l` | List all disks and partitions | `sudo parted -l` |
| `inxi -D` | Show disk information | `inxi -D` |

## Disk Usage Commands

| Command | Description | Example |
|---------|-------------|---------|
| `df -h` | Show disk space usage with human-readable sizes | `df -h` |
| `df -i` | Show inode usage | `df -i` |
| `du -sh` | Summarize directory size | `du -sh /var` |
| `du -sh *` | Show sizes of all items in current directory | `du -sh /var/*` |
| `ncdu` | Interactive disk usage analyzer | `ncdu /` |
| `iotop` | Monitor disk I/O by process | `sudo iotop` |
| `iostat` | Report CPU and disk I/O statistics | `iostat -x 2` |
| `vmstat` | Report virtual memory statistics | `vmstat 1 10` |
| `dstat` | Versatile resource statistics tool | `dstat -d` |
| `free -h` | Show memory and swap usage | `free -h` |

## Mounting and Unmounting

| Command | Description | Example |
|---------|-------------|---------|
| `mount` | Show mounted filesystems or mount a device | `mount` |
| `mount -a` | Mount all filesystems in fstab | `sudo mount -a` |
| `mount -o` | Mount with specific options | `sudo mount -o ro /dev/sdb1 /mnt` |
| `umount` | Unmount a filesystem | `sudo umount /mnt` |
| `umount -l` | Lazy unmount (useful when device is busy) | `sudo umount -l /mnt` |
| `findmnt` | Find mounted filesystems | `findmnt -t ext4` |
| `fuser` | Identify processes using a mount point | `sudo fuser -m /mnt` |
| `lsof` | List open files on a mount point | `sudo lsof /mnt` |

## Partition Management

| Command | Description | Example |
|---------|-------------|---------|
| `fdisk` | Partition editor (MBR) | `sudo fdisk /dev/sdb` |
| `gdisk` | Partition editor (GPT) | `sudo gdisk /dev/sdb` |
| `parted` | Versatile partition editor | `sudo parted /dev/sdb` |
| `gparted` | Graphical partition editor | `sudo gparted` |
| `cfdisk` | User-friendly curses-based partition editor | `sudo cfdisk /dev/sdb` |
| `sfdisk` | Scriptable partition editor | `sudo sfdisk -d /dev/sda > partitions.txt` |
| `partprobe` | Inform OS of partition table changes | `sudo partprobe` |
| `partx` | Tell the kernel about partition table changes | `sudo partx -u /dev/sdb` |

## Filesystem Operations

| Command | Description | Example |
|---------|-------------|---------|
| `mkfs.ext4` | Create ext4 filesystem | `sudo mkfs.ext4 /dev/sdb1` |
| `mkfs.xfs` | Create XFS filesystem | `sudo mkfs.xfs /dev/sdb2` |
| `mkfs.btrfs` | Create BTRFS filesystem | `sudo mkfs.btrfs /dev/sdb3` |
| `mkswap` | Create swap filesystem | `sudo mkswap /dev/sdb4` |
| `swapon/swapoff` | Enable/disable swap | `sudo swapon /dev/sdb4` |
| `tune2fs` | Adjust ext filesystem parameters | `sudo tune2fs -L "BACKUP" /dev/sdb1` |
| `fsck` | Check and repair filesystem | `sudo fsck -f /dev/sdb1` |
| `xfs_repair` | Repair XFS filesystem | `sudo xfs_repair /dev/sdb2` |
| `e2label` | Set ext filesystem label | `sudo e2label /dev/sdb1 backup` |

## LVM (Logical Volume Management)

| Command | Description | Example |
|---------|-------------|---------|
| `pvs` | List physical volumes | `sudo pvs` |
| `vgs` | List volume groups | `sudo vgs` |
| `lvs` | List logical volumes | `sudo lvs` |
| `pvcreate` | Create physical volume | `sudo pvcreate /dev/sdb1` |
| `vgcreate` | Create volume group | `sudo vgcreate vg0 /dev/sdb1` |
| `lvcreate` | Create logical volume | `sudo lvcreate -L 100G -n lv0 vg0` |
| `lvextend` | Extend logical volume | `sudo lvextend -L +5G /dev/vg0/lv0` |
| `vgextend` | Add PV to volume group | `sudo vgextend vg0 /dev/sdc1` |
| `pvmove` | Move data between PVs | `sudo pvmove /dev/sdb1 /dev/sdc1` |
| `lvremove` | Remove logical volume | `sudo lvremove /dev/vg0/lv0` |
| `vgremove` | Remove volume group | `sudo vgremove vg0` |
| `pvremove` | Remove physical volume | `sudo pvremove /dev/sdb1` |
| `lvresize` | Resize a logical volume | `sudo lvresize -L 10G /dev/vg0/lv0` |
| `resize2fs` | Resize filesystem on LV | `sudo resize2fs /dev/vg0/lv0` |

## RAID Management

| Command | Description | Example |
|---------|-------------|---------|
| `mdadm --create` | Create a RAID array | `sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1` |
| `mdadm --detail` | Show RAID details | `sudo mdadm --detail /dev/md0` |
| `mdadm --examine` | Examine a device for RAID info | `sudo mdadm --examine /dev/sdb1` |
| `mdadm --stop` | Stop a RAID array | `sudo mdadm --stop /dev/md0` |
| `mdadm --assemble` | Assemble a RAID array | `sudo mdadm --assemble /dev/md0 /dev/sdb1 /dev/sdc1` |
| `mdadm --manage` | Manage a RAID array | `sudo mdadm --manage /dev/md0 --add /dev/sdd1` |
| `cat /proc/mdstat` | Show RAID status | `cat /proc/mdstat` |

## Disk Maintenance and Recovery

| Command | Description | Example |
|---------|-------------|---------|
| `badblocks` | Search for bad blocks | `sudo badblocks -v /dev/sdb > bad-blocks-list` |
| `e2fsck -l` | Check filesystem with bad blocks list | `sudo e2fsck -l bad-blocks-list /dev/sdb1` |
| `smartctl -t` | Run SMART self-test | `sudo smartctl -t short /dev/sda` |
| `smartctl -H` | Check SMART health status | `sudo smartctl -H /dev/sda` |
| `dd` | Disk cloning and conversion | `sudo dd if=/dev/sda of=/dev/sdb bs=4M status=progress` |
| `ddrescue` | Data recovery tool | `sudo ddrescue /dev/sda /dev/sdb recovery.log` |
| `testdisk` | Data recovery software | `sudo testdisk` |
| `photorec` | File recovery software | `sudo photorec` |
| `fsck.ext4 -c` | Check for bad blocks during fsck | `sudo fsck.ext4 -c /dev/sdb1` |

## Configuration Files and Directories

| File/Directory | Description | Example Use |
|----------------|-------------|-------------|
| `/etc/fstab` | Filesystem table | `nano /etc/fstab` |
| `/etc/mtab` | Currently mounted filesystems | `cat /etc/mtab` |
| `/proc/mounts` | Kernel's view of mounted filesystems | `cat /proc/mounts` |
| `/proc/partitions` | System partition information | `cat /proc/partitions` |
| `/etc/lvm/` | LVM configuration directory | `ls -la /etc/lvm/` |
| `/etc/mdadm/mdadm.conf` | RAID configuration | `cat /etc/mdadm/mdadm.conf` |
| `/sys/block/` | Block device information in sysfs | `ls -la /sys/block/sda/` |
| `/dev/disk/by-uuid/` | Disk device links by UUID | `ls -la /dev/disk/by-uuid/` |
| `/dev/disk/by-label/` | Disk device links by label | `ls -la /dev/disk/by-label/` |
| `/var/log/messages` | General system logs (including disk errors) | `grep -i "sda" /var/log/messages` |

## Advanced Disk Management Examples

```bash
# Create a 2GB swap file
sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Partition a disk with specific sizes using parted
sudo parted /dev/sdb mklabel gpt
sudo parted -a optimal /dev/sdb mkpart primary 0% 25%
sudo parted -a optimal /dev/sdb mkpart primary 25% 75%
sudo parted -a optimal /dev/sdb mkpart primary 75% 100%

# Show top directory sizes (useful for disk cleanup)
sudo du -h --max-depth=1 / | sort -hr

# Set up email alerts when a disk is failing
echo '#!/bin/bash
smartctl -H /dev/sda | grep -q "PASSED" || echo "SMART failure on /dev/sda" | mail -s "Disk Failure" admin@example.com
' > /etc/cron.daily/disk-health-check
chmod +x /etc/cron.daily/disk-health-check

# Resize a filesystem after extending an LVM volume
sudo lvextend -L +10G /dev/mapper/vg-lv
sudo resize2fs /dev/mapper/vg-lv

# Find all files larger than 100MB
sudo find / -type f -size +100M -exec ls -lh {} \; | sort -k5 -hr

# Monitor disk I/O with dstat
dstat --top-io --top-bio

# Set disk read-ahead buffer (improves performance for sequential reads)
sudo blockdev --setra 4096 /dev/sda

# Check for active disk operations before shutdown
sudo lsof | grep /mnt
sudo fuser -m /mnt

# Create filesystem snapshot with LVM
sudo lvcreate -L 5G -s -n snapshot_name /dev/vg0/lv0

# Schedule a filesystem check on the next boot for ext4
sudo tune2fs -c 1 /dev/sda1
``` 