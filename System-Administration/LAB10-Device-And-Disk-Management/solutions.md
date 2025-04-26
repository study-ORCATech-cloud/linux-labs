# LAB10 - Device and Disk Management Solutions

Below are the solutions to the device and disk management exercises. Remember to try solving them on your own first!

## Exercise 1: Exploring Storage Devices

### Solution:
1. List all block devices on your system:
   ```bash
   lsblk
   ```
   Output example:
   ```
   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   sda           8:0    0   100G  0 disk 
   ├─sda1        8:1    0     1G  0 part /boot
   ├─sda2        8:2    0    10G  0 part [SWAP]
   └─sda3        8:3    0    89G  0 part /
   ```

2. Display more detailed information about block devices:
   ```bash
   sudo blkid
   ```
   Output example:
   ```
   /dev/sda1: UUID="c8b93f87-78a4-4f8c-a672-9282cd890915" TYPE="ext4" PARTUUID="bd2722cf-01"
   /dev/sda2: UUID="4e5153d4-629e-4a7d-bc80-5771c6611671" TYPE="swap" PARTUUID="bd2722cf-02"
   /dev/sda3: UUID="2c8bfefb-464a-485e-a4c7-98e90d1cb0b8" TYPE="ext4" PARTUUID="bd2722cf-03"
   ```

3. Show partitioning information for a specific device:
   ```bash
   sudo fdisk -l /dev/sda
   ```
   Output example:
   ```
   Disk /dev/sda: 100 GiB, 107374182400 bytes, 209715200 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0xbd2722cf

   Device     Boot   Start       End   Sectors  Size Id Type
   /dev/sda1  *       2048   2099199   2097152    1G 83 Linux
   /dev/sda2       2099200  23072767  20973568   10G 82 Linux swap
   /dev/sda3      23072768 209715199 186642432   89G 83 Linux
   ```

4. Show detailed information about a specific device:
   ```bash
   sudo lshw -class disk
   ```
   Output example:
   ```
   *-disk
        description: ATA Disk
        product: VBOX HARDDISK
        vendor: VirtualBox
        physical id: 0.0.0
        bus info: scsi@0:0.0.0
        logical name: /dev/sda
        version: 1.0
        serial: VB1234567890
        size: 100GiB
        capabilities: partitioned partitioned:dos
        configuration: ansiversion=5 logicalsectorsize=512 sectorsize=512
   ```

5. Display hardware information about physical disks:
   ```bash
   sudo hdparm -i /dev/sda
   ```
   Output example:
   ```
   /dev/sda:
   
    Model=VBOX HARDDISK, FwRev=1.0, SerialNo=VB1234567890
    Config={ Fixed }
    RawCHS=16383/16/63, TrkSize=0, SectSize=0, ECCbytes=0
    BuffType=unknown, BuffSize=256kB, MaxMultSect=16, MultSect=16
    CurCHS=16383/16/63, CurSects=16514064, LBA=yes, LBAsects=209715200
    IORDY=yes, tPIO={min:120,w/IORDY:120}, tDMA={min:120,rec:120}
    PIO modes:  pio0 pio1 pio2 pio3 pio4 
    DMA modes:  mdma0 mdma1 mdma2 
    UDMA modes: udma0 udma1 udma2 udma3 udma4 udma5 *udma6 
    AdvancedPM=no WriteCache=enabled
    Drive conforms to: unknown:  ATA/ATAPI-5,6,7
   ```

6. Check disk health and SMART data (if available):
   ```bash
   sudo smartctl -a /dev/sda
   ```
   Output example:
   ```
   smartctl 7.2 2020-12-30 r5155 [x86_64-linux-5.15.0-76-generic] (local build)
   Copyright (C) 2002-20, Bruce Allen, Christian Franke, www.smartmontools.org

   Device Model:     VBOX HARDDISK
   Serial Number:    VB1234567890
   Firmware Version: 1.0
   User Capacity:    107,374,182,400 bytes [107 GB]
   Sector Size:      512 bytes logical/physical
   Device is:        Not in smartctl database [for details use: -P showall]
   ATA Version is:   ATA/ATAPI-5 published, ANSI INCITS 340-2000
   Local Time is:    Wed Jan 17 15:52:39 2024 UTC
   SMART support is: Available - device has SMART capability.
   SMART support is: Enabled
   ```

## Exercise 2: Monitoring Disk Usage

### Solution:
1. Display mounted filesystems and their usage:
   ```bash
   df -h
   ```
   Output example:
   ```
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/sda3        88G   20G   64G  24% /
   /dev/sda1       976M  205M  705M  23% /boot
   tmpfs           1.6G     0  1.6G   0% /dev/shm
   ```

2. Show disk usage by directory:
   ```bash
   du -sh /var/*
   ```
   Output example:
   ```
   20K     /var/backups
   72M     /var/cache
   4.0K    /var/crash
   264K    /var/lib
   4.0K    /var/local
   0       /var/lock
   5.2M    /var/log
   4.0K    /var/mail
   4.0K    /var/opt
   0       /var/run
   640K    /var/spool
   0       /var/tmp
   ```

3. Find the largest files in a directory:
   ```bash
   sudo find /var -type f -exec du -h {} \; | sort -rh | head -n 10
   ```
   Output example:
   ```
   40M     /var/cache/apt/archives/libreoffice-common_1%3a7.3.7-0ubuntu0.22.04.3_all.deb
   20M     /var/cache/apt/archives/firefox_120.0.1+build1-0ubuntu0.22.04.1_amd64.deb
   15M     /var/cache/apt/archives/linux-firmware_1.201.4_all.deb
   10M     /var/cache/apt/archives/thunderbird_1%3a102.15.1+build1-0ubuntu0.22.04.1_amd64.deb
   8.0M    /var/log/journal/3c9ce8e6d8b048e0a8a1adecfdc432f2/system.journal
   5.5M    /var/cache/apt/archives/libgl1-mesa-dri_22.0.1-1ubuntu2.1_amd64.deb
   4.2M    /var/cache/apt/archives/python3-distupgrade_1:22.04.17_all.deb
   4.0M    /var/cache/apt/archives/ubuntu-release-upgrader-gtk_1:22.04.17_all.deb
   3.8M    /var/cache/apt/archives/python3-update-manager_1:22.04.6_all.deb
   ```

4. Monitor disk I/O in real-time:
   ```bash
   sudo iotop
   ```
   Output example:
   ```
   Total DISK READ:       0.00 B/s | Total DISK WRITE:       0.00 B/s
   Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
     TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
       1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --system
     345 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kworker/0:3-events]
     789 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % sshd: ubuntu [priv]
    1029 be/4 ubuntu      0.00 B/s    0.00 B/s  0.00 %  0.00 % bash
   ```

5. Display disk activity statistics:
   ```bash
   iostat -x 2
   ```
   Output example:
   ```
   Linux 5.15.0-76-generic   01/17/2024      _x86_64_        (2 CPU)

   avg-cpu:  %user   %nice %system %iowait  %steal   %idle
              2.81    0.00    1.51    0.30    0.00   95.38

   Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
   sda              0.16    0.58      6.33     11.57     0.00     0.22   0.00  27.27    0.38    1.61   0.00    40.21    19.87   0.49   0.04
   ```

6. View current disk I/O performance:
   ```bash
   sudo vmstat 1 10
   ```
   Output example:
   ```
   procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
    r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
    0  0      0 3128744  46480 842408    0    0     2     4   27   48  3  2 95  0  0
    0  0      0 3128744  46480 842408    0    0     0     0  108  189  0  0 100  0  0
    0  0      0 3128744  46480 842408    0    0     0     0  102  177  0  0 100  0  0
   ```

## Exercise 3: Working with Mount Points

### Solution:
1. List all currently mounted filesystems:
   ```bash
   mount
   ```
   Output example:
   ```
   sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
   proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
   udev on /dev type devtmpfs (rw,nosuid,relatime,size=1986560k,nr_inodes=496640)
   devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620)
   /dev/sda3 on / type ext4 (rw,relatime,errors=remount-ro)
   /dev/sda1 on /boot type ext4 (rw,relatime)
   ```

2. View the entries in the filesystem table:
   ```bash
   cat /etc/fstab
   ```
   Output example:
   ```
   # /etc/fstab: static file system information.
   #
   # Use 'blkid' to print the universally unique identifier for a
   # device; this may be used with UUID= as a more robust way to name devices
   # that works even if disks are added and removed. See fstab(5).
   #
   # <file system> <mount point>   <type>  <options>       <dump>  <pass>
   UUID=c8b93f87-78a4-4f8c-a672-9282cd890915 /boot           ext4    defaults        0       2
   UUID=2c8bfefb-464a-485e-a4c7-98e90d1cb0b8 /               ext4    errors=remount-ro 0       1
   UUID=4e5153d4-629e-4a7d-bc80-5771c6611671 none            swap    sw              0       0
   ```

3. Create a new mount point directory:
   ```bash
   sudo mkdir /mnt/testdisk
   ```

4. Mount a filesystem temporarily:
   ```bash
   # Replace /dev/sdX1 with the actual partition you want to mount, for example /dev/sdb1
   sudo mount /dev/sdb1 /mnt/testdisk
   ```

5. Unmount the filesystem:
   ```bash
   sudo umount /mnt/testdisk
   ```

6. Mount a filesystem with specific options:
   ```bash
   sudo mount -o ro,noexec /dev/sdb1 /mnt/testdisk
   ```

## Exercise 4: Partitioning Disks

### Solution:
1. Launch the fdisk utility for a device:
   ```bash
   # Replace /dev/sdX with the device you want to partition, for example /dev/sdb
   sudo fdisk /dev/sdb
   ```
   
   Common fdisk commands:
   ```
   m - display help menu
   p - print the partition table
   n - create a new partition
   d - delete a partition
   w - write changes to disk
   q - quit without saving changes
   ```

2. Create a new partition table using parted:
   ```bash
   # Replace /dev/sdX with your test device, for example /dev/sdb
   sudo parted /dev/sdb mklabel gpt
   ```

3. Create new partitions using gdisk (for GPT):
   ```bash
   sudo gdisk /dev/sdb
   ```
   
   Common gdisk commands:
   ```
   ? - display help menu
   p - print the partition table
   n - create a new partition
   d - delete a partition
   w - write changes to disk
   q - quit without saving changes
   ```

4. Create a new partition with a specific size using parted:
   ```bash
   sudo parted /dev/sdb mkpart primary ext4 1MiB 501MiB
   ```

5. Verify the new partition(s):
   ```bash
   sudo partprobe
   lsblk
   ```

6. Display partition UUID and label:
   ```bash
   sudo blkid /dev/sdb1
   ```

## Exercise 5: Creating Filesystems

### Solution:
1. Create an ext4 filesystem on a partition:
   ```bash
   # Replace /dev/sdX1 with the partition you want to format, for example /dev/sdb1
   sudo mkfs.ext4 /dev/sdb1
   ```
   Output example:
   ```
   mke2fs 1.46.5 (30-Dec-2021)
   Creating filesystem with 125952 4k blocks and 31488 inodes
   Filesystem UUID: f9f49a22-9b11-4cc1-b6f4-e3d5cca789ad
   Superblock backups stored on blocks: 
   	32768, 98304
   
   Allocating group tables: done                            
   Writing inode tables: done                            
   Creating journal (4096 blocks): done
   Writing superblocks and filesystem accounting information: done
   ```

2. Create an XFS filesystem on a partition:
   ```bash
   sudo mkfs.xfs /dev/sdb2
   ```
   Output example:
   ```
   meta-data=/dev/sdb2              isize=512    agcount=4, agsize=65536 blks
            =                       sectsz=512   attr=2, projid32bit=1
            =                       crc=1        finobt=1, sparse=1, rmapbt=0
            =                       reflink=1    bigtime=0 inobtcount=0
   data     =                       bsize=4096   blocks=262144, imaxpct=25
            =                       sunit=0      swidth=0 blks
   naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
   log      =internal log           bsize=4096   blocks=2560, version=2
            =                       sectsz=512   sunit=0 blks, lazy-count=1
   realtime =none                   extsz=4096   blocks=0, rtextents=0
   ```

3. Create a swap partition:
   ```bash
   sudo mkswap /dev/sdb3
   ```
   Output example:
   ```
   Setting up swapspace version 1, size = 500 MiB (524283904 bytes)
   no label, UUID=63cc1eb9-4781-4b66-a409-9fe6dc5614d3
   ```

4. Activate the swap partition:
   ```bash
   sudo swapon /dev/sdb3
   ```

5. Display filesystem information:
   ```bash
   sudo tune2fs -l /dev/sdb1
   ```
   Output example:
   ```
   tune2fs 1.46.5 (30-Dec-2021)
   Filesystem volume name:   <none>
   Last mounted on:          <not available>
   Filesystem UUID:          f9f49a22-9b11-4cc1-b6f4-e3d5cca789ad
   Filesystem magic number:  0xEF53
   Filesystem revision #:    1 (dynamic)
   Filesystem features:      has_journal ext_attr resize_inode dir_index filetype extent 64bit flex_bg sparse_super large_file huge_file dir_nlink extra_isize metadata_csum
   ```

6. Check filesystem for errors:
   ```bash
   sudo fsck /dev/sdb1
   ```
   Output example:
   ```
   fsck from util-linux 2.37.2
   e2fsck 1.46.5 (30-Dec-2021)
   /dev/sdb1: clean, 11/31488 files, 8667/125952 blocks
   ```

## Exercise 6: Managing LVM (Logical Volume Management)

### Solution:
1. Check if LVM is installed and list existing physical volumes:
   ```bash
   sudo pvs
   ```
   Output example:
   ```
   PV         VG        Fmt  Attr PSize   PFree
   /dev/sdc1  vg_data   lvm2 a--   10.00g   0  
   ```

2. Create a physical volume on a partition:
   ```bash
   # Replace /dev/sdX1 with your test partition, for example /dev/sdb4
   sudo pvcreate /dev/sdb4
   ```
   Output example:
   ```
   Physical volume "/dev/sdb4" successfully created.
   ```

3. Create a volume group:
   ```bash
   sudo vgcreate vg_test /dev/sdb4
   ```
   Output example:
   ```
   Volume group "vg_test" successfully created
   ```

4. Create a logical volume:
   ```bash
   sudo lvcreate -L 100M -n lv_test vg_test
   ```
   Output example:
   ```
   Logical volume "lv_test" created.
   ```

5. Format the logical volume:
   ```bash
   sudo mkfs.ext4 /dev/vg_test/lv_test
   ```
   Output example:
   ```
   mke2fs 1.46.5 (30-Dec-2021)
   Creating filesystem with 25600 4k blocks and 25600 inodes
   Filesystem UUID: a5a1c63a-1a8c-4ced-a5e7-6c1bb7fe25b5
   Superblock backups stored on blocks: 
   	8193, 24577
   
   Allocating group tables: done                            
   Writing inode tables: done                            
   Creating journal (1024 blocks): done
   Writing superblocks and filesystem accounting information: done
   ```

6. Mount and verify the logical volume:
   ```bash
   sudo mkdir -p /mnt/lvm_test
   sudo mount /dev/vg_test/lv_test /mnt/lvm_test
   df -h | grep lvm_test
   ```
   Output example:
   ```
   /dev/mapper/vg_test-lv_test   97M  1.6M   89M   2% /mnt/lvm_test
   ```

## Exercise 7: Disk Maintenance and Recovery

### Solution:
1. Check disk usage and identify large files:
   ```bash
   sudo du -h --max-depth=1 /var | sort -hr
   ```
   Output example:
   ```
   108M    /var
   72M     /var/cache
   25M     /var/lib
   5.2M    /var/log
   1.4M    /var/spool
   644K    /var/backups
   ```

2. Clear systemd journal logs to free up space:
   ```bash
   sudo journalctl --vacuum-time=2d
   ```
   Output example:
   ```
   Deleted archived journal /var/log/journal/3c9ce8e6d8b048e0a8a1adecfdc432f2/system@19d3a9d3c7d74e28b018eba25049d9ca-000000000002597d-00060cc3a9e45152.journal (16.0M).
   Vacuuming done, freed 16.0M of archived journals.
   ```

3. Clean apt/yum package cache:
   ```bash
   # For Debian/Ubuntu
   sudo apt clean
   
   # For RHEL/CentOS
   sudo yum clean all
   ```

4. Check for filesystem errors:
   ```bash
   sudo fsck -f /dev/sdb1
   ```
   Output example:
   ```
   fsck from util-linux 2.37.2
   e2fsck 1.46.5 (30-Dec-2021)
   Pass 1: Checking inodes, blocks, and sizes
   Pass 2: Checking directory structure
   Pass 3: Checking directory connectivity
   Pass 4: Checking reference counts
   Pass 5: Checking group summary information
   /dev/sdb1: 11/31488 files (0.0% non-contiguous), 8667/125952 blocks
   ```

5. Check and repair a mounted filesystem at next reboot:
   ```bash
   sudo touch /forcefsck
   ```

6. Monitor disk health with SMART:
   ```bash
   sudo smartctl -t short /dev/sda
   ```
   Output example:
   ```
   smartctl 7.2 2020-12-30 r5155 [x86_64-linux-5.15.0-76-generic] (local build)
   Copyright (C) 2002-20, Bruce Allen, Christian Franke, www.smartmontools.org

   Sending command: "Execute SMART Short self-test routine immediately in off-line mode".
   Drive command "Execute SMART Short self-test routine immediately in off-line mode" successful.
   Testing has begun.
   Please wait 1 minutes for test to complete.
   Test will complete after Wed Jan 17 16:12:10 2024 UTC
   Use smartctl -X to abort test.
   ```

   Check results after it completes:
   ```bash
   sudo smartctl -H /dev/sda
   ```

## Exercise 8: Cleanup

### Solution:
1. Unmount any mounted filesystems created during these exercises:
   ```bash
   sudo umount /mnt/testdisk
   sudo umount /mnt/lvm_test
   ```

2. Deactivate and remove any logical volumes created:
   ```bash
   sudo lvchange -an /dev/vg_test/lv_test
   sudo lvremove /dev/vg_test/lv_test
   ```
   Output example:
   ```
   Do you really want to remove active logical volume vg_test/lv_test? [y/n]: y
   Logical volume "lv_test" successfully removed
   ```

3. Remove the volume group:
   ```bash
   sudo vgremove vg_test
   ```
   Output example:
   ```
   Volume group "vg_test" successfully removed
   ```

4. Remove the physical volume:
   ```bash
   sudo pvremove /dev/sdb4
   ```
   Output example:
   ```
   Labels on physical volume "/dev/sdb4" successfully wiped.
   ```

5. Turn off swap partitions you created:
   ```bash
   sudo swapoff /dev/sdb3
   ```

6. Remove any mount point directories created:
   ```bash
   sudo rmdir /mnt/testdisk
   sudo rmdir /mnt/lvm_test
   ``` 