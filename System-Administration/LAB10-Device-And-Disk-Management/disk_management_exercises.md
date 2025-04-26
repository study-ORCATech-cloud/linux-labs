# LAB10 - Device and Disk Management Exercises

These exercises will help you practice managing storage devices, filesystems, and partitions in Linux. Complete each task to build essential disk management skills for system administration.

## Exercise 1: Exploring Storage Devices

### TODO:
1. List all block devices on your system.

2. Display more detailed information about block devices.

3. Show partitioning information for a specific device.

4. Show detailed information about a specific device.

5. Display hardware information about physical disks.

6. Check disk health and SMART data (if available).

## Exercise 2: Monitoring Disk Usage

### TODO:
1. Display mounted filesystems and their usage.

2. Show disk usage by directory.

3. Find the largest files in a directory.

4. Monitor disk I/O in real-time.

5. Display disk activity statistics.

6. View current disk I/O performance.

## Exercise 3: Working with Mount Points

### TODO:
1. List all currently mounted filesystems.

2. View the entries in the filesystem table.

3. Create a new mount point directory.

4. Mount a filesystem temporarily.

5. Unmount the filesystem.

6. Mount a filesystem with specific options (read-only and no execute).

## Exercise 4: Partitioning Disks

### WARNING: Be extremely careful with these commands. Test only on virtual machines or disks that don't contain important data.

### TODO:
1. Launch the fdisk utility for a device.

2. Create a new partition table using parted.

3. Create new partitions using gdisk (for GPT).

4. Create a new partition with a specific size using parted.

5. Verify the new partition(s).

6. Display partition UUID and label.

## Exercise 5: Creating Filesystems

### WARNING: Be extremely careful with these commands. Test only on virtual machines or disks that don't contain important data.

### TODO:
1. Create an ext4 filesystem on a partition.

2. Create an XFS filesystem on a partition.

3. Create a swap partition.

4. Activate the swap partition.

5. Display filesystem information.

6. Check filesystem for errors.

## Exercise 6: Managing LVM (Logical Volume Management)

### WARNING: Be extremely careful with these commands. Test only on virtual machines or disks that don't contain important data.

### TODO:
1. Check if LVM is installed and list existing physical volumes.

2. Create a physical volume on a partition.

3. Create a volume group.

4. Create a logical volume.

5. Format the logical volume.

6. Mount and verify the logical volume.

## Exercise 7: Disk Maintenance and Recovery

### TODO:
1. Check disk usage and identify large files.

2. Clear systemd journal logs to free up space.

3. Clean apt/yum package cache.

4. Perform filesystem check on next boot.

5. Scan and repair bad blocks on disk.

6. Learn how to recover data from a failing disk using ddrescue.

## Bonus Challenge:
Create a shell script called `disk_monitor.sh` that:
1. Checks disk usage on all mounted filesystems
2. Sends an alert if any filesystem is over 80% full
3. Identifies the largest directories/files on any filesystem over 80% full
4. Creates a log of disk usage trends over time
5. Includes options to clean up common space wasters (logs, package caches, etc.) 