# Networking Cheatsheet

## Network Configuration Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ip addr` | Show network interfaces and addresses | `ip addr` |
| `ip link` | Show network interface status | `ip link show eth0` |
| `ip -s link` | Show interface statistics | `ip -s link show eth0` |
| `ip route` | Show routing table | `ip route` |
| `ip neigh` | Show ARP/neighbor table | `ip neigh` |
| `ifconfig` | Show/configure interfaces (older) | `ifconfig eth0` |
| `route` | Show/manipulate routing table (older) | `route -n` |
| `hostname` | Show or set system hostname | `hostname -f` |
| `dhclient` | DHCP client to obtain IP | `sudo dhclient eth0` |
| `nmcli` | NetworkManager command-line tool | `nmcli device status` |
| `nmtui` | NetworkManager text UI | `nmtui` |

## Network Testing & Diagnostics

| Command | Description | Example |
|---------|-------------|---------|
| `ping` | Test connectivity to host | `ping -c 4 google.com` |
| `ping6` | Test IPv6 connectivity | `ping6 -c 4 ipv6.google.com` |
| `traceroute` | Show route to destination | `traceroute google.com` |
| `tracepath` | Trace path to destination (no root needed) | `tracepath google.com` |
| `mtr` | Continuously traceroute a host | `mtr google.com` |
| `netstat` | Network statistics | `netstat -tuln` |
| `ss` | Socket statistics (newer netstat) | `ss -tuln` |
| `nmap` | Network port scanner | `nmap -sT 192.168.1.1` |
| `tcpdump` | Capture packet data | `sudo tcpdump -i eth0 port 80` |
| `ethtool` | Query/control network driver/hardware | `sudo ethtool eth0` |
| `iperf3` | Network bandwidth testing | `iperf3 -c iperf.server.com` |

## DNS Tools

| Command | Description | Example |
|---------|-------------|---------|
| `nslookup` | Query DNS records | `nslookup google.com` |
| `dig` | DNS lookup utility | `dig google.com` |
| `dig +short` | Simple DNS lookup | `dig +short google.com` |
| `host` | DNS lookup | `host google.com` |
| `getent hosts` | Query hosts database | `getent hosts google.com` |
| `whois` | Query WHOIS databases | `whois google.com` |
| `resolvectl` | Query systemd-resolved service | `resolvectl status` |

## Web & HTTP Tools

| Command | Description | Example |
|---------|-------------|---------|
| `curl` | Transfer data from/to server | `curl https://example.com` |
| `curl -I` | Get HTTP headers only | `curl -I https://example.com` |
| `curl -v` | Verbose output (debug) | `curl -v https://example.com` |
| `wget` | Download files from web | `wget https://example.com/file` |
| `lynx` | Text-based web browser | `lynx example.com` |
| `ab` | Apache HTTP benchmarking tool | `ab -n 100 https://example.com/` |

## Network Ports & Services

| Command | Description | Example |
|---------|-------------|---------|
| `netstat -tuln` | Show listening TCP/UDP ports | `netstat -tuln` |
| `netstat -anp` | Show all connections with PID/program | `sudo netstat -anp` |
| `ss -tuln` | Show listening sockets (modern) | `ss -tuln` |
| `lsof -i` | List processes with open ports | `sudo lsof -i :22` |
| `fuser` | Show processes using file/socket | `sudo fuser 80/tcp` |
| `nc` | Netcat for connections/scanning | `nc -zv example.com 80` |
| `telnet` | Connect to a service | `telnet example.com 80` |

## Connection Management

| Command | Description | Example |
|---------|-------------|---------|
| `ssh` | Secure shell connection | `ssh user@host` |
| `scp` | Secure copy over SSH | `scp file.txt user@host:path/` |
| `rsync` | Fast file transfer/sync | `rsync -avz dir/ user@host:dir/` |
| `sftp` | Secure FTP over SSH | `sftp user@host` |
| `iptables` | Configure IP firewall | `sudo iptables -L` |
| `ufw` | Uncomplicated Firewall | `sudo ufw status` |

## Network Configuration Files

| File | Description | Example Use |
|------|-------------|-------------|
| `/etc/hosts` | Static hostname mappings | `echo "192.168.1.10 server" >> /etc/hosts` |
| `/etc/resolv.conf` | DNS resolver configuration | `cat /etc/resolv.conf` |
| `/etc/hostname` | System hostname | `echo "myserver" > /etc/hostname` |
| `/etc/nsswitch.conf` | Name service switch config | `cat /etc/nsswitch.conf` |
| `/etc/network/interfaces` | Interface config (Debian) | `cat /etc/network/interfaces` |
| `/etc/sysconfig/network-scripts/` | Interface config (RHEL) | `ls /etc/sysconfig/network-scripts/` |
| `/etc/netplan/` | Netplan config (Ubuntu) | `cat /etc/netplan/*.yaml` |

## Network Service Management

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl status networking` | Check network service | `systemctl status networking` |
| `systemctl restart networking` | Restart networking | `sudo systemctl restart networking` |
| `systemctl status NetworkManager` | Check NetworkManager | `systemctl status NetworkManager` |
| `service network restart` | Restart network (old style) | `sudo service network restart` |
| `systemd-resolve --status` | systemd-resolved status | `systemd-resolve --status` |

## Wireless Networking

| Command | Description | Example |
|---------|-------------|---------|
| `iwconfig` | Configure wireless interfaces | `iwconfig wlan0` |
| `iwlist` | List wireless network parameters | `iwlist wlan0 scan` |
| `nmcli radio wifi` | Check WiFi status | `nmcli radio wifi` |
| `nmcli device wifi list` | List available WiFi networks | `nmcli device wifi list` |
| `nmcli device wifi connect` | Connect to WiFi | `nmcli device wifi connect SSID password PASSWORD` |

## Advanced Network Examples

```bash
# Set a static IP temporarily
sudo ip addr add 192.168.1.100/24 dev eth0

# Set a default gateway temporarily
sudo ip route add default via 192.168.1.1

# Add a static route
sudo ip route add 10.0.0.0/24 via 192.168.1.254

# Show routing table for a specific destination
ip route get 8.8.8.8

# Clear ARP cache
sudo ip neigh flush all

# Show listening TCP ports in numeric format
ss -tln

# Monitor all HTTP traffic on an interface
sudo tcpdump -i eth0 port 80 -A

# List all established SSH connections
ss -o state established '( dport = :ssh or sport = :ssh )'

# Check DNS resolution time
time dig google.com

# Diagnose network connectivity with mtr
mtr --report --report-cycles=10 google.com

# Download a webpage and show its HTTP status code
curl -s -o /dev/null -w "%{http_code}\n" https://example.com

# Port scan a host
sudo nmap -sS -p 1-1000 192.168.1.1

# Test if a port is accessible
timeout 1 bash -c "</dev/tcp/google.com/80" && echo "Port is open" || echo "Port is closed"
``` 