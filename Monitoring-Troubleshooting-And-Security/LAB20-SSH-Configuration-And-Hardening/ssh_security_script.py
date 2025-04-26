#!/usr/bin/env python3
"""
SSH Security Checker Script

This script performs a security audit of your SSH configuration and provides
recommendations for hardening. It is intended for educational purposes in the
SSH Configuration and Hardening lab.

Usage:
    python3 ssh_security_script.py

Requirements:
    - Python 3.6+
    - Root privileges for some checks (run with sudo)
"""

import os
import subprocess
import sys
import re
import socket
import pwd
import datetime
from pathlib import Path


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error running command: {e}"


def check_if_root():
    """Check if script is run with root privileges."""
    if os.geteuid() != 0:
        print("Warning: Some checks require root privileges. Run with sudo for full results.")
        return False
    return True


def get_ssh_version():
    """Get the installed SSH version."""
    ssh_version = run_command("ssh -V 2>&1")
    return ssh_version


def check_ssh_status():
    """Check if SSH service is running."""
    print_header("SSH SERVICE STATUS")
    
    status = run_command("systemctl is-active sshd 2>/dev/null || echo inactive")
    if status == "active":
        print("✅ SSH server is running")
    else:
        print("⚠️ SSH server is not running")
        return False
    
    # Get SSH listening ports
    ports = []
    port_output = run_command("ss -tuln | grep -E ':(22|2222)' | awk '{print $5}'")
    
    if port_output:
        for line in port_output.splitlines():
            match = re.search(r':(\d+)$', line)
            if match:
                ports.append(match.group(1))
        
        if ports:
            print(f"SSH is listening on port(s): {', '.join(ports)}")
            if '22' in ports:
                print("⚠️ SSH is using the default port (22)")
            else:
                print("✅ SSH is using a non-standard port")
    else:
        print("⚠️ Could not determine SSH listening ports")
    
    return True


def check_ssh_config():
    """Check SSH server configuration."""
    print_header("SSH CONFIGURATION ANALYSIS")
    
    sshd_config_path = "/etc/ssh/sshd_config"
    if not os.path.exists(sshd_config_path):
        print(f"⚠️ SSH configuration file {sshd_config_path} not found")
        return
    
    # Define security settings to check
    security_settings = {
        "PasswordAuthentication": {"recommended": "no", "critical": True},
        "PermitRootLogin": {"recommended": "no", "critical": True},
        "Protocol": {"recommended": "2", "critical": True},
        "PubkeyAuthentication": {"recommended": "yes", "critical": True},
        "MaxAuthTries": {"recommended": "3", "critical": False, "max_value": 4},
        "LoginGraceTime": {"recommended": "30", "critical": False, "max_value": 60},
        "PermitEmptyPasswords": {"recommended": "no", "critical": True},
        "X11Forwarding": {"recommended": "no", "critical": False},
        "AllowTcpForwarding": {"recommended": "no", "critical": False},
        "ClientAliveInterval": {"recommended": "300", "critical": False, "max_value": 600},
        "ClientAliveCountMax": {"recommended": "0", "critical": False, "max_value": 2},
        "StrictModes": {"recommended": "yes", "critical": False}
    }
    
    # Read the SSH config file
    with open(sshd_config_path, 'r') as f:
        config_data = f.read()
    
    # Check each security setting
    for setting, details in security_settings.items():
        pattern = re.compile(r'^(?!#)\s*' + setting + r'\s+(\S+)', re.MULTILINE)
        match = pattern.search(config_data)
        
        if match:
            value = match.group(1)
            
            # Handle numeric comparisons
            if "max_value" in details and value.isdigit() and details["recommended"].isdigit():
                if int(value) <= int(details["max_value"]):
                    print(f"✅ {setting} is set to {value} (acceptable: ≤{details['max_value']})")
                else:
                    symbol = "❌" if details["critical"] else "⚠️"
                    print(f"{symbol} {setting} is set to {value}, recommended: ≤{details['max_value']}")
            # Handle exact match comparison
            elif value == details["recommended"]:
                print(f"✅ {setting} is set to recommended value: {value}")
            else:
                symbol = "❌" if details["critical"] else "⚠️"
                print(f"{symbol} {setting} is set to {value}, recommended: {details['recommended']}")
        else:
            print(f"⚠️ {setting} is not explicitly set in sshd_config")
    
    # Check for AllowUsers/AllowGroups
    allow_users_pattern = re.compile(r'^(?!#)\s*AllowUsers\s+(\S+)', re.MULTILINE)
    allow_groups_pattern = re.compile(r'^(?!#)\s*AllowGroups\s+(\S+)', re.MULTILINE)
    
    if allow_users_pattern.search(config_data) or allow_groups_pattern.search(config_data):
        print("✅ SSH access is restricted to specific users or groups")
    else:
        print("⚠️ No user or group restrictions for SSH access")


def check_key_based_auth():
    """Check for key-based authentication setup."""
    print_header("SSH KEY-BASED AUTHENTICATION")
    
    # Check if ~/.ssh directory exists
    home_dir = str(Path.home())
    ssh_dir = os.path.join(home_dir, ".ssh")
    
    if not os.path.exists(ssh_dir):
        print("⚠️ SSH directory not found in your home directory")
        return
    
    # Check for private keys
    private_keys = []
    for file in os.listdir(ssh_dir):
        if file.startswith("id_") and not file.endswith(".pub"):
            private_keys.append(file)
    
    if private_keys:
        print(f"Found {len(private_keys)} SSH private key(s):")
        for key in private_keys:
            # Check key permissions
            key_path = os.path.join(ssh_dir, key)
            key_perms = oct(os.stat(key_path).st_mode)[-3:]
            if key_perms == '600':
                print(f"✅ {key} has secure permissions (600)")
            else:
                print(f"❌ {key} has insecure permissions: {key_perms}, should be 600")
            
            # Check if key has a passphrase
            has_passphrase = run_command(f"ssh-keygen -y -P \"\" -f {key_path} >/dev/null 2>&1 || echo protected")
            if "protected" in has_passphrase:
                print(f"✅ {key} is protected with a passphrase")
            else:
                print(f"⚠️ {key} does not appear to have a passphrase")
    else:
        print("⚠️ No SSH private keys found")
    
    # Check authorized_keys file
    auth_keys_path = os.path.join(ssh_dir, "authorized_keys")
    if os.path.exists(auth_keys_path):
        num_keys = len(open(auth_keys_path).readlines())
        print(f"Found {num_keys} authorized key(s)")
        
        # Check auth_keys permissions
        auth_keys_perms = oct(os.stat(auth_keys_path).st_mode)[-3:]
        if auth_keys_perms in ['600', '644']:
            print(f"✅ authorized_keys has secure permissions ({auth_keys_perms})")
        else:
            print(f"⚠️ authorized_keys has unusual permissions: {auth_keys_perms}")
    else:
        print("⚠️ No authorized_keys file found")


def check_ssh_client_config():
    """Check SSH client configuration."""
    print_header("SSH CLIENT CONFIGURATION")
    
    home_dir = str(Path.home())
    ssh_config = os.path.join(home_dir, ".ssh", "config")
    
    if not os.path.exists(ssh_config):
        print("⚠️ SSH client config file not found")
        return
    
    # Read the SSH client config file
    with open(ssh_config, 'r') as f:
        config_data = f.read()
    
    # Check for custom hosts
    host_pattern = re.compile(r'^Host\s+(?![\*\?])', re.MULTILINE)
    hosts = host_pattern.findall(config_data)
    
    if hosts:
        print(f"✅ Found {len(hosts)} custom host configuration(s)")
    else:
        print("⚠️ No custom host configurations found")
    
    # Check for security settings
    if re.search(r'^\s*ForwardAgent\s+yes', config_data, re.MULTILINE):
        print("⚠️ ForwardAgent is enabled in client config (security risk)")
    
    if re.search(r'^\s*StrictHostKeyChecking\s+no', config_data, re.MULTILINE):
        print("❌ StrictHostKeyChecking is disabled (major security risk)")


def check_firewall_for_ssh():
    """Check firewall configuration for SSH."""
    print_header("FIREWALL CONFIGURATION FOR SSH")
    
    # Check if UFW is installed and enabled
    ufw_status = run_command("ufw status 2>/dev/null")
    if "inactive" in ufw_status:
        print("⚠️ UFW firewall is inactive")
    elif "active" in ufw_status:
        print("✅ UFW firewall is active")
        
        # Check for SSH rules
        if "22" in ufw_status or "ssh" in ufw_status:
            print("✅ Firewall has rules for SSH")
        else:
            print("⚠️ No explicit SSH rules found in firewall")
    else:
        # Check iptables for SSH rules
        iptables_rules = run_command("iptables -L INPUT -n | grep -E '(22|ssh)'")
        if iptables_rules:
            print("✅ iptables has rules for SSH")
        else:
            print("⚠️ No SSH rules found in iptables")


def check_ssh_login_attempts():
    """Check for failed SSH login attempts."""
    print_header("SSH LOGIN ATTEMPTS")
    
    # Check for failed login attempts in auth.log or secure
    if os.path.exists("/var/log/auth.log"):
        log_file = "/var/log/auth.log"
    elif os.path.exists("/var/log/secure"):
        log_file = "/var/log/secure"
    else:
        print("⚠️ Could not find SSH log files")
        return
    
    # Get failed login attempts from today
    today = datetime.datetime.now().strftime("%b %e")
    failed_attempts = run_command(f"grep 'sshd.*Failed password' {log_file} | grep '{today}'")
    
    if failed_attempts:
        count = len(failed_attempts.splitlines())
        print(f"⚠️ Found {count} failed SSH login attempts today")
        
        # Extract IP addresses of failed attempts
        ips = set()
        for line in failed_attempts.splitlines():
            match = re.search(r'from\s+(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ips.add(match.group(1))
        
        if ips:
            print(f"Failed attempts from {len(ips)} unique IP addresses:")
            for ip in list(ips)[:5]:  # Show up to 5 IPs
                print(f"  - {ip}")
            if len(ips) > 5:
                print(f"  - ... and {len(ips) - 5} more")
    else:
        print("✅ No failed SSH login attempts found today")


def check_ssh_keys_security():
    """Check SSH keys security settings."""
    print_header("SSH KEYS SECURITY ANALYSIS")
    
    # Find all SSH keys
    home_dir = str(Path.home())
    ssh_dir = os.path.join(home_dir, ".ssh")
    
    if not os.path.exists(ssh_dir):
        print("⚠️ SSH directory not found")
        return
    
    # Check SSH directory permissions
    ssh_dir_perms = oct(os.stat(ssh_dir).st_mode)[-3:]
    if ssh_dir_perms == '700':
        print(f"✅ SSH directory has secure permissions (700)")
    else:
        print(f"❌ SSH directory has insecure permissions: {ssh_dir_perms}, should be 700")
    
    # Find public keys and check their type and size
    for file in os.listdir(ssh_dir):
        if file.endswith(".pub"):
            key_path = os.path.join(ssh_dir, file)
            key_info = run_command(f"ssh-keygen -l -f {key_path}")
            
            if key_info and "bit" in key_info:
                # Extract key size and type
                size_match = re.search(r'(\d+) \w+ key', key_info)
                type_match = re.search(r'(rsa|dsa|ecdsa|ed25519)', key_info.lower())
                
                if size_match and type_match:
                    size = size_match.group(1)
                    key_type = type_match.group(1)
                    
                    if key_type == 'rsa' and int(size) < 3072:
                        print(f"⚠️ {file}: RSA key with size {size} bits (recommended: ≥3072 bits)")
                    elif key_type == 'dsa':
                        print(f"❌ {file}: Using DSA key type (insecure, should be replaced)")
                    elif key_type == 'ecdsa' and int(size) < 256:
                        print(f"⚠️ {file}: ECDSA key with size {size} bits (recommended: ≥256 bits)")
                    elif key_type == 'ed25519':
                        print(f"✅ {file}: Using ED25519 key type (good security)")
                    else:
                        print(f"✅ {file}: {key_type.upper()} key with good size ({size} bits)")


def provide_recommendations():
    """Provide general recommendations for SSH hardening."""
    print_header("SSH HARDENING RECOMMENDATIONS")
    
    recommendations = [
        "1. Use key-based authentication and disable password authentication",
        "2. Use strong keys: RSA (4096 bits) or ED25519",
        "3. Always protect your private keys with a strong passphrase",
        "4. Consider changing the default SSH port to reduce automated attacks",
        "5. Implement rate limiting with fail2ban to prevent brute force attacks",
        "6. Regularly audit authorized_keys files and remove unused entries",
        "7. Configure idle timeout to automatically disconnect inactive sessions",
        "8. Limit user access with AllowUsers or AllowGroups",
        "9. Disable root login and use sudo for administrative tasks",
        "10. Keep your SSH software updated to patch security vulnerabilities"
    ]
    
    for rec in recommendations:
        print(rec)


def main():
    """Run all SSH security checks."""
    print_header("SSH SECURITY AUDIT REPORT")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"User: {pwd.getpwuid(os.getuid()).pw_name}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"SSH Version: {get_ssh_version()}")
    
    is_root = check_if_root()
    
    if check_ssh_status():
        check_ssh_config()
        check_key_based_auth()
        check_ssh_client_config()
        check_firewall_for_ssh()
        check_ssh_keys_security()
        
        if is_root:
            check_ssh_login_attempts()
        else:
            print("\n⚠️ Skipping SSH login attempts check (requires root)")
    
    provide_recommendations()
    
    print_header("AUDIT COMPLETE")
    print("This is a basic SSH security audit for educational purposes only.")
    print("For a comprehensive security assessment, consider professional security tools.")


if __name__ == "__main__":
    main() 