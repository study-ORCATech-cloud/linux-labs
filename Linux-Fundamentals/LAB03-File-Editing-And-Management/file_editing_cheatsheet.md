# Text Editors and File Management Cheatsheet

## Basic File Operations

| Command | Description | Example |
|---------|-------------|---------|
| `touch` | Create empty file(s) | `touch file.txt` |
| `cat` | Display file content | `cat file.txt` |
| `less` | View file content with pagination | `less file.txt` |
| `head` | Show first lines of a file | `head -n 5 file.txt` |
| `tail` | Show last lines of a file | `tail -n 10 file.txt` |
| `cp` | Copy files or directories | `cp file.txt backup/` |
| `mv` | Move or rename files | `mv old.txt new.txt` |
| `rm` | Remove files | `rm file.txt` |
| `mkdir` | Create directory | `mkdir documents` |
| `rmdir` | Remove empty directory | `rmdir emptyfolder` |
| `rm -r` | Remove directory and contents | `rm -r folder` |
| `ln -s` | Create symbolic link | `ln -s target link_name` |

## File Content Operations

| Command | Description | Example |
|---------|-------------|---------|
| `wc` | Count lines, words, chars | `wc file.txt` |
| `sort` | Sort file content | `sort file.txt` |
| `uniq` | Show/remove duplicate lines | `sort file.txt \| uniq` |
| `grep` | Search for patterns | `grep "pattern" file.txt` |
| `diff` | Compare files line by line | `diff file1.txt file2.txt` |
| `cut` | Extract sections from lines | `cut -d, -f1 file.csv` |
| `tr` | Translate or delete chars | `cat file.txt \| tr 'a-z' 'A-Z'` |

## I/O Redirection

| Operator | Description | Example |
|----------|-------------|---------|
| `>` | Redirect output to file (overwrite) | `echo "text" > file.txt` |
| `>>` | Redirect output to file (append) | `echo "more" >> file.txt` |
| `<` | Redirect input from file | `sort < unsorted.txt` |
| `\|` | Pipe output to another command | `cat file.txt \| grep "pattern"` |
| `2>` | Redirect error output | `command 2> errors.log` |
| `&>` | Redirect all output | `command &> all.log` |

## Nano Editor Commands

| Keystroke | Description |
|-----------|-------------|
| `Ctrl+G` | Display help |
| `Ctrl+O` | Save file |
| `Ctrl+X` | Exit nano |
| `Ctrl+K` | Cut line |
| `Ctrl+U` | Paste line |
| `Ctrl+W` | Search for text |
| `Alt+/` | Go to end of file |
| `Alt+\` | Go to beginning of file |
| `Ctrl+_` | Go to specific line number |
| `Ctrl+C` | Show cursor position |
| `Ctrl+J` | Justify paragraph |
| `Ctrl+/` | Replace text |
| `Ctrl+T` | Check spelling |
| `Ctrl+R` | Insert another file |

## Vim Editor Modes

| Mode | Description | How to Enter |
|------|-------------|-------------|
| Normal | Default mode for navigation and commands | Press `Esc` |
| Insert | For inserting/editing text | Press `i`, `I`, `a`, `A`, `o`, or `O` in Normal mode |
| Visual | For selecting text | Press `v`, `V`, or `Ctrl+v` in Normal mode |
| Command | For executing commands | Type `:` in Normal mode |

## Vim Basic Commands

| Command | Description |
|---------|-------------|
| `:w` | Save file |
| `:q` | Quit (fails if unsaved changes) |
| `:q!` | Quit and discard unsaved changes |
| `:wq` or `ZZ` | Save and quit |
| `/pattern` | Search forward for pattern |
| `?pattern` | Search backward for pattern |
| `n` | Repeat search in same direction |
| `N` | Repeat search in opposite direction |
| `dd` | Delete current line |
| `yy` | Copy (yank) current line |
| `p` | Paste after cursor |
| `P` | Paste before cursor |
| `u` | Undo last change |
| `Ctrl+r` | Redo |
| `G` | Go to last line |
| `gg` | Go to first line |
| `:line_number` | Go to specific line |
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `o` | Open new line below |
| `O` | Open new line above |

## File Finding and Searching

| Command | Description | Example |
|---------|-------------|---------|
| `find` | Search for files in directory | `find /home -name "*.txt"` |
| `locate` | Find files by name (uses index) | `locate filename` |
| `grep` | Search inside files | `grep -r "text" /path` |
| `which` | Show full path of command | `which python` |
| `whereis` | Locate binary, source, manual | `whereis bash` |

## File Permissions Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file permissions | `chmod 755 script.sh` |
| `chown` | Change file owner | `chown user:group file.txt` |
| `umask` | Set default permissions | `umask 022` | 