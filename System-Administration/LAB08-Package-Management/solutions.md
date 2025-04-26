# LAB08 - Package Management Solutions

Below are the solutions to the package management exercises. Remember to try solving them on your own first!

## Exercise 1: Package Manager Basics

### Solution:
1. Determine Linux distribution and package manager:
   ```bash
   cat /etc/os-release
   ```

2. Update package repository information:
   ```bash
   # For Debian/Ubuntu
   sudo apt update
   
   # For RHEL/CentOS
   sudo yum check-update
   # or
   sudo dnf check-update
   ```

3. List available upgrades:
   ```bash
   # For Debian/Ubuntu
   apt list --upgradable
   
   # For RHEL/CentOS
   yum list updates
   # or
   dnf list --upgrades
   ```

4. Count installed packages:
   ```bash
   # For Debian/Ubuntu
   dpkg -l | grep "^ii" | wc -l
   
   # For RHEL/CentOS
   rpm -qa | wc -l
   ```

5. Display package manager version:
   ```bash
   # For Debian/Ubuntu
   apt --version
   
   # For RHEL/CentOS
   yum --version
   # or
   dnf --version
   ```

6. Review package management logs:
   ```bash
   # For Debian/Ubuntu
   less /var/log/apt/history.log
   
   # For RHEL/CentOS
   less /var/log/yum.log
   # or
   dnf history
   ```

## Exercise 2: Installing and Removing Packages

### Solution:
1. Install htop:
   ```bash
   # For Debian/Ubuntu
   sudo apt install htop
   
   # For RHEL/CentOS
   sudo yum install htop
   ```

2. Run htop:
   ```bash
   htop
   # Press q to exit
   ```

3. Check which package provides htop:
   ```bash
   # For Debian/Ubuntu
   dpkg -S $(which htop)
   
   # For RHEL/CentOS
   rpm -qf $(which htop)
   ```

4. Find htop configuration files:
   ```bash
   # For Debian/Ubuntu
   dpkg -L htop | grep etc
   # If no system-wide config, check user directory
   ls -la ~/.config/htop/
   
   # For RHEL/CentOS
   rpm -ql htop | grep etc
   # If no system-wide config, check user directory
   ls -la ~/.config/htop/
   ```

5. Remove htop but keep configuration:
   ```bash
   # For Debian/Ubuntu
   sudo apt remove htop
   
   # For RHEL/CentOS
   sudo yum remove htop
   ```

6. Completely remove htop including configuration:
   ```bash
   # For Debian/Ubuntu
   sudo apt purge htop
   
   # For RHEL/CentOS
   sudo yum erase htop
   ```

## Exercise 3: Package Searching and Information

### Solution:
1. Search for Python packages:
   ```bash
   # For Debian/Ubuntu
   apt search python | grep ^python
   
   # For RHEL/CentOS
   yum search python
   ```

2. Get detailed package information:
   ```bash
   # For Debian/Ubuntu
   apt show python3
   
   # For RHEL/CentOS
   yum info python3
   ```

3. List files installed by a package:
   ```bash
   # For Debian/Ubuntu
   dpkg -L python3
   
   # For RHEL/CentOS
   rpm -ql python3
   ```

4. Find which package owns a file:
   ```bash
   # For Debian/Ubuntu
   dpkg -S /usr/bin/python3
   
   # For RHEL/CentOS
   rpm -qf /usr/bin/python3
   ```

5. List packages by size:
   ```bash
   # For Debian/Ubuntu
   dpkg-query -W -f='${Installed-Size}\t${Package}\n' | sort -nr | head -n 10
   
   # For RHEL/CentOS
   rpm -qa --queryformat '%{size} %{name}\n' | sort -rn | head -n 10
   ```

6. Find packages by description:
   ```bash
   # For Debian/Ubuntu
   apt-cache search "text editor"
   
   # For RHEL/CentOS
   yum search "text editor"
   ```

## Exercise 4: Dependency Management

### Solution:
1. Identify package dependencies:
   ```bash
   # For Debian/Ubuntu
   apt-cache depends nginx
   
   # For RHEL/CentOS
   yum deplist nginx
   ```

2. Check reverse dependencies:
   ```bash
   # For Debian/Ubuntu
   apt-cache rdepends python3
   
   # For RHEL/CentOS
   yum whatrequires python3
   ```

3. Clean up orphaned packages:
   ```bash
   # For Debian/Ubuntu
   sudo apt autoremove
   
   # For RHEL/CentOS
   sudo yum autoremove
   ```

4. Check for broken dependencies:
   ```bash
   # For Debian/Ubuntu
   sudo apt-get check
   ```

5. Install without recommended dependencies:
   ```bash
   # For Debian/Ubuntu
   sudo apt install --no-install-recommends nginx
   ```

6. Hold a package at its current version:
   ```bash
   # For Debian/Ubuntu
   sudo apt-mark hold nginx
   
   # For RHEL/CentOS
   # First install the versionlock plugin if needed
   sudo yum install yum-plugin-versionlock
   sudo yum versionlock add nginx
   ```

## Exercise 5: Package Management Files and Repositories

### Solution:
1. Examine repository configuration:
   ```bash
   # For Debian/Ubuntu
   cat /etc/apt/sources.list
   ls -la /etc/apt/sources.list.d/
   
   # For RHEL/CentOS
   ls -la /etc/yum.repos.d/
   ```

2. Add a new repository:
   ```bash
   # For Ubuntu
   sudo add-apt-repository ppa:deadsnakes/ppa
   
   # For RHEL/CentOS
   # Create a repo file in /etc/yum.repos.d/
   sudo tee /etc/yum.repos.d/example.repo <<EOF
   [example]
   name=Example Repository
   baseurl=http://example.com/repo
   enabled=1
   gpgcheck=0
   EOF
   ```

3. Update package lists after adding repo:
   ```bash
   # For Debian/Ubuntu
   sudo apt update
   
   # For RHEL/CentOS
   sudo yum makecache
   ```

4. Check package cache size and location:
   ```bash
   # For Debian/Ubuntu
   du -sh /var/cache/apt/
   
   # For RHEL/CentOS
   du -sh /var/cache/yum/
   ```

5. Clean package cache:
   ```bash
   # For Debian/Ubuntu
   sudo apt clean
   
   # For RHEL/CentOS
   sudo yum clean all
   ```

6. Verify package authenticity:
   ```bash
   # For Debian/Ubuntu
   apt-key list
   
   # For RHEL/CentOS
   rpm -qa gpg-pubkey*
   ```

## Exercise 6: Package Upgrades and Maintenance

### Solution:
1. Perform a distribution upgrade simulation:
   ```bash
   # For Debian/Ubuntu
   sudo apt-get -s dist-upgrade
   
   # For RHEL/CentOS
   sudo yum check-update
   ```

2. Install security updates only:
   ```bash
   # For Debian/Ubuntu
   # First install if needed
   sudo apt install unattended-upgrades
   sudo unattended-upgrade --dry-run
   
   # For RHEL/CentOS
   sudo yum update-minimal --security
   ```

3. Configure automatic updates:
   ```bash
   # For Debian/Ubuntu
   sudo apt install unattended-upgrades
   sudo dpkg-reconfigure -plow unattended-upgrades
   
   # For RHEL/CentOS
   sudo yum install dnf-automatic
   sudo systemctl enable --now dnf-automatic.timer
   ```

4. Create a log of installed packages:
   ```bash
   # For Debian/Ubuntu
   dpkg --get-selections > installed_packages.txt
   
   # For RHEL/CentOS
   rpm -qa > installed_packages.txt
   ```

5. Use package manager history:
   ```bash
   # For Debian/Ubuntu
   less /var/log/apt/history.log
   
   # For RHEL/CentOS
   yum history
   ```

6. Check for obsolete packages:
   ```bash
   # For Debian/Ubuntu
   sudo apt install aptitude
   aptitude search ~o
   
   # For RHEL/CentOS
   sudo yum install yum-utils
   package-cleanup --orphans
   ```

## Exercise 7: Package Building Basics

### Solution:
1. Install package building tools:
   ```bash
   # For Debian/Ubuntu
   sudo apt install build-essential devscripts
   
   # For RHEL/CentOS
   sudo yum groupinstall "Development Tools"
   ```

2. Download source package:
   ```bash
   # For Debian/Ubuntu
   # First enable source repositories
   sudo sed -i '/deb-src/s/^# //' /etc/apt/sources.list
   sudo apt update
   apt-get source hello
   
   # For RHEL/CentOS
   sudo yum install yum-utils
   sudo yumdownloader --source hello
   ```

3. Inspect package build files:
   ```bash
   # For example, after downloading the "hello" source
   ls -la hello*/
   cat hello*/debian/rules  # For Debian packages
   cat hello*/*.spec        # For RPM packages
   ```

4. Install from a local package file:
   ```bash
   # For Debian/Ubuntu
   sudo dpkg -i package.deb
   
   # For RHEL/CentOS
   sudo rpm -ivh package.rpm
   ```

5. Verify package after installation:
   ```bash
   # For Debian/Ubuntu
   dpkg -V package_name
   
   # For RHEL/CentOS
   rpm -V package_name
   ```

6. Check integrity of all installed packages:
   ```bash
   # For RHEL/CentOS
   rpm -Va
   ```

## Bonus Challenge Solution:

```bash
#!/bin/bash

# package_manager.sh - Universal package manager script
# Usage: ./package_manager.sh

# Variables
LOG_FILE="$HOME/package_manager_operations.log"
DISTRO=""
PKG_MGR=""

# Function to detect the distribution and package manager
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO="$ID"
        
        case $DISTRO in
            ubuntu|debian|mint)
                PKG_MGR="apt"
                ;;
            centos|rhel|fedora|rocky|alma)
                if command -v dnf &>/dev/null; then
                    PKG_MGR="dnf"
                else
                    PKG_MGR="yum"
                fi
                ;;
            *)
                echo "Unsupported distribution: $DISTRO"
                exit 1
                ;;
        esac
    else
        echo "Could not detect distribution!"
        exit 1
    fi
    
    echo "Detected distribution: $DISTRO"
    echo "Using package manager: $PKG_MGR"
}

# Function to log operations
log_operation() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Function to update the system
update_system() {
    echo "Updating system packages..."
    
    case $PKG_MGR in
        apt)
            log_operation "Running: sudo apt update && sudo apt upgrade -y"
            sudo apt update && sudo apt upgrade -y
            ;;
        yum|dnf)
            log_operation "Running: sudo $PKG_MGR update -y"
            sudo $PKG_MGR update -y
            ;;
    esac
    
    echo "System update completed!"
}

# Function to install a package
install_package() {
    echo -n "Enter package name to install: "
    read package
    
    echo "Installing package: $package"
    
    case $PKG_MGR in
        apt)
            log_operation "Running: sudo apt install $package -y"
            sudo apt install "$package" -y
            ;;
        yum|dnf)
            log_operation "Running: sudo $PKG_MGR install $package -y"
            sudo $PKG_MGR install "$package" -y
            ;;
    esac
}

# Function to remove a package
remove_package() {
    echo -n "Enter package name to remove: "
    read package
    
    echo "Removing package: $package"
    
    case $PKG_MGR in
        apt)
            log_operation "Running: sudo apt remove $package -y"
            sudo apt remove "$package" -y
            ;;
        yum|dnf)
            log_operation "Running: sudo $PKG_MGR remove $package -y"
            sudo $PKG_MGR remove "$package" -y
            ;;
    esac
}

# Function to search for a package
search_package() {
    echo -n "Enter search term: "
    read search_term
    
    echo "Searching for packages matching: $search_term"
    
    case $PKG_MGR in
        apt)
            log_operation "Running: apt search $search_term"
            apt search "$search_term" | grep -E '^[a-z]'
            ;;
        yum|dnf)
            log_operation "Running: $PKG_MGR search $search_term"
            $PKG_MGR search "$search_term"
            ;;
    esac
}

# Function to clean package cache
clean_cache() {
    echo "Cleaning package cache..."
    
    case $PKG_MGR in
        apt)
            log_operation "Running: sudo apt clean && sudo apt autoclean"
            sudo apt clean && sudo apt autoclean
            ;;
        yum|dnf)
            log_operation "Running: sudo $PKG_MGR clean all"
            sudo $PKG_MGR clean all
            ;;
    esac
    
    echo "Package cache cleaned!"
}

# Function to list recently installed packages
list_recent_packages() {
    echo "Recently installed packages:"
    
    case $PKG_MGR in
        apt)
            log_operation "Checking recent installations from /var/log/apt/history.log"
            grep 'Commandline: apt install' /var/log/apt/history.log | tail -n 10
            ;;
        yum)
            log_operation "Running: yum history | head -20"
            sudo yum history | head -20
            ;;
        dnf)
            log_operation "Running: dnf history | head -20"
            sudo dnf history | head -20
            ;;
    esac
}

# Main menu
main_menu() {
    clear
    echo "========================================="
    echo "      Package Management Assistant       "
    echo "========================================="
    echo "Distribution: $DISTRO"
    echo "Package Manager: $PKG_MGR"
    echo "========================================="
    echo "1. Update system"
    echo "2. Install a package"
    echo "3. Remove a package"
    echo "4. Search for a package"
    echo "5. Clean package cache"
    echo "6. List recently installed packages"
    echo "0. Exit"
    echo -n "Enter your choice [0-6]: "
    
    read choice
    
    case $choice in
        1) update_system ;;
        2) install_package ;;
        3) remove_package ;;
        4) search_package ;;
        5) clean_cache ;;
        6) list_recent_packages ;;
        0) 
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Press Enter to continue..."
            read
            ;;
    esac
    
    echo
    echo "Press Enter to return to the menu..."
    read
    main_menu
}

# Main script execution
detect_distro
main_menu
```

To use the script:
```bash
chmod +x package_manager.sh
./package_manager.sh
``` 