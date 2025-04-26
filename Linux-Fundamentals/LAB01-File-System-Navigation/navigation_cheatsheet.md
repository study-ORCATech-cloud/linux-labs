# File System Navigation Cheatsheet

## Basic Navigation Commands

| Command | Description | Example |
|---------|-------------|---------|
| `pwd` | Print Working Directory - shows current location | `pwd` |
| `cd` | Change Directory - navigate to specified directory | `cd /home/user` |
| `ls` | List - show directory contents | `ls -la` |
| `mkdir` | Make Directory - create new directory | `mkdir new_folder` |
| `rmdir` | Remove Directory - delete empty directory | `rmdir old_folder` |
| `rm` | Remove - delete files or directories | `rm -r folder` |

## Path Types

| Path Type | Description | Example |
|-----------|-------------|---------|
| Absolute | Starts from root directory (/) | `/home/user/Documents` |
| Relative | Starts from current location | `Documents/files` |
| Home Directory | Starts from user's home | `~/Documents` |

## Special Path Shortcuts

| Shortcut | Description |
|----------|-------------|
| `.` | Current directory |
| `..` | Parent directory (one level up) |
| `~` | Home directory |
| `-` | Previous directory (where you were before) |

## Common `ls` Options

| Option | Description | Example |
|--------|-------------|---------|
| `-l` | Long format (detailed info) | `ls -l` |
| `-a` | All files (including hidden) | `ls -a` |
| `-h` | Human-readable file sizes | `ls -lh` |
| `-t` | Sort by modification time | `ls -lt` |
| `-r` | Reverse order | `ls -lr` |
| `-R` | Recursive (include subdirectories) | `ls -R` |

## Directory Creation

| Command | Description | Example |
|---------|-------------|---------|
| `mkdir dir1` | Create single directory | `mkdir Documents` |
| `mkdir -p dir1/dir2/dir3` | Create nested directories | `mkdir -p Projects/web/css` |

## Path Navigation Examples

```bash
# Go to home directory
cd ~
# or simply:
cd

# Go up one level
cd ..

# Go up two levels
cd ../..

# Go to root directory
cd /

# Go to previous directory
cd -

# Go to absolute path
cd /var/log

# Go to subdirectory (relative)
cd Documents/Projects
```

## Practical Tips

1. Use Tab completion to avoid typing long paths
2. Use up/down arrow keys to navigate command history
3. Use `clear` to clear the terminal screen
4. Remember that Linux is case-sensitive for filenames and commands 