# File Searching and Archiving Cheatsheet

## Finding Files

### find Command

| Command | Description | Example |
|---------|-------------|---------|
| `find dir -name pattern` | Find files by name | `find /home -name "*.txt"` |
| `find dir -type f` | Find only files | `find /var -type f` |
| `find dir -type d` | Find only directories | `find /etc -type d` |
| `find dir -user username` | Find files owned by user | `find /home -user john` |
| `find dir -size +10M` | Find files larger than 10MB | `find / -size +10M` |
| `find dir -size -1M` | Find files smaller than 1MB | `find /var/log -size -1M` |
| `find dir -mtime -7` | Find files modified in the last 7 days | `find /home -mtime -7` |
| `find dir -mmin -60` | Find files modified in the last 60 minutes | `find /tmp -mmin -60` |
| `find dir -exec cmd {} \;` | Execute command on each result | `find . -name "*.log" -exec rm {} \;` |
| `find dir -perm mode` | Find files with specific permissions | `find /bin -perm 755` |

### locate Command

| Command | Description | Example |
|---------|-------------|---------|
| `locate pattern` | Find files by name using database | `locate "*.conf"` |
| `updatedb` | Update the locate database | `sudo updatedb` |
| `locate -i pattern` | Case-insensitive search | `locate -i "readme"` |
| `locate -c pattern` | Count matching entries | `locate -c "*.py"` |

### grep Command

| Command | Description | Example |
|---------|-------------|---------|
| `grep pattern file` | Search for pattern in file | `grep "error" log.txt` |
| `grep -r pattern dir` | Recursive search in directory | `grep -r "function" /src` |
| `grep -i pattern file` | Case-insensitive search | `grep -i "warning" log.txt` |
| `grep -v pattern file` | Show lines NOT matching pattern | `grep -v "debug" log.txt` |
| `grep -l pattern files` | Show only filenames with matches | `grep -l "TODO" *.c` |
| `grep -n pattern file` | Show line numbers with output | `grep -n "main()" *.c` |
| `grep -A n pattern file` | Show n lines after match | `grep -A 3 "error" log.txt` |
| `grep -B n pattern file` | Show n lines before match | `grep -B 2 "error" log.txt` |
| `grep -C n pattern file` | Show n lines around match | `grep -C 2 "error" log.txt` |

## Archiving Files

### tar Command (Tape Archive)

| Command | Description | Example |
|---------|-------------|---------|
| `tar -cvf archive.tar dir/` | Create archive | `tar -cvf backup.tar /home/user/` |
| `tar -xvf archive.tar` | Extract archive | `tar -xvf backup.tar` |
| `tar -tvf archive.tar` | List contents | `tar -tvf backup.tar` |
| `tar -czvf archive.tar.gz dir/` | Create compressed archive with gzip | `tar -czvf backup.tar.gz /home/user/` |
| `tar -xzvf archive.tar.gz` | Extract gzipped archive | `tar -xzvf backup.tar.gz` |
| `tar -cjvf archive.tar.bz2 dir/` | Create compressed archive with bzip2 | `tar -cjvf backup.tar.bz2 /home/user/` |
| `tar -xjvf archive.tar.bz2` | Extract bzip2 archive | `tar -xjvf backup.tar.bz2` |
| `tar -C dir -xvf archive.tar` | Extract to specific directory | `tar -C /tmp -xvf backup.tar` |

#### tar Options

| Option | Description |
|--------|-------------|
| `-c` | Create a new archive |
| `-x` | Extract files from archive |
| `-t` | List the contents of archive |
| `-v` | Verbose output |
| `-f` | Specify archive file name |
| `-z` | Filter through gzip |
| `-j` | Filter through bzip2 |
| `-J` | Filter through xz |
| `-C dir` | Change to directory before operation |
| `-p` | Preserve permissions |
| `--exclude=pattern` | Exclude files/directories |

### gzip/gunzip Command

| Command | Description | Example |
|---------|-------------|---------|
| `gzip file` | Compress file (replaces original) | `gzip largefile.txt` |
| `gzip -c file > file.gz` | Compress file (keep original) | `gzip -c largefile.txt > largefile.txt.gz` |
| `gzip -r directory` | Recursively compress files in directory | `gzip -r ./logs` |
| `gzip -d file.gz` | Decompress file | `gzip -d largefile.txt.gz` |
| `gunzip file.gz` | Decompress file | `gunzip largefile.txt.gz` |
| `gunzip -c file.gz > file` | Decompress while keeping .gz file | `gunzip -c largefile.txt.gz > largefile.txt` |
| `gzip -l file.gz` | List compression information | `gzip -l *.gz` |

### zip/unzip Command

| Command | Description | Example |
|---------|-------------|---------|
| `zip archive.zip files` | Create zip archive | `zip backup.zip *.txt` |
| `zip -r archive.zip directory` | Recursively zip directory | `zip -r backup.zip ./docs` |
| `unzip archive.zip` | Extract zip archive | `unzip backup.zip` |
| `unzip -l archive.zip` | List contents of zip file | `unzip -l backup.zip` |
| `zip -u archive.zip files` | Update existing zip archive | `zip -u backup.zip newfile.txt` |
| `unzip archive.zip -d directory` | Extract to specific directory | `unzip backup.zip -d /tmp` |
| `unzip archive.zip file` | Extract specific file | `unzip backup.zip file.txt` |

## Combining Search and Archive

### Examples

1. Find and archive in one command:
   ```bash
   find /home -name "*.jpg" | tar -cvf photos.tar -T -
   ```

2. Find and compress in one step:
   ```bash
   find /var/log -name "*.log" -exec gzip {} \;
   ```

3. Search for text and create archive of matching files:
   ```bash
   grep -l "TODO" *.c | xargs tar -cvf todo.tar
   ```

4. Create a tar file from the most recently modified files:
   ```bash
   find . -type f -mtime -7 | tar -cvf recent.tar -T -
   ```

5. Search for and archive only files containing specific text:
   ```bash
   find . -name "*.txt" -exec grep -l "important" {} \; | tar -cvf important.tar -T -
   ``` 