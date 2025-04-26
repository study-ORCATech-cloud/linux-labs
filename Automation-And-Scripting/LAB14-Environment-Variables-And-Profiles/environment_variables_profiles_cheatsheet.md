# LAB14 - Environment Variables and Profiles Cheatsheet

This cheatsheet provides a quick reference for working with environment variables and profile files in Linux.

## Environment Variables Basics

| Command | Description | Example |
|---------|-------------|---------|
| `printenv` | Display all environment variables | `printenv` |
| `env` | Another way to display environment variables | `env` |
| `echo $VARIABLE` | Display the value of a specific variable | `echo $HOME` |
| `export VAR=value` | Create or modify an environment variable | `export EDITOR=nano` |
| `unset VARIABLE` | Remove an environment variable | `unset EDITOR` |
| `VARIABLE=value command` | Set a variable for a single command | `DEBUG=true ./script.sh` |
| `env -i command` | Run a command with an empty environment | `env -i bash -c 'echo $HOME'` |

## Common Environment Variables

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `HOME` | User's home directory | `/home/username` |
| `USER` | Current username | `username` |
| `SHELL` | Path to current shell | `/bin/bash` |
| `PATH` | List of directories to search for executable files | `/usr/local/bin:/usr/bin:/bin` |
| `PWD` | Current working directory | `/home/username/documents` |
| `LANG` | System language and locale | `en_US.UTF-8` |
| `TERM` | Terminal type | `xterm-256color` |
| `EDITOR` | Default text editor | `nano` or `vim` |
| `DISPLAY` | X display server | `:0` |
| `HISTSIZE` | Maximum commands stored in history | `1000` |
| `HISTFILESIZE` | Maximum lines stored in history file | `2000` |
| `TMPDIR` | Directory for temporary files | `/tmp` |

## Manipulating the PATH Variable

| Task | Command |
|------|---------|
| View PATH | `echo $PATH` |
| Count directories in PATH | `echo $PATH \| tr ':' '\n' \| wc -l` |
| List PATH directories one per line | `echo $PATH \| tr ':' '\n'` |
| Add directory to start of PATH | `export PATH=/new/dir:$PATH` |
| Add directory to end of PATH | `export PATH=$PATH:/new/dir` |
| Add directory to PATH if not already there | `if [[ ":$PATH:" != *":/new/dir:"* ]]; then export PATH="$PATH:/new/dir"; fi` |

## Profile Files and Startup Order

| File | When Executed | Purpose |
|------|---------------|---------|
| `/etc/profile` | System-wide, login | System-wide environment and startup programs |
| `/etc/bash.bashrc` | System-wide, interactive | System-wide functions and aliases |
| `~/.bash_profile` | User-specific, login | Personal environment setup, runs `.bashrc` |
| `~/.bashrc` | User-specific, interactive | Personal shell settings, aliases, functions |
| `~/.profile` | User-specific, login | Alternative to `.bash_profile` |
| `~/.bash_login` | User-specific, login | Used if `.bash_profile` not found |
| `~/.bash_logout` | User-specific, logout | Commands to run when logging out |

## Customizing the Shell Prompt (PS1)

| Escape Sequence | Result |
|-----------------|--------|
| `\u` | Username |
| `\h` | Hostname (short) |
| `\H` | Hostname (FQDN) |
| `\w` | Current working directory with $HOME as ~ |
| `\W` | Base name of current working directory |
| `\$` | # if root, $ otherwise |
| `\d` | Date in "Weekday Month Date" format |
| `\t` | Time in 24-hour format |
| `\T` | Time in 12-hour format |
| `\@` | Time in 12-hour am/pm format |
| `\j` | Number of jobs managed by the shell |
| `\!` | History number of the command |
| `\#` | Command number of the command |
| `\[` and `\]` | Begin and end non-printing characters (like colors) |

## ANSI Color Codes for Prompt

| Color Code | Text Color |
|------------|------------|
| `\e[30m` | Black |
| `\e[31m` | Red |
| `\e[32m` | Green |
| `\e[33m` | Yellow |
| `\e[34m` | Blue |
| `\e[35m` | Magenta |
| `\e[36m` | Cyan |
| `\e[37m` | White |
| `\e[0m` | Reset to Default |
| `\e[1m` | Bold |

Example colored prompt:
```bash
PS1='\[\e[32m\]\u@\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '
```

## Working with Profile Files

| Task | Command |
|------|---------|
| Edit .bashrc | `nano ~/.bashrc` |
| Apply changes without logging out | `source ~/.bashrc` or `. ~/.bashrc` |
| Add alias to .bashrc | `echo "alias ll='ls -la'" >> ~/.bashrc` |
| Add environment variable to .bashrc | `echo "export PROJECT_PATH=~/projects" >> ~/.bashrc` |
| Backup a profile file | `cp ~/.bashrc ~/.bashrc.bak` |
| Create a custom prompt | `echo 'export PS1="\u@\h:\w\$ "' >> ~/.bashrc` |

## Best Practices

1. **Keep it organized**: Group related settings together in your profile files
2. **Add comments**: Document what your variables and settings are for
3. **Use conditional checks**: Ensure directories exist before adding to PATH
4. **Use functions**: For complex operations in profile files
5. **Check return values**: Especially for important environment setup
6. **Be cautious with system-wide settings**: They affect all users
7. **Backup before editing**: Always backup profile files before major changes
8. **Avoid exporting large values**: Environment variables are copied to child processes

## Debugging Profile Problems

| Issue | Solution |
|-------|----------|
| Changes not taking effect | Source the file (`source ~/.bashrc`) or start a new shell |
| Script errors on login | Debug with `bash -x ~/.bashrc` |
| PATH problems | Check path with `which command` or `type command` |
| Slow shell startup | Add `set -x` at the top and `set +x` at the bottom of profile files |
| Finding where a variable is set | Use `grep -r "VARIABLE" ~/.*` and `/etc/.*` | 