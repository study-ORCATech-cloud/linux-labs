# Linux Security Basics - Practical Exercises

This file contains hands-on exercises to practice implementing basic Linux security measures. Complete each TODO task to strengthen your system's security posture.

## Exercise 1: User Password Policy Management

### Task 1.1: Configure Password Expiration
```bash
# TODO: Use the chage command to set the following password policies for your user:
# - Maximum password age (90 days)
# - Minimum password age (7 days)
# - Password expiration warning (14 days)

```

### Task 1.2: Check Current Password Policies
```bash
# TODO: Use the appropriate command to check the current password aging 
# information for your user

```

## Exercise 2: User and Group Management

### Task 2.1: Create a Limited User
```bash
# TODO: Create a new user with limited permissions
# - Username: securitytester
# - No home directory
# - No login shell

```

### Task 2.2: Create a Security Group and Add User
```bash
# TODO: Create a new group called 'secaudit'
# TODO: Add the securitytester user to this group

```

### Task 2.3: Lock an Unused Account
```bash
# TODO: Lock the securitytester account to prevent login while maintaining the account
# TODO: Verify that the account is locked

```

## Exercise 3: Secure SSH Configuration

### Task 3.1: SSH Configuration Hardening
Edit the SSH configuration file:
```bash
# TODO: Modify the SSH configuration to:
# - Disable root login
# - Use SSH Protocol 2
# - Limit max auth tries to 3
# - Set idle timeout to 300 seconds
# - Disable empty passwords

```

### Task 3.2: Restart SSH Service
```bash
# TODO: Restart the SSH service to apply the changes

```

## Exercise 4: Basic Firewall Configuration

### Task 4.1: Configure UFW (Uncomplicated Firewall)
```bash
# TODO: Install UFW if not already installed
# TODO: Configure UFW to:
#  - Enable the firewall
#  - Allow SSH (port 22)
#  - Allow HTTP (port 80)
#  - Deny all other incoming connections
#  - Allow all outgoing connections

```

### Task 4.2: Check Firewall Status
```bash
# TODO: Check the status of the firewall to verify your rules

```

## Exercise 5: Service Management

### Task 5.1: List All Running Services
```bash
# TODO: List all running services on your system

```

### Task 5.2: Disable Unnecessary Services
```bash
# TODO: Identify at least one unnecessary service
# TODO: Disable and stop this service

```

## Exercise 6: File Permissions Audit

### Task 6.1: Find SUID/SGID Files
```bash
# TODO: Find all files with SUID permissions set
# TODO: Find all files with SGID permissions set

```

### Task 6.2: Secure Important Configuration Files
```bash
# TODO: Check and set appropriate permissions for:
# - /etc/passwd (should be 644)
# - /etc/shadow (should be 600 or 640)
# - /etc/ssh/sshd_config (should be 600)

```

## Validation Checklist

- [ ] Password aging policies configured correctly
- [ ] User account created, added to group, and locked
- [ ] SSH configuration secured
- [ ] Firewall enabled with proper rules
- [ ] Unnecessary services disabled
- [ ] File permissions properly configured

## Cleanup Instructions
```bash
# TODO: Remove the securitytester user
# TODO: Remove the secaudit group
# TODO: Reset any changed SSH configurations if needed
# TODO: Disable the firewall if this is a training environment

```

Remember to never perform these exercises on production systems without proper authorization and testing! 