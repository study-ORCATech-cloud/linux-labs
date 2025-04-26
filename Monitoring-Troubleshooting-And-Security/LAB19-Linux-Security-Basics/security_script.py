#!/usr/bin/env python3
"""
Linux Security Basics - Simple Security Auditing Script

This script performs basic security checks on a Linux system and generates
a report of potential security issues. This is for educational purposes only
and should not be considered a comprehensive security tool.

Usage:
    python3 security_script.py

Requirements:
    - Python 3.6+
    - Root privileges for some checks (run with sudo)
"""

import os
import subprocess
import sys
import platform
import datetime
import pwd
import grp
import stat


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


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
        print("Warning: Some checks require root privileges. Run with sudo for complete results.")
        return False
    return True


def system_info():
    """Collect and print system information."""
    print_header("SYSTEM INFORMATION")
    
    # Basic system info
    print(f"Hostname: {platform.node()}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Distribution: {run_command('lsb_release -d 2>/dev/null || cat /etc/os-release | grep PRETTY_NAME')}")
    print(f"Kernel: {platform.uname().release}")
    print(f"Architecture: {platform.machine()}")
    
    # Current time
    print(f"Current Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Last boot time
    uptime = run_command("uptime -s")
    print(f"System Boot Time: {uptime}")


def check_users():
    """Check user accounts for security issues."""
    print_header("USER ACCOUNT SECURITY")
    
    # List users with UID 0 (root privileges)
    root_users = []
    for user in pwd.getpwall():
        if user.pw_uid == 0:
            root_users.append(user.pw_name)
    
    if len(root_users) > 1:
        print("⚠️  WARNING: Multiple users with UID 0 (root privileges):")
        for user in root_users:
            print(f"  - {user}")
    else:
        print("✅ Only one user (root) has UID 0")
    
    # Check for users without passwords
    # TODO: Implement the check for users without passwords
    # This requires root access to read /etc/shadow
    
    # Check for users with login shells that shouldn't have them
    system_users = []
    for user in pwd.getpwall():
        if 1 <= user.pw_uid < 1000 and user.pw_shell not in ['/usr/sbin/nologin', '/bin/false', '/sbin/nologin']:
            system_users.append(f"{user.pw_name} (Shell: {user.pw_shell})")
    
    if system_users:
        print("⚠️  System users with login shells:")
        for user in system_users:
            print(f"  - {user}")
    else:
        print("✅ No system users with login shells")


def check_ssh_config():
    """Check SSH configuration for security issues."""
    print_header("SSH CONFIGURATION")
    
    if not os.path.exists('/etc/ssh/sshd_config'):
        print("SSH server is not installed")
        return
    
    # Check important SSH settings
    settings_to_check = {
        'PermitRootLogin': {'recommended': 'no', 'critical': True},
        'PasswordAuthentication': {'recommended': 'no', 'critical': False},
        'Protocol': {'recommended': '2', 'critical': True},
        'PermitEmptyPasswords': {'recommended': 'no', 'critical': True},
        'MaxAuthTries': {'recommended': '3', 'critical': False},
        'ClientAliveInterval': {'recommended': '300', 'critical': False}
    }
    
    sshd_config = run_command("cat /etc/ssh/sshd_config")
    
    for setting, details in settings_to_check.items():
        found = False
        for line in sshd_config.splitlines():
            if line.strip().startswith(setting) and not line.strip().startswith('#'):
                found = True
                value = line.strip().split()[1]
                if value == details['recommended']:
                    print(f"✅ {setting} is set to recommended value: {value}")
                else:
                    symbol = "❌" if details['critical'] else "⚠️"
                    print(f"{symbol} {setting} is set to {value}, recommended: {details['recommended']}")
        
        if not found:
            print(f"⚠️ {setting} is not explicitly set in sshd_config")


def check_service_status():
    """Check status of important services."""
    print_header("SERVICE STATUS")
    
    # Services that should be checked (add or remove based on your requirements)
    services = [
        {'name': 'ssh', 'expected': 'active', 'critical': False},
        {'name': 'ufw', 'expected': 'active', 'critical': True},
        {'name': 'apparmor', 'expected': 'active', 'critical': False},
        {'name': 'cups', 'expected': 'inactive', 'critical': False}
    ]
    
    for service in services:
        status = run_command(f"systemctl is-active {service['name']} 2>/dev/null || echo inactive")
        if status == service['expected']:
            print(f"✅ {service['name']} is {status} (expected)")
        else:
            symbol = "❌" if service['critical'] else "⚠️"
            print(f"{symbol} {service['name']} is {status}, expected: {service['expected']}")


def check_firewall():
    """Check firewall status and configuration."""
    print_header("FIREWALL STATUS")
    
    # Check UFW status
    ufw_status = run_command("ufw status 2>/dev/null")
    if 'inactive' in ufw_status:
        print("❌ UFW firewall is inactive")
    elif 'active' in ufw_status:
        print("✅ UFW firewall is active")
        
        # Get UFW rules
        print("\nFirewall Rules:")
        print(run_command("ufw status numbered | grep -v Status | grep -v -- '--'"))
    else:
        # Check if iptables has rules
        iptables_rules = run_command("iptables -L | grep -v Chain | grep -v target | grep -v ^$")
        if iptables_rules:
            print("✅ iptables has rules configured")
        else:
            print("❌ No firewall appears to be configured")


def check_file_permissions():
    """Check permissions on important files."""
    print_header("FILE PERMISSIONS")
    
    critical_files = [
        {'path': '/etc/passwd', 'expected_mode': 0o644, 'expected_owner': 'root', 'expected_group': 'root'},
        {'path': '/etc/shadow', 'expected_mode': 0o640, 'expected_owner': 'root', 'expected_group': 'shadow'},
        {'path': '/etc/ssh/sshd_config', 'expected_mode': 0o600, 'expected_owner': 'root', 'expected_group': 'root'}
    ]
    
    for file_info in critical_files:
        path = file_info['path']
        if not os.path.exists(path):
            print(f"⚠️ File {path} does not exist")
            continue
        
        try:
            stat_info = os.stat(path)
            mode = stat.S_IMODE(stat_info.st_mode)
            owner = pwd.getpwuid(stat_info.st_uid).pw_name
            group = grp.getgrgid(stat_info.st_gid).gr_name
            
            issues = []
            if mode != file_info['expected_mode']:
                actual_mode_str = oct(mode)[2:]
                expected_mode_str = oct(file_info['expected_mode'])[2:]
                issues.append(f"mode {actual_mode_str} (expected {expected_mode_str})")
            if owner != file_info['expected_owner']:
                issues.append(f"owner {owner} (expected {file_info['expected_owner']})")
            if group != file_info['expected_group']:
                issues.append(f"group {group} (expected {file_info['expected_group']})")
            
            if issues:
                print(f"❌ {path} has incorrect: {', '.join(issues)}")
            else:
                print(f"✅ {path} has correct permissions")
        except Exception as e:
            print(f"⚠️ Error checking {path}: {e}")


def main():
    """Main function to run all checks."""
    print_header("LINUX SECURITY AUDIT REPORT")
    print(f"Run Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    is_root = check_if_root()
    
    # Run all checks
    system_info()
    check_users()
    check_ssh_config()
    check_service_status()
    check_firewall()
    
    if is_root:
        check_file_permissions()
    else:
        print_header("FILE PERMISSIONS")
        print("Skipped file permission checks - requires root privileges")
    
    print_header("AUDIT COMPLETE")
    print("This is a basic security audit for educational purposes only.")
    print("For a comprehensive security assessment, consider professional security tools.")
    
    # TODO: Add more security checks as needed
    # - Listening network ports
    # - SUID/SGID files
    # - Process analysis
    # - Network configuration


if __name__ == "__main__":
    main() 