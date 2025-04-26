# Package Management Cheatsheet

## Debian/Ubuntu (APT) Commands

| Command | Description | Example |
|---------|-------------|---------|
| `apt update` | Update package list | `sudo apt update` |
| `apt upgrade` | Upgrade installed packages | `sudo apt upgrade` |
| `apt full-upgrade` | Upgrade with package removal if needed | `sudo apt full-upgrade` |
| `apt install` | Install a package | `sudo apt install nginx` |
| `apt remove` | Remove a package | `sudo apt remove nginx` |
| `apt purge` | Remove package and configuration | `sudo apt purge nginx` |
| `apt autoremove` | Remove unneeded dependencies | `sudo apt autoremove` |
| `apt search` | Search for packages | `apt search python` |
| `apt show` | Show package details | `apt show nginx` |
| `apt list` | List packages | `apt list --installed` |
| `apt clean` | Clean local package cache | `sudo apt clean` |
| `apt-get` | Lower-level package manager | `sudo apt-get install nginx` |
| `apt-cache` | Query package cache | `apt-cache policy nginx` |

## RHEL/CentOS/Fedora (YUM/DNF) Commands

| Command | Description | Example |
|---------|-------------|---------|
| `yum check-update` | Check for updates | `sudo yum check-update` |
| `yum update` | Update all packages | `sudo yum update` |
| `yum install` | Install a package | `sudo yum install httpd` |
| `yum remove` | Remove a package | `sudo yum remove httpd` |
| `yum erase` | Remove package completely | `sudo yum erase httpd` |
| `yum search` | Search for packages | `yum search python` |
| `yum info` | Show package details | `yum info httpd` |
| `yum list` | List packages | `yum list installed` |
| `yum clean` | Clean cache | `sudo yum clean all` |
| `yum history` | View transaction history | `yum history` |
| `dnf` | Next-gen YUM (Fedora/RHEL8+) | `sudo dnf install httpd` |
| `dnf autoremove` | Remove unused dependencies | `sudo dnf autoremove` |

## Low-Level Package Commands (Debian)

| Command | Description | Example |
|---------|-------------|---------|
| `dpkg -i` | Install a .deb package | `sudo dpkg -i package.deb` |
| `dpkg -r` | Remove package | `sudo dpkg -r package` |
| `dpkg -P` | Purge package and config | `sudo dpkg -P package` |
| `dpkg -l` | List installed packages | `dpkg -l` |
| `dpkg -L` | List files in package | `dpkg -L nginx` |
| `dpkg -S` | Find which package owns a file | `dpkg -S /usr/bin/nginx` |
| `dpkg-reconfigure` | Reconfigure installed package | `sudo dpkg-reconfigure tzdata` |
| `dpkg --get-selections` | List package selections | `dpkg --get-selections > packages.txt` |
| `dpkg --set-selections` | Set package selections | `dpkg --set-selections < packages.txt` |

## Low-Level Package Commands (RHEL/CentOS)

| Command | Description | Example |
|---------|-------------|---------|
| `rpm -i` | Install an .rpm package | `sudo rpm -i package.rpm` |
| `rpm -e` | Erase/remove package | `sudo rpm -e package` |
| `rpm -q` | Query if package is installed | `rpm -q httpd` |
| `rpm -qa` | List all installed packages | `rpm -qa` |
| `rpm -qi` | Display package info | `rpm -qi httpd` |
| `rpm -ql` | List files in package | `rpm -ql httpd` |
| `rpm -qf` | Find which package owns a file | `rpm -qf /usr/sbin/httpd` |
| `rpm -V` | Verify package | `rpm -V httpd` |
| `rpm -ivh` | Install with verbose & hash progress | `sudo rpm -ivh package.rpm` |
| `rpm -Uvh` | Upgrade with verbose & hash progress | `sudo rpm -Uvh package.rpm` |

## Package Repositories Management

| Command | Description | Example |
|---------|-------------|---------|
| `add-apt-repository` | Add Ubuntu PPA repo | `sudo add-apt-repository ppa:name/here` |
| `apt-add-repository` | Add repo to sources list | `sudo apt-add-repository 'deb http://repo.url stable main'` |
| `sources.list` | APT repo config file | `sudo nano /etc/apt/sources.list` |
| `yum-config-manager` | Manage YUM repos | `sudo yum-config-manager --add-repo=repo_url` |
| `subscription-manager` | Manage RHEL subscriptions | `subscription-manager list` |
| `yum repolist` | List enabled repositories | `yum repolist` |
| `yum repoinfo` | Display repo info | `yum repoinfo base` |

## APT Specific Commands

| Command | Description | Example |
|---------|-------------|---------|
| `apt-mark hold` | Prevent package updates | `sudo apt-mark hold package` |
| `apt-mark unhold` | Allow package updates | `sudo apt-mark unhold package` |
| `apt-mark showhold` | Show held packages | `apt-mark showhold` |
| `apt-get source` | Download source package | `apt-get source nginx` |
| `apt-get build-dep` | Install build dependencies | `sudo apt-get build-dep nginx` |
| `apt-get download` | Download but don't install | `apt-get download nginx` |
| `apt-get changelog` | View package changelog | `apt-get changelog nginx` |
| `apt-get --purge autoremove` | Remove unused packages & configs | `sudo apt-get --purge autoremove` |

## YUM/DNF Specific Commands

| Command | Description | Example |
|---------|-------------|---------|
| `yum grouplist` | List available package groups | `yum grouplist` |
| `yum groupinstall` | Install a package group | `sudo yum groupinstall "Development Tools"` |
| `yum whatprovides` | Find which package provides a file | `yum whatprovides */nginx` |
| `yum deplist` | Show dependencies | `yum deplist httpd` |
| `yum versionlock` | Lock package version | `sudo yum versionlock add httpd` |
| `yum history undo` | Undo transaction | `sudo yum history undo 15` |
| `yum-complete-transaction` | Complete interrupted transaction | `sudo yum-complete-transaction` |
| `yumdownloader` | Download but don't install | `yumdownloader httpd` |
| `dnf module list` | List available modules | `dnf module list` |

## Package Configuration Files

| File | Description | Distribution |
|------|-------------|-------------|
| `/etc/apt/sources.list` | Main APT repository config | Debian/Ubuntu |
| `/etc/apt/sources.list.d/` | Repository definition files | Debian/Ubuntu |
| `/etc/apt/apt.conf.d/` | APT configuration files | Debian/Ubuntu |
| `/var/cache/apt/archives/` | Downloaded package files | Debian/Ubuntu |
| `/var/lib/apt/lists/` | Repository metadata | Debian/Ubuntu |
| `/var/log/apt/` | APT operation logs | Debian/Ubuntu |
| `/etc/yum.repos.d/` | Repository definition files | RHEL/CentOS |
| `/etc/yum.conf` | YUM configuration | RHEL/CentOS |
| `/var/cache/yum/` | YUM cache directory | RHEL/CentOS |
| `/var/log/yum.log` | YUM transaction log | RHEL/CentOS |
| `/etc/dnf/dnf.conf` | DNF configuration | Fedora/RHEL8+ |

## Advanced Package Management Examples

```bash
# Debian/Ubuntu: Install a specific package version
apt install nginx=1.18.0-0ubuntu1

# Search for packages matching a pattern
apt search "^python3.*"

# Get source package and build it
apt-get source --compile package_name

# Install local .deb file and resolve dependencies
apt install ./package.deb

# Show reverse dependencies (what depends on a package)
apt-cache rdepends nginx

# Find all configuration files for a package
find /etc -name "*nginx*"

# Download a package without installing
apt-get download nginx

# Check for broken dependencies
apt-get check

# Extract content from a .deb file without installing
dpkg-deb -x package.deb extract_dir/

# RHEL/CentOS: Install from a specific repository
yum --enablerepo=epel install nginx

# Get package changelog
rpm -q --changelog httpd | less

# Install package with specific options and answer yes
yum install -y --setopt=install_weak_deps=False nginx

# Enable a specific module stream (DNF)
dnf module enable nodejs:12

# Downgrade a package to a specific version
yum downgrade package-1.0.0-1.el7

# Extract an RPM without installing
rpm2cpio package.rpm | cpio -idmv

# Create a local repository
createrepo /path/to/repo/directory
``` 