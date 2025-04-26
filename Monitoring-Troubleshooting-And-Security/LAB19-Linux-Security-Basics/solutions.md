# Linux Security Basics - Exercise Solutions

Below are the solutions to the exercises in the security_exercises.md file. Use these to verify your work or if you get stuck.

## Exercise 1: User Password Policy Management

### Task 1.1: Configure Password Expiration
```bash
# Set maximum password age to 90 days
sudo chage -M 90 $USER

# Set minimum password age to 7 days
sudo chage -m 7 $USER

# Set password expiration warning to 14 days
sudo chage -W 14 $USER
```

### Task 1.2: Check Current Password Policies
```bash
# View password aging information for your user
sudo chage -l $USER
```

## Exercise 2: User and Group Management

### Task 2.1: Create a Limited User
```bash
# Create a new user with no home directory and no login shell
sudo useradd -M -s /sbin/nologin securitytester

# Alternative method:
# sudo useradd --no-create-home --shell /usr/sbin/nologin securitytester
```

### Task 2.2: Create a Security Group and Add User
```bash
# Create a new group called 'secaudit'
sudo groupadd secaudit

# Add the securitytester user to this group
sudo usermod -aG secaudit securitytester

# Verify the user is in the group
groups securitytester
```

### Task 2.3: Lock an Unused Account
```bash
# Lock the securitytester account
sudo usermod -L securitytester

# Verify that the account is locked (check for ! in front of password hash)
sudo grep securitytester /etc/shadow
```

## Exercise 3: Secure SSH Configuration

### Task 3.1: SSH Configuration Hardening
```bash
# Edit the SSH configuration file
sudo nano /etc/ssh/sshd_config

# Make the following changes:
# PermitRootLogin no
# Protocol 2
# MaxAuthTries 3
# ClientAliveInterval 300
# ClientAliveCountMax 0
# PermitEmptyPasswords no
```

### Task 3.2: Restart SSH Service
```bash
# Restart the SSH service to apply the changes
sudo systemctl restart sshd

# Verify SSH is running with the new configuration
sudo systemctl status sshd
```

## Exercise 4: Basic Firewall Configuration

### Task 4.1: Configure UFW (Uncomplicated Firewall)
```bash
# Install UFW if not already installed
sudo apt update
sudo apt install ufw -y

# Set default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (port 22)
sudo ufw allow ssh

# Allow HTTP (port 80)
sudo ufw allow http

# Enable the firewall
sudo ufw enable
```

### Task 4.2: Check Firewall Status
```bash
# Check the status of the firewall to verify your rules
sudo ufw status verbose
```

## Exercise 5: Service Management

### Task 5.1: List All Running Services
```bash
# List all running services on your system
sudo systemctl list-units --type=service --state=running

# Alternative methods:
# sudo service --status-all | grep '[ + ]'
# sudo systemctl --type=service
```

### Task 5.2: Disable Unnecessary Services
```bash
# Example of disabling a commonly unnecessary service (cups - printing service)
# First check if it's running
sudo systemctl status cups

# If running and not needed, disable and stop
sudo systemctl stop cups
sudo systemctl disable cups

# For a more aggressive approach, mask the service
sudo systemctl mask cups
```

## Exercise 6: File Permissions Audit

### Task 6.1: Find SUID/SGID Files
```bash
# Find all files with SUID permissions set
sudo find / -perm -4000 -type f 2>/dev/null

# Find all files with SGID permissions set
sudo find / -perm -2000 -type f 2>/dev/null
```

### Task 6.2: Secure Important Configuration Files
```bash
# Check current permissions
ls -l /etc/passwd /etc/shadow /etc/ssh/sshd_config

# Set appropriate permissions if needed
sudo chmod 644 /etc/passwd
sudo chmod 640 /etc/shadow
sudo chmod 600 /etc/ssh/sshd_config

# Verify the changes
ls -l /etc/passwd /etc/shadow /etc/ssh/sshd_config
```

## Cleanup Instructions
```bash
# Remove the securitytester user
sudo userdel securitytester

# Remove the secaudit group
sudo groupdel secaudit

# Reset any changed SSH configurations (if needed)
sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
sudo systemctl restart sshd

# Disable the firewall (in training environment only)
sudo ufw disable
```

## Important Notes

1. Always make backups of configuration files before editing them:
```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

2. When locking user accounts, make sure not to lock yourself out:
```bash
# Never do this to your own admin account or the only admin account
sudo usermod -L your_admin_account  # DON'T DO THIS
```

3. Be careful with firewall rules to avoid locking yourself out:
```bash
# When using SSH, always add this rule BEFORE enabling the firewall
sudo ufw allow ssh
```

4. After making security changes, test thoroughly to ensure system accessibility and functionality. 