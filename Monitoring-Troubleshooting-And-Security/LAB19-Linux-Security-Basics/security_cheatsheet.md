# Linux Security Cheatsheet

This is a quick reference for common Linux security commands and concepts covered in this lab.

## User and Password Management

| Command | Description | Example |
|---------|-------------|---------|
| `passwd` | Change user password | `passwd username` |
| `chage` | Manage password aging | `chage -l username` |
| `chage -M` | Set maximum password age | `chage -M 90 username` |
| `chage -m` | Set minimum password age | `chage -m 7 username` |
| `chage -W` | Set password warning period | `chage -W 14 username` |
| `chage -E` | Set account expiration date | `chage -E 2023-12-31 username` |

## User and Group Commands

| Command | Description | Example |
|---------|-------------|---------|
| `useradd` | Create new user | `useradd -s /sbin/nologin username` |
| `usermod` | Modify user | `usermod -L username` |
| `userdel` | Delete user | `userdel -r username` |
| `groupadd` | Create new group | `groupadd secgroup` |
| `groupdel` | Delete group | `groupdel secgroup` |
| `usermod -G` | Add user to group | `usermod -G secgroup username` |
| `usermod -L` | Lock user account | `usermod -L username` |
| `usermod -U` | Unlock user account | `usermod -U username` |

## File Permissions

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file permissions | `chmod 700 script.sh` |
| `chown` | Change file owner | `chown user:group file.txt` |
| `find` | Find files with specific permissions | `find / -perm -4000 -type f` |
| `umask` | Set default permissions | `umask 027` |

### Common Permission Patterns

| Permission | Numeric | Description |
|------------|---------|-------------|
| `rwx------` | 700 | Owner can read, write, execute |
| `rw-------` | 600 | Owner can read, write |
| `rwxr-xr-x` | 755 | Everyone can read & execute; owner can write |
| `rw-r--r--` | 644 | Everyone can read; owner can write |
| `rwxrwx---` | 770 | Owner & group can read, write, execute |

## SSH Security

| File/Command | Description | Example |
|--------------|-------------|---------|
| `/etc/ssh/sshd_config` | SSH server configuration | - |
| `systemctl restart sshd` | Restart SSH service | - |
| `ssh-keygen` | Generate SSH keys | `ssh-keygen -t ed25519` |

### Key SSH Configuration Options

```
PermitRootLogin no
PasswordAuthentication no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 0
Protocol 2
```

## Firewall Management (UFW)

| Command | Description | Example |
|---------|-------------|---------|
| `ufw enable` | Enable firewall | - |
| `ufw disable` | Disable firewall | - |
| `ufw status` | Check firewall status | - |
| `ufw allow` | Allow traffic | `ufw allow 22/tcp` |
| `ufw deny` | Block traffic | `ufw deny 23/tcp` |
| `ufw default` | Set default policy | `ufw default deny incoming` |

## Service Management

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl list-units --type=service` | List all services | - |
| `systemctl status service` | Check service status | `systemctl status ssh` |
| `systemctl stop service` | Stop a service | `systemctl stop apache2` |
| `systemctl disable service` | Disable service at boot | `systemctl disable cups` |
| `systemctl mask service` | Completely disable service | `systemctl mask bluetooth` |

## System Security Auditing

| Command | Description | Example |
|---------|-------------|---------|
| `find / -perm -4000 -type f` | Find SUID files | - |
| `find / -perm -2000 -type f` | Find SGID files | - |
| `find / -perm -1000 -type f` | Find sticky bit files | - |
| `lsof -i` | List open network files | - |
| `netstat -tuln` | List listening ports | - |
| `ss -tuln` | Modern alternative to netstat | - |

## Security Best Practices

1. **Principle of Least Privilege**: Only grant the minimum permissions necessary
2. **Defense in Depth**: Implement multiple layers of security
3. **Regular Updates**: Keep the system and applications updated
4. **Limit Access**: Reduce attack surface by disabling unnecessary services
5. **Monitor & Audit**: Regularly check logs and audit system security 