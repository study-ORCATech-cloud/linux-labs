# SSH Configuration and Hardening - Exercise Solutions

Below are the solutions to the exercises in the ssh_exercises.md file. Use these to verify your work or if you get stuck.

## Exercise 1: SSH Key Generation and Authentication

### Task 1.1: Generate SSH Key Pair
```bash
# Generate an SSH key pair with 4096 bit RSA encryption
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_lab
# Enter a strong passphrase when prompted
```

### Task 1.2: Examine the Generated SSH Keys
```bash
# Examine the public key file generated
cat ~/.ssh/id_rsa_lab.pub

# List all SSH keys in your .ssh directory
ls -la ~/.ssh/
```

### Task 1.3: Copy Public Key to Server
```bash
# Copy your public key to the server
ssh-copy-id -i ~/.ssh/id_rsa_lab.pub username@hostname

# If working locally (on the same machine)
ssh-copy-id -i ~/.ssh/id_rsa_lab.pub localhost
```

## Exercise 2: Configure SSH Client

### Task 2.1: Create SSH Config for Easy Connections
```bash
# Create or edit SSH config file
nano ~/.ssh/config
```

Add the following configuration:
```
Host myserver
    HostName 192.168.1.100
    User myusername
    IdentityFile ~/.ssh/id_rsa_lab
    Port 22
```

### Task 2.2: Test SSH Connection Using Config
```bash
# Connect using the defined host
ssh myserver

# Verify connecting with key, not password
ssh -v myserver
# Look for "Offering public key" and "Server accepts key" in the output
```

## Exercise 3: Harden SSH Server Configuration

### Task 3.1: Create a Backup of SSH Server Configuration
```bash
# Backup the SSH server configuration file
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

### Task 3.2: Edit SSH Server Configuration
```bash
# Edit the SSH configuration file
sudo nano /etc/ssh/sshd_config
```

Make the following changes:
```
# Disable password authentication
PasswordAuthentication no

# Disable root login
PermitRootLogin no

# Limit SSH access to specific users
AllowUsers yourusername

# Set a non-standard port
Port 2222

# Change login grace time
LoginGraceTime 30

# Set maximum authentication attempts
MaxAuthTries 3

# Enable strict mode
StrictModes yes

# Ensure public key authentication is enabled
PubkeyAuthentication yes
```

### Task 3.3: Validate SSH Configuration
```bash
# Check the SSH configuration file for syntax errors
sudo sshd -t
```

### Task 3.4: Apply the Changes
```bash
# Restart the SSH service
sudo systemctl restart sshd

# Check the status to ensure it restarted correctly
sudo systemctl status sshd
```

## Exercise 4: Configure SSH Firewall Rules

### Task 4.1: Update Firewall for Custom SSH Port
```bash
# Allow SSH on custom port
sudo ufw allow 2222/tcp

# Remove rule for standard SSH port if it exists
sudo ufw delete allow ssh

# Verify the firewall rules
sudo ufw status
```

## Exercise 5: Additional SSH Hardening

### Task 5.1: Configure SSH Key-Only Authentication
```bash
# Verify that password authentication is disabled
grep PasswordAuthentication /etc/ssh/sshd_config

# Try to connect using a password (should fail)
ssh -o PubkeyAuthentication=no yourusername@localhost -p 2222
# This should fail with "Permission denied (publickey)"

# Connect using your SSH key
ssh -i ~/.ssh/id_rsa_lab yourusername@localhost -p 2222
```

### Task 5.2: Set Up SSH Idle Timeout
```bash
# Edit SSH configuration
sudo nano /etc/ssh/sshd_config
```

Add the following lines:
```
# Disconnect inactive sessions after 5 minutes
ClientAliveInterval 300
ClientAliveCountMax 0
```

```bash
# Restart SSH to apply changes
sudo systemctl restart sshd
```

### Task 5.3: Disable Unused SSH Features
```bash
# Edit SSH configuration
sudo nano /etc/ssh/sshd_config
```

Add or modify the following lines:
```
# Disable X11 forwarding
X11Forwarding no

# Disable TCP forwarding
AllowTcpForwarding no

# Disable agent forwarding
AllowAgentForwarding no
```

```bash
# Restart SSH to apply changes
sudo systemctl restart sshd
```

## Exercise 6: SSH Login Notifications

### Task 6.1: Configure Login Notifications
```bash
# Create a custom SSH banner
sudo nano /etc/ssh/banner
```

Add a banner message:
```
*******************************************************************
*                      AUTHORIZED ACCESS ONLY                      *
* This system is restricted to authorized users for legitimate     *
* business purposes only. Unauthorized access is prohibited.       *
*******************************************************************
```

```bash
# Configure SSH to display the banner
sudo nano /etc/ssh/sshd_config
```

Add the line:
```
Banner /etc/ssh/banner
```

```bash
# Configure the MOTD
sudo nano /etc/update-motd.d/10-sshinfo
```

Create a script to show system information:
```bash
#!/bin/bash
echo "Welcome to $(hostname)"
echo "System information as of $(date)"
echo "--------------------------------------"
echo "Kernel:    $(uname -r)"
echo "Uptime:    $(uptime -p)"
echo "CPU Load:  $(cat /proc/loadavg | awk '{print $1, $2, $3}')"
echo "Memory:    $(free -m | awk '/Mem/{printf("%.2f%%", $3/$2*100)}')"
echo "Processes: $(ps aux | wc -l)"
echo "--------------------------------------"
```

```bash
# Make the file executable
sudo chmod +x /etc/update-motd.d/10-sshinfo

# Restart SSH service
sudo systemctl restart sshd
```

## Cleanup Instructions
```bash
# If you changed the SSH port, revert to standard port 22
sudo nano /etc/ssh/sshd_config
# Change 'Port 2222' to 'Port 22'

# Update firewall rules to allow standard SSH port
sudo ufw allow ssh
sudo ufw delete allow 2222/tcp

# Restart SSH service to apply changes
sudo systemctl restart sshd
```

## Important Notes

1. **Never lock yourself out** - Always keep an existing SSH session open when applying security changes.

2. **Test all changes thoroughly** before implementing in production:
```bash
# Test SSH configuration before restarting
sudo sshd -t
```

3. **Create backups** of important configuration files:
```bash
# Create backup before editing
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

4. **When changing SSH port**, update all relevant tools and configurations:
   - Update firewall rules
   - Update monitoring tools
   - Update backup systems
   - Update any automation that uses SSH

5. **For key management**, consider these additional best practices:
   - Use separate keys for different servers/purposes
   - Rotate keys periodically
   - Revoke compromised keys immediately 