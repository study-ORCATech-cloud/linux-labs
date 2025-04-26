# LAB14 - Environment Variables and Profiles Solutions

Below are the solutions to the environment variables and profiles exercises. Remember to try solving them on your own first!

## Exercise 1: Understanding Environment Variables

### Solution:

1. Display all current environment variables:
   ```bash
   printenv
   # OR
   env
   ```

2. Display only the PATH environment variable and count directories:
   ```bash
   echo $PATH
   
   # Count directories in PATH
   echo $PATH | tr ':' '\n' | wc -l
   
   # View directories one per line
   echo $PATH | tr ':' '\n'
   ```

3. Display the current shell:
   ```bash
   echo $SHELL
   ```

4. Find variables for username and home directory:
   ```bash
   echo "Username: $USER"
   echo "Home directory: $HOME"
   ```

5. Find where temporary files are stored:
   ```bash
   echo $TMPDIR
   # If TMPDIR isn't set, the default is usually /tmp
   echo "/tmp is the default location"
   ```

## Exercise 2: Creating and Using Environment Variables

### Solution:

1. Create the MY_NAME variable:
   ```bash
   export MY_NAME="Your Name"
   ```

2. Create the CURRENT_PROJECT variable:
   ```bash
   export CURRENT_PROJECT="Linux Environment Lab"
   ```

3. Create the PROJECT_PATH variable:
   ```bash
   export PROJECT_PATH="$HOME/projects"
   
   # Create the directory if it doesn't exist
   mkdir -p $PROJECT_PATH
   ```

4. Display a message using all variables:
   ```bash
   echo "Hello, $MY_NAME! You are working on $CURRENT_PROJECT in $PROJECT_PATH"
   ```

5. Check if variables exist in a new shell:
   
   After opening a new terminal window or tab:
   ```bash
   echo $MY_NAME
   echo $CURRENT_PROJECT
   echo $PROJECT_PATH
   ```
   
   The variables don't appear in the new shell because environment variables set with `export` are only available in the current shell session and its children, not in new independent shell sessions.

## Exercise 3: Making Environment Variables Permanent

### Solution:

1. Edit `.bashrc` to add environment variables:
   ```bash
   echo 'export MY_NAME="Your Name"' >> ~/.bashrc
   echo 'export CURRENT_PROJECT="Linux Environment Lab"' >> ~/.bashrc
   echo 'export PROJECT_PATH="$HOME/projects"' >> ~/.bashrc
   ```

2. Add BACKUP_DIR to `.bashrc`:
   ```bash
   echo 'export BACKUP_DIR="$HOME/backups"' >> ~/.bashrc
   echo 'mkdir -p $BACKUP_DIR' >> ~/.bashrc
   ```

3. Apply changes immediately:
   ```bash
   source ~/.bashrc
   # OR
   . ~/.bashrc
   ```

4. Verify that environment variables are set:
   ```bash
   echo $MY_NAME
   echo $CURRENT_PROJECT
   echo $PROJECT_PATH
   echo $BACKUP_DIR
   ```

5. Create a new shell session and verify:
   
   After opening a new terminal window or tab:
   ```bash
   echo $MY_NAME
   echo $CURRENT_PROJECT
   echo $PROJECT_PATH
   echo $BACKUP_DIR
   ```
   
   The variables should now be available in the new session because they're set in `.bashrc`, which is loaded for each new interactive shell.

## Exercise 4: Understanding Profile Files

### Solution:

1. List profile files in your home directory:
   ```bash
   ls -la ~ | grep -E '\.(profile|bash)'
   ```
   
   This should show files like `.profile`, `.bash_profile`, `.bashrc`, `.bash_logout`, etc.

2. Examine `/etc/profile`:
   ```bash
   less /etc/profile
   ```
   
   Summary: `/etc/profile` is a system-wide initialization file executed for login shells. It sets up environment variables, default permissions (umask), and runs scripts in the `/etc/profile.d/` directory to set up the system environment for all users.

3. Compare profile files:
   ```bash
   # View each file
   [[ -f ~/.bash_profile ]] && less ~/.bash_profile
   [[ -f ~/.profile ]] && less ~/.profile
   less ~/.bashrc
   ```
   
   - `.bash_profile`: Executed for login shells when using bash. Typically sets up environment variables and runs `.bashrc`.
   - `.profile`: Executed for login shells when using any POSIX-compatible shell. Used for setting environment variables.
   - `.bashrc`: Executed for interactive non-login bash shells. Used for aliases, functions, prompt settings, etc.

4. Determine which files are executed:
   
   Login shell (when you log in to the system):
   1. `/etc/profile`
   2. The first file found from: `~/.bash_profile`, `~/.bash_login`, `~/.profile`
   
   Interactive non-login shell (new terminal):
   1. `/etc/bash.bashrc` (on some distributions)
   2. `~/.bashrc`

5. Create a script to be executed by `.bashrc`:
   ```bash
   # Create the script
   echo '#!/bin/bash' > ~/lab_complete.sh
   echo 'echo "Profile files lab completed"' >> ~/lab_complete.sh
   chmod +x ~/lab_complete.sh
   
   # Add to .bashrc
   echo '~/lab_complete.sh' >> ~/.bashrc
   
   # Apply changes
   source ~/.bashrc
   ```

## Exercise 5: PATH Management

### Solution:

1. Create a bin directory:
   ```bash
   mkdir -p ~/bin
   ```

2. Add the directory to PATH permanently:
   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Create a simple shell script:
   ```bash
   cat > ~/bin/hello << 'EOF'
   #!/bin/bash
   echo "Hello from your personal bin directory!"
   echo "Current time: $(date)"
   echo "Running as user: $(whoami)"
   EOF
   ```

4. Make the script executable:
   ```bash
   chmod +x ~/bin/hello
   ```

5. Test the script from any directory:
   ```bash
   cd /tmp
   hello
   ```
   
   The script should run without specifying the full path because `~/bin` is now in your PATH.

## Exercise 6: Custom Shell Prompt

### Solution:

1. Examine the current prompt:
   ```bash
   echo $PS1
   ```

2. Modify `.bashrc` to create a custom prompt:
   ```bash
   # Backup existing PS1
   echo '# Original PS1 value' >> ~/.bashrc
   echo "# PS1='$PS1'" >> ~/.bashrc
   
   # Add new custom prompt
   echo 'export PS1="\[\e[32m\]\u\[\e[0m\]@\h:\[\e[34m\]\w\[\e[0m\] [\t]\$ "' >> ~/.bashrc
   ```

3. Apply the changes:
   ```bash
   source ~/.bashrc
   ```
   
   This prompt includes username in green, the hostname, the current directory in blue, and the current time in square brackets.

4. Create another custom prompt:
   ```bash
   # Add this to .bashrc
   create_custom_prompt() {
     local exit_status=$?
     local file_count=$(ls -1 | wc -l)
     PS1="\[\e[36m\]\w\[\e[0m\] [Files: $file_count, Exit: $exit_status]\n\$ "
   }
   
   export PROMPT_COMMAND=create_custom_prompt
   ```
   
   Add this to `.bashrc` and then apply with `source ~/.bashrc`

5. Test the custom prompts in different directories:
   ```bash
   cd ~
   ls
   cd /etc
   ls
   cd /tmp
   ls
   ```

## Exercise 7: Cleanup

### Solution:

1. Backup modified profile files:
   ```bash
   cp ~/.bashrc ~/.bashrc.lab14.bak
   [[ -f ~/.profile ]] && cp ~/.profile ~/.profile.lab14.bak
   [[ -f ~/.bash_profile ]] && cp ~/.bash_profile ~/.bash_profile.lab14.bak
   ```

2. Remove temporary environment variables:
   ```bash
   unset MY_NAME
   unset CURRENT_PROJECT
   unset PROJECT_PATH
   unset BACKUP_DIR
   ```

3. Restore original prompt settings (if desired):
   ```bash
   # Edit .bashrc and remove or comment out PS1 settings
   # Or restore from backup
   cp ~/.bashrc.lab14.bak ~/.bashrc
   source ~/.bashrc
   ```

4. Keep or remove permanent variables:
   
   To remove permanent variables, edit `~/.bashrc` with a text editor and remove the lines containing the `export` statements for these variables. Then apply the changes with `source ~/.bashrc`.

## Bonus Challenge: Environment Variable Manager Script

```bash
#!/bin/bash

# env_manager.sh - Manage environment variables in profile files
# Usage: ./env_manager.sh [list|add|remove|search|backup]

# Configuration
BACKUP_DIR="$HOME/env_backups"
PROFILE_FILE="$HOME/.bashrc"  # Default profile file to modify
mkdir -p "$BACKUP_DIR"

# Function to backup a profile file
backup_profile() {
    local file="$1"
    local backup_file="$BACKUP_DIR/$(basename $file).$(date +%Y%m%d_%H%M%S).bak"
    
    if [[ -f "$file" ]]; then
        cp "$file" "$backup_file"
        echo "Backup created: $backup_file"
        return 0
    else
        echo "Error: File $file does not exist."
        return 1
    fi
}

# Function to list all environment variables
list_env_vars() {
    echo "Current environment variables:"
    env | sort
}

# Function to add a new environment variable
add_env_var() {
    local var_name="$1"
    local var_value="$2"
    
    if [[ -z "$var_name" || -z "$var_value" ]]; then
        echo "Error: Variable name and value are required."
        echo "Usage: $0 add VARIABLE_NAME VARIABLE_VALUE"
        return 1
    fi
    
    # Check if the variable already exists in the profile file
    if grep -q "export $var_name=" "$PROFILE_FILE"; then
        echo "Variable $var_name already exists in $PROFILE_FILE."
        echo "Current value in the file:"
        grep "export $var_name=" "$PROFILE_FILE"
        read -p "Do you want to update it? (y/n): " confirm
        
        if [[ "$confirm" != "y" ]]; then
            echo "Operation cancelled."
            return 0
        fi
        
        # Backup before modification
        backup_profile "$PROFILE_FILE"
        
        # Update the variable
        sed -i "s|export $var_name=.*|export $var_name=\"$var_value\"|" "$PROFILE_FILE"
        echo "Variable $var_name updated in $PROFILE_FILE."
    else
        # Backup before modification
        backup_profile "$PROFILE_FILE"
        
        # Add the variable
        echo "export $var_name=\"$var_value\"" >> "$PROFILE_FILE"
        echo "Variable $var_name added to $PROFILE_FILE."
    fi
    
    # Set the variable in the current environment
    export "$var_name=$var_value"
    echo "Variable $var_name set in current session."
}

# Function to remove an environment variable
remove_env_var() {
    local var_name="$1"
    
    if [[ -z "$var_name" ]]; then
        echo "Error: Variable name is required."
        echo "Usage: $0 remove VARIABLE_NAME"
        return 1
    fi
    
    # Check if the variable exists in the profile file
    if grep -q "export $var_name=" "$PROFILE_FILE"; then
        # Backup before modification
        backup_profile "$PROFILE_FILE"
        
        # Remove the variable
        sed -i "/export $var_name=/d" "$PROFILE_FILE"
        echo "Variable $var_name removed from $PROFILE_FILE."
        
        # Unset the variable in current session
        unset "$var_name"
        echo "Variable $var_name unset in current session."
    else
        echo "Variable $var_name not found in $PROFILE_FILE."
    fi
}

# Function to search for a specific environment variable
search_env_var() {
    local search_term="$1"
    
    if [[ -z "$search_term" ]]; then
        echo "Error: Search term is required."
        echo "Usage: $0 search SEARCH_TERM"
        return 1
    fi
    
    echo "Searching for '$search_term' in current environment:"
    env | grep -i "$search_term" || echo "No matches found in current environment."
    
    echo -e "\nSearching for '$search_term' in profile files:"
    
    # Search in common profile files
    for file in ~/.bashrc ~/.profile ~/.bash_profile; do
        if [[ -f "$file" ]]; then
            echo -e "\nIn $file:"
            grep -i "$search_term" "$file" || echo "No matches found in $file."
        fi
    done
    
    # Search in system profile files
    echo -e "\nIn system profile files:"
    if [[ -f /etc/profile ]]; then
        echo "In /etc/profile:"
        sudo grep -i "$search_term" /etc/profile || echo "No matches found in /etc/profile."
    fi
}

# Main execution
case "$1" in
    list)
        list_env_vars
        ;;
    add)
        add_env_var "$2" "$3"
        ;;
    remove)
        remove_env_var "$2"
        ;;
    search)
        search_env_var "$2"
        ;;
    backup)
        if [[ -z "$2" ]]; then
            echo "Backing up default profile file: $PROFILE_FILE"
            backup_profile "$PROFILE_FILE"
        else
            echo "Backing up specified file: $2"
            backup_profile "$2"
        fi
        ;;
    *)
        echo "Environment Variable Manager"
        echo "Usage: $0 [command]"
        echo
        echo "Commands:"
        echo "  list                     List all environment variables"
        echo "  add VARIABLE VALUE       Add or update environment variable"
        echo "  remove VARIABLE          Remove environment variable"
        echo "  search TERM              Search for environment variable"
        echo "  backup [FILE]            Backup profile file (default: $PROFILE_FILE)"
        echo
        echo "Examples:"
        echo "  $0 add MY_VAR 'my value'"
        echo "  $0 search PATH"
        echo "  $0 backup ~/.profile"
        ;;
esac

exit 0
```

To use the script:
```bash
chmod +x env_manager.sh
./env_manager.sh list
./env_manager.sh add TEST_VAR "test value"
./env_manager.sh search TEST
./env_manager.sh remove TEST_VAR
./env_manager.sh backup
```

Remember, these solutions are provided for reference. It's best to first try solving the exercises on your own to get the most benefit from the learning experience. 