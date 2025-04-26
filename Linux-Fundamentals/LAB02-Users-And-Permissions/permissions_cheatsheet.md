# Users and Permissions Cheatsheet

## User Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `useradd` | Create a new user | `sudo useradd username` |
| `userdel` | Delete a user | `sudo userdel username` |
| `passwd` | Set or change a user's password | `sudo passwd username` |
| `usermod` | Modify user account properties | `sudo usermod -aG groupname username` |
| `id` | Display user identity | `id username` |
| `whoami` | Display current user | `whoami` |
| `su` | Switch to another user | `su - username` |
| `sudo` | Execute command as another user (typically root) | `sudo command` |

## Group Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `groupadd` | Create a new group | `sudo groupadd groupname` |
| `groupdel` | Delete a group | `sudo groupdel groupname` |
| `groups` | Display group memberships | `groups username` |
| `gpasswd` | Administer a group | `sudo gpasswd -a username groupname` |

## File Permission Commands

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file permissions | `chmod 755 file` |
| `chown` | Change file owner | `sudo chown user:group file` |
| `chgrp` | Change file group | `sudo chgrp groupname file` |
| `umask` | Set default permissions | `umask 022` |
| `getfacl` | Display file ACLs | `getfacl file` |
| `setfacl` | Set file ACLs | `setfacl -m u:user:rwx file` |

## Understanding Permission Notation

### Symbolic Notation (Letters)

| Symbol | Description |
|--------|-------------|
| `r` | Read permission |
| `w` | Write permission |
| `x` | Execute permission |
| `-` | No permission |

### Numeric Notation (Octal)

| Number | Permission | Symbolic |
|--------|------------|----------|
| `0` | No permission | `---` |
| `1` | Execute only | `--x` |
| `2` | Write only | `-w-` |
| `3` | Write and execute | `-wx` |
| `4` | Read only | `r--` |
| `5` | Read and execute | `r-x` |
| `6` | Read and write | `rw-` |
| `7` | Read, write, and execute | `rwx` |

## Common Permission Examples

| Octal | Symbolic | Meaning |
|-------|----------|---------|
| `755` | `rwxr-xr-x` | Owner: full permissions; Group and Others: read and execute |
| `644` | `rw-r--r--` | Owner: read and write; Group and Others: read only |
| `600` | `rw-------` | Owner: read and write; Group and Others: no permissions |
| `777` | `rwxrwxrwx` | Everyone has full permissions (avoid using!) |
| `750` | `rwxr-x---` | Owner: full permissions; Group: read and execute; Others: none |

## Special Permissions

| Permission | Octal | Effect on Files | Effect on Directories |
|------------|-------|-----------------|----------------------|
| SUID | `4000` | Executes as the owner | No effect |
| SGID | `2000` | Executes as the group | New files inherit directory group |
| Sticky Bit | `1000` | No effect | Only owner can delete files |

## Example: Setting Special Permissions

```bash
# Set SUID bit (runs as file owner)
chmod u+s file
# or
chmod 4755 file

# Set SGID bit (runs as file group or inherits directory group)
chmod g+s file
# or
chmod 2755 file

# Set sticky bit (prevents deletion by non-owners)
chmod +t directory
# or
chmod 1777 directory
```

## Important Files

| File | Description |
|------|-------------|
| `/etc/passwd` | User account information |
| `/etc/shadow` | Encrypted user passwords |
| `/etc/group` | Group information |
| `/etc/sudoers` | Sudo configuration |
| `/etc/login.defs` | Default settings for user accounts | 