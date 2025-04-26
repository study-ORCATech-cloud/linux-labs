# SSH Configuration and Hardening Cheatsheet

This is a quick reference for SSH commands, configuration options, and hardening techniques covered in this lab.

## SSH Key Management

| Command | Description | Example |
|---------|-------------|---------|
| `ssh-keygen` | Generate SSH key pair | `ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_lab` |
| `ssh-copy-id` | Copy public key to server | `ssh-copy-id -i ~/.ssh/id_rsa_lab.pub user@server` |
| `ssh-add` | Add key to SSH agent | `ssh-add ~/.ssh/id_rsa_lab` |
| `ssh-keygen -l` | Display key fingerprint | `ssh-keygen -l -f ~/.ssh/id_rsa_lab.pub` |
| `ssh-keygen -p` | Change passphrase | `ssh-keygen -p -f ~/.ssh/id_rsa_lab` |

## SSH Client Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ssh` | Connect to server | `ssh user@server` |
| `ssh -i` | Connect with specific key | `ssh -i ~/.ssh/id_rsa_lab user@server` |
| `ssh -p` | Connect to specific port | `ssh -p 2222 user@server` |
| `ssh -v` | Verbose connection info | `ssh -v user@server` |
| `scp` | Secure file copy | `scp file.txt user@server:/path/` |
| `sftp` | SSH file transfer | `sftp user@server` |

## SSH Client Configuration (~/.ssh/config)

```
Host myserver
    HostName 192.168.1.10
    User username
    Port 2222
    IdentityFile ~/.ssh/id_rsa_lab
    IdentitiesOnly yes
    ConnectTimeout 5
    ServerAliveInterval 60
    ServerAliveCountMax 3
    ForwardAgent no
    ForwardX11 no
```

## SSH Server Configuration (/etc/ssh/sshd_config)

### Key Security Settings

| Setting | Recommended Value | Description |
|---------|-------------------|-------------|
| `PasswordAuthentication` | `no` | Disable password login |
| `PermitRootLogin` | `no` | Disable root login |
| `PubkeyAuthentication` | `yes` | Enable key-based authentication |
| `Port` | Non-standard (e.g., 2222) | Change default SSH port |
| `MaxAuthTries` | `3` | Limit authentication attempts |
| `LoginGraceTime` | `30` | Reduce login grace time |
| `AllowUsers` | `user1 user2` | Restrict SSH to specific users |
| `Protocol` | `2` | Use SSH protocol version 2 only |
| `PermitEmptyPasswords` | `no` | Disallow empty passwords |
| `StrictModes` | `yes` | Check file permissions before accepting login |

### Idle Timeout Settings

| Setting | Recommended Value | Description |
|---------|-------------------|-------------|
| `ClientAliveInterval` | `300` | Send null packet to client every 5 min |
| `ClientAliveCountMax` | `0` | Disconnect after no response |

### Feature Restriction Settings

| Setting | Recommended Value | Description |
|---------|-------------------|-------------|
| `X11Forwarding` | `no` | Disable X11 forwarding |
| `AllowTcpForwarding` | `no` | Disable TCP forwarding |
| `AllowAgentForwarding` | `no` | Disable SSH agent forwarding |
| `PermitTunnel` | `no` | Disable tunneling |
| `Banner` | `/etc/ssh/banner` | Display banner on login |

## Firewall Configuration for SSH

### UFW Commands

```bash
# Allow SSH on standard port
sudo ufw allow ssh

# Allow SSH on custom port
sudo ufw allow 2222/tcp

# Remove rule
sudo ufw delete allow ssh

# Check status
sudo ufw status
```

### iptables Commands

```bash
# Allow SSH on standard port
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow SSH on custom port
sudo iptables -A INPUT -p tcp --dport 2222 -j ACCEPT
```

## SSH Service Management

```bash
# Restart SSH service
sudo systemctl restart sshd

# Check SSH service status
sudo systemctl status sshd

# Stop SSH service
sudo systemctl stop sshd

# Start SSH service
sudo systemctl start sshd
```

## SSH Configuration Validation

```bash
# Check SSH config syntax
sudo sshd -t

# Debug SSH connection issues
ssh -vvv user@server

# View SSH login attempts
sudo journalctl -u ssh

# Check listening ports
sudo ss -tuln | grep ssh
```

## SSH Security Best Practices

1. **Use SSH keys instead of passwords**
   - Longer keys (4096 bits) provide better security
   - Always protect private keys with strong passphrases

2. **Keep SSH software updated**
   - Regularly update OpenSSH packages to patch vulnerabilities

3. **Implement defense in depth**
   - Firewall restrictions
   - Fail2ban to prevent brute force attacks
   - Port knocking for additional security layers

4. **Regularly audit SSH access**
   - Monitor logs for suspicious activity
   - Rotate keys periodically
   - Remove unused authorized keys

5. **Use configuration management**
   - Automate secure SSH configuration with tools like Ansible
   - Maintain consistent security settings across servers 