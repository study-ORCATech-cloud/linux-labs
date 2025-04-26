# Basic Shell Commands Cheatsheet

## File Viewing Commands

| Command | Description | Example |
|---------|-------------|---------|
| `cat file` | Display entire file content | `cat users.txt` |
| `less file` | View file with pagination | `less large_log.txt` |
| `more file` | Simple file pager | `more data.txt` |
| `head file` | View beginning of file (10 lines by default) | `head -n 5 log.txt` |
| `tail file` | View end of file (10 lines by default) | `tail -n 20 log.txt` |
| `tail -f file` | Follow file updates in real-time | `tail -f /var/log/syslog` |
| `wc file` | Count lines, words, and characters | `wc -l users.txt` |

## Text Processing Commands

| Command | Description | Example |
|---------|-------------|---------|
| `cut -d'x' -f1` | Extract fields from each line | `cut -d: -f1,3 /etc/passwd` |
| `sort file` | Sort lines in file | `sort names.txt` |
| `sort -r file` | Sort in reverse order | `sort -r numbers.txt` |
| `sort -n file` | Sort numerically | `sort -n numbers.txt` |
| `uniq file` | Filter out duplicate adjacent lines | `sort file | uniq` |
| `uniq -c file` | Count occurrences of lines | `sort file | uniq -c` |
| `uniq -d file` | Show only duplicate lines | `sort file | uniq -d` |
| `paste file1 file2` | Merge lines from files | `paste names.txt scores.txt` |
| `paste -d, file1 file2` | Merge with custom delimiter | `paste -d, names.txt scores.txt` |
| `tr 'old' 'new'` | Translate or delete characters | `cat file | tr 'a-z' 'A-Z'` |
| `nl file` | Number lines in file | `nl config.txt` |
| `expand file` | Convert tabs to spaces | `expand -t 4 code.txt` |

## Searching Commands

| Command | Description | Example |
|---------|-------------|---------|
| `grep pattern file` | Find lines with pattern | `grep "error" log.txt` |
| `grep -i pattern file` | Case-insensitive search | `grep -i "warning" log.txt` |
| `grep -v pattern file` | Show lines NOT matching pattern | `grep -v "debug" log.txt` |
| `grep -n pattern file` | Show line numbers with output | `grep -n "error" log.txt` |
| `grep -c pattern file` | Count matching lines | `grep -c "error" log.txt` |
| `grep -A n pattern file` | Show n lines after match | `grep -A 3 "error" log.txt` |
| `grep -B n pattern file` | Show n lines before match | `grep -B 2 "error" log.txt` |
| `grep -r pattern dir` | Recursive search | `grep -r "TODO" src/` |
| `egrep pattern file` | Extended grep (regex) | `egrep "error|warning" log.txt` |

## Redirection and Pipes

| Symbol | Description | Example |
|--------|-------------|---------|
| `>` | Redirect output to file (overwrite) | `ls > files.txt` |
| `>>` | Redirect output to file (append) | `echo "text" >> log.txt` |
| `<` | Redirect input from file | `sort < unsorted.txt` |
| `2>` | Redirect error output | `find / -name "*.log" 2> errors.txt` |
| `2>&1` | Redirect stderr to stdout | `command > all.log 2>&1` |
| `&>` | Redirect both stdout and stderr | `command &> all.log` |
| `\|` | Pipe output to another command | `cat file.txt \| grep "error"` |
| `tee file` | Write to file and stdout | `cat file.txt \| tee copy.txt \| grep "error"` |

## Data Processing

| Command | Description | Example |
|---------|-------------|---------|
| `awk '{print $1}'` | Process and extract text | `awk '{print $1, $3}' data.txt` |
| `awk -F: '{print $1}'` | Specify field separator | `awk -F: '{print $1}' /etc/passwd` |
| `sed 's/old/new/' file` | Stream editor for substitution | `sed 's/error/ERROR/' log.txt` |
| `sed -i 's/old/new/g' file` | Edit file in-place, global replace | `sed -i 's/foo/bar/g' config.txt` |
| `xargs command` | Build command lines from input | `find . -name "*.txt" \| xargs grep "error"` |

## System Information Commands

| Command | Description | Example |
|---------|-------------|---------|
| `date` | Show current date and time | `date "+%Y-%m-%d %H:%M:%S"` |
| `cal` | Display calendar | `cal -3` (show 3 months) |
| `uptime` | Show system uptime | `uptime` |
| `w` | Show logged in users | `w` |
| `whoami` | Show current username | `whoami` |
| `id` | Show user identity | `id` |
| `hostname` | Show system hostname | `hostname -f` (full name) |
| `uname -a` | System information | `uname -a` |
| `df -h` | Disk space usage (human-readable) | `df -h /home` |
| `du -sh dir` | Directory space usage | `du -sh /var/log` |
| `free -h` | Memory usage | `free -m` (in MB) |

## Command Chaining

| Operator | Description | Example |
|----------|-------------|---------|
| `cmd1 ; cmd2` | Run cmd1 then cmd2 | `echo "Hello" ; echo "World"` |
| `cmd1 && cmd2` | Run cmd2 only if cmd1 succeeds | `mkdir dir && cd dir` |
| `cmd1 \|\| cmd2` | Run cmd2 only if cmd1 fails | `grep "pattern" file \|\| echo "Not found"` |
| `(cmd1 ; cmd2)` | Group commands | `(cd dir && ls) \| grep "file"` |

## Useful Command Combinations

1. List all unique IPs in a log file:
   ```bash
   grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" access.log | sort | uniq -c | sort -nr
   ```

2. Count occurrences of each HTTP status code:
   ```bash
   awk '{print $9}' access.log | sort | uniq -c | sort -nr
   ```

3. Find the top 10 largest files:
   ```bash
   find . -type f -exec du -h {} \; | sort -hr | head -n 10
   ```

4. Extract fields from a CSV file:
   ```bash
   cut -d, -f1,3 data.csv | sort | uniq
   ```

5. Monitor a log file for errors:
   ```bash
   tail -f logfile.log | grep --color=auto "ERROR"
   ``` 