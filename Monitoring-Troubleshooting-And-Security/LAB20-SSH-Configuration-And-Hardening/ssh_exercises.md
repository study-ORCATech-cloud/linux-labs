# SSH Configuration and Hardening - Practical Exercises

This file contains hands-on exercises to practice implementing secure SSH configurations. Complete each TODO task to strengthen your server's SSH security.

## Exercise 1: SSH Key Generation and Authentication

### Task 1.1: Generate SSH Key Pair
```bash
# TODO: Generate an SSH key pair with the following specifications:
# - RSA type
# - 4096 bits
# - Custom key name (e.g., id_rsa_lab)
# - A passphrase for extra security

```

### Task 1.2: Examine the Generated SSH Keys
```bash
# TODO: Examine the public key file you generated
# TODO: List all SSH keys in your .ssh directory

```

### Task 1.3: Copy Public Key to Server
```bash
# TODO: Use ssh-copy-id to copy your public key to the server
# (If you're working on a single machine, you can copy to localhost)

```

## Exercise 2: Configure SSH Client

### Task 2.1: Create SSH Config for Easy Connections
Create or edit the SSH config file:
```bash
# TODO: Create/edit the ~/.ssh/config file to add a host entry with:
# - Hostname (your server IP or localhost)
# - User (your username)
# - Identity file (path to your private key)
# - Optional: Port (if using non-standard port)

```

### Task 2.2: Test SSH Connection Using Config
```bash
# TODO: Connect to your server using the host defined in the config
# TODO: Verify that you're connecting with your key and not a password

```

## Exercise 3: Harden SSH Server Configuration

### Task 3.1: Create a Backup of SSH Server Configuration
```bash
# TODO: Create a backup of the SSH server configuration file

```

### Task 3.2: Edit SSH Server Configuration
Edit the SSH configuration file:
```bash
# TODO: Edit the SSH server configuration to implement the following:
# - Disable password authentication
# - Disable root login
# - Limit SSH access to specific users
# - Set a non-standard port (e.g., 2222)
# - Change login grace time to 30 seconds
# - Set maximum authentication attempts to 3
# - Enable strict mode
# - Enable public key authentication

```

### Task 3.3: Validate SSH Configuration
```bash
# TODO: Check the SSH configuration file for syntax errors

```

### Task 3.4: Apply the Changes
```bash
# TODO: Restart the SSH service to apply the configuration changes
# Note: Keep your current session open in case of issues

```

## Exercise 4: Configure SSH Firewall Rules

### Task 4.1: Update Firewall for Custom SSH Port
```bash
# TODO: Configure UFW to allow SSH on the custom port you specified
# TODO: Remove the rule for the standard SSH port if it exists
# TODO: Verify the firewall rules

```

## Exercise 5: Additional SSH Hardening

### Task 5.1: Configure SSH Key-Only Authentication
```bash
# TODO: Verify that password authentication is disabled
# TODO: Try to connect using a password (should fail)
# TODO: Connect using your SSH key

```

### Task 5.2: Set Up SSH Idle Timeout
```bash
# TODO: Configure SSH to disconnect inactive sessions after 5 minutes by setting:
# - ClientAliveInterval
# - ClientAliveCountMax

```

### Task 5.3: Disable Unused SSH Features
```bash
# TODO: Disable the following SSH features:
# - X11 forwarding
# - TCP forwarding
# - Agent forwarding

```

## Exercise 6: SSH Login Notifications

### Task 6.1: Configure Login Notifications
```bash
# TODO: Create a custom SSH banner message in /etc/ssh/banner
# TODO: Configure SSH to display the banner at login
# TODO: Configure the MOTD (Message of the Day) to show system information

```

## Validation Checklist

- [ ] SSH key pair successfully generated
- [ ] SSH key authentication working
- [ ] Password authentication disabled
- [ ] Root login disabled
- [ ] Custom SSH port configured and accessible
- [ ] Firewall rules updated for the custom port
- [ ] Idle timeout configured
- [ ] Unnecessary SSH features disabled
- [ ] SSH banner configured

## Cleanup Instructions
```bash
# TODO: If you changed the SSH port, revert to the standard port 22
# TODO: Update firewall rules to allow standard SSH port
# TODO: Restart SSH service to apply changes

```

> ⚠️ **Important**: Always maintain at least one active terminal session when making SSH configuration changes, to avoid being locked out of your system! 