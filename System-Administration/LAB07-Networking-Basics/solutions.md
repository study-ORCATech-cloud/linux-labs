# LAB07 - Networking Basics Solutions

Below are the solutions to the networking basics exercises. Remember to try solving them on your own first!

## Exercise 1: Network Configuration

### Solution:
1. Display all network interfaces:
   ```bash
   ip addr
   ```

2. Identify primary network interface:
   ```bash
   # Look for the interface with an assigned IP address
   # It will usually be named eth0, enp0s3, ens33, or wlan0 depending on your system
   ip addr | grep -A2 "state UP"
   ```

3. Determine IP address, network mask, and broadcast address:
   ```bash
   # From the ip addr output, look for lines like:
   # inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
   # The /24 represents the subnet mask (255.255.255.0)
   ip addr show dev eth0  # Replace eth0 with your interface name
   ```

4. View default gateway:
   ```bash
   ip route | grep default
   ```

5. Check hostname:
   ```bash
   hostname
   ```

6. Display fully qualified domain name:
   ```bash
   hostname -f
   # If this doesn't show the FQDN, your system might not have one configured
   ```

## Exercise 2: Network Connectivity Testing

### Solution:
1. Test connectivity to Google DNS:
   ```bash
   ping 8.8.8.8
   # Press Ctrl+C to stop
   ```

2. Ping with exact packet count:
   ```bash
   ping -c 5 example.com
   ```

3. Ping hostname and note IP:
   ```bash
   ping -c 2 google.com
   # Note the IP address in the output:
   # PING google.com (142.250.x.x) 56(84) bytes of data.
   ```

4. Test port connectivity with telnet:
   ```bash
   # Install telnet if needed
   sudo apt install telnetd-ssl  # Debian/Ubuntu
   # or
   sudo yum install telnet  # RHEL/CentOS

   telnet google.com 80
   # If successful, you'll get a connection
   # Type Ctrl+] then 'quit' to exit
   ```

5. Test port connectivity with netcat:
   ```bash
   # Install netcat if needed
   sudo apt install netcat  # Debian/Ubuntu
   # or
   sudo yum install nc  # RHEL/CentOS

   nc -zv google.com 80
   ```

6. Measure latency:
   ```bash
   ping -c 10 google.com
   # Check the statistics at the end for min/avg/max times
   ```

## Exercise 3: DNS Resolution

### Solution:
1. Find IP address with nslookup:
   ```bash
   nslookup example.com
   ```

2. Query DNS with dig:
   ```bash
   # Install dig if needed
   sudo apt install dnsutils  # Debian/Ubuntu
   # or
   sudo yum install bind-utils  # RHEL/CentOS

   dig example.com
   ```

3. Look up mail servers:
   ```bash
   dig MX gmail.com
   ```

4. Find name servers:
   ```bash
   dig NS example.com
   ```

5. Examine DNS resolver configuration:
   ```bash
   cat /etc/resolv.conf
   ```

6. Perform reverse DNS lookup:
   ```bash
   host 8.8.8.8
   # or
   dig -x 8.8.8.8
   ```

## Exercise 4: Network Diagnostics

### Solution:
1. Display path to website:
   ```bash
   # Install traceroute if needed
   sudo apt install traceroute  # Debian/Ubuntu
   # or
   sudo yum install traceroute  # RHEL/CentOS

   traceroute google.com
   ```

2. Observe hop counts and latency:
   ```bash
   # From the traceroute output, each line represents a hop with latency values
   traceroute -n google.com  # -n shows IP addresses instead of hostnames
   ```

3. Use mtr for continuous path monitoring:
   ```bash
   # Install mtr if needed
   sudo apt install mtr-tiny  # Debian/Ubuntu
   # or
   sudo yum install mtr  # RHEL/CentOS

   mtr google.com
   # Press 'q' to quit
   ```

4. Check for packet errors:
   ```bash
   # Using ip command
   ip -s link show dev eth0  # Replace eth0 with your interface name

   # Using ifconfig if available
   ifconfig eth0 | grep -E "errors|dropped"
   ```

5. View interface statistics:
   ```bash
   netstat -i
   ```

6. Try ICMP traceroute:
   ```bash
   traceroute -I google.com
   ```

## Exercise 5: Working with Web Content

### Solution:
1. Fetch website HTML:
   ```bash
   curl https://example.com
   ```

2. Save curl output to file:
   ```bash
   curl -o example.html https://example.com
   ```

3. View HTTP headers only:
   ```bash
   curl -I https://example.com
   ```

4. Download file with wget:
   ```bash
   # Install wget if needed
   sudo apt install wget  # Debian/Ubuntu
   # or
   sudo yum install wget  # RHEL/CentOS

   wget https://example.com/index.html
   ```

5. Test an API endpoint:
   ```bash
   curl https://jsonplaceholder.typicode.com/posts/1
   ```

6. Use verbose curl:
   ```bash
   curl -v https://example.com
   ```

## Exercise 6: Network Services and Ports

### Solution:
1. List listening ports:
   ```bash
   # Install net-tools if needed
   sudo apt install net-tools  # Debian/Ubuntu
   # or
   sudo yum install net-tools  # RHEL/CentOS

   netstat -tuln
   ```

2. Use ss to list ports:
   ```bash
   ss -tuln
   ```

3. Check which process uses a port:
   ```bash
   # Install lsof if needed
   sudo apt install lsof  # Debian/Ubuntu
   # or
   sudo yum install lsof  # RHEL/CentOS

   sudo lsof -i :22  # Check what's using port 22 (usually SSH)
   ```

4. List established connections:
   ```bash
   netstat -tuna
   ```

5. Monitor real-time connections:
   ```bash
   watch ss -tuna
   ```

6. Check common services:
   ```bash
   # Check SSH (port 22)
   sudo lsof -i :22
   # Check HTTP (port 80)
   sudo lsof -i :80
   # Check HTTPS (port 443)
   sudo lsof -i :443
   ```

## Exercise 7: Network Configuration Files

### Solution:
1. Examine network interface configuration:
   ```bash
   # On Debian/Ubuntu
   ls -la /etc/network/
   cat /etc/network/interfaces

   # On RHEL/CentOS
   ls -la /etc/sysconfig/network-scripts/
   cat /etc/sysconfig/network-scripts/ifcfg-eth0  # Replace eth0 with your interface
   ```

2. Check DNS resolver configuration:
   ```bash
   cat /etc/resolv.conf
   ```

3. View hosts file:
   ```bash
   cat /etc/hosts
   ```

4. Check hostname configuration:
   ```bash
   cat /etc/hostname
   ```

5. Examine firewall rules:
   ```bash
   sudo iptables -L
   ```

6. Check NetworkManager status:
   ```bash
   systemctl status NetworkManager
   # or
   nmcli general status
   ```

## Bonus Challenge Solution:

```bash
#!/bin/bash

# network_info.sh - A script to display network information
# Usage: ./network_info.sh

echo "============================================"
echo "          NETWORK INFORMATION               "
echo "============================================"
echo

# 1. Primary IP and interface
echo "PRIMARY INTERFACE AND IP ADDRESS:"
primary_interface=$(ip route | grep default | awk '{print $5}')
primary_ip=$(ip -4 addr show dev "$primary_interface" | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
echo "Interface: $primary_interface"
echo "IP Address: $primary_ip"
echo

# 2. All interfaces and status
echo "ALL INTERFACES:"
ip -brief link show
echo

# 3. Default gateway
echo "DEFAULT GATEWAY:"
ip route | grep default
echo

# 4. DNS servers
echo "DNS SERVERS:"
grep "nameserver" /etc/resolv.conf
echo

# 5. Check connectivity
echo "CONNECTIVITY TESTS:"
echo "Pinging 8.8.8.8:"
ping -c 2 8.8.8.8
echo
echo "Pinging google.com:"
ping -c 2 google.com
echo

# 6. Route to google.com (first 5 hops)
echo "ROUTE TO GOOGLE.COM (FIRST 5 HOPS):"
traceroute -m 5 google.com
echo

# 7. Listening ports
echo "LISTENING PORTS:"
ss -tuln
echo

echo "============================================"
```

To use the script:
```bash
chmod +x network_info.sh
./network_info.sh
``` 