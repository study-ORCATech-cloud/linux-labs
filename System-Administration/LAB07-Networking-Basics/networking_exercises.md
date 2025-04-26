# LAB07 - Networking Basics Exercises

These exercises will help you practice essential networking concepts and tools in Linux. Complete each task to build fundamental networking skills for system administration.

## Exercise 1: Network Configuration

### TODO:
1. Display all network interfaces on your system.

2. Identify your primary network interface (usually starts with 'eth', 'en', or 'wl').

3. Determine your IP address, network mask, and broadcast address.

4. View your default gateway.

5. Check your hostname.

6. Display your fully qualified domain name (FQDN).

## Exercise 2: Network Connectivity Testing

### TODO:
1. Test connectivity to Google's DNS server (8.8.8.8).

2. Send exactly 5 packets to a website of your choice.

3. Ping a hostname (like google.com) and note the resolved IP address.

4. Test connectivity to a port using telnet or a similar tool.

5. Use netcat (nc) to test port connectivity.

6. Determine if a service is reachable and measure latency.

## Exercise 3: DNS Resolution

### TODO:
1. Find the IP address of a popular website using nslookup.

2. Query detailed DNS information for a domain using dig.

3. Look up the mail server (MX records) for a domain.

4. Find the name servers (NS records) for a domain.

5. Examine your system's DNS resolver configuration.

6. Perform a reverse DNS lookup on an IP address.

## Exercise 4: Network Diagnostics

### TODO:
1. Display the path packets take to reach a website.

2. Observe the number of hops and latency at each hop.

3. Use mtr (My TraceRoute) for continuous path monitoring.

4. Check for packet errors or drops on interfaces.

5. View interface statistics.

6. Try a different protocol with traceroute (e.g., ICMP).

## Exercise 5: Working with Web Content

### TODO:
1. Fetch the HTML content of a website.

2. Save the output of a web request to a file.

3. View only HTTP headers from a website.

4. Download a file using a command-line tool.

5. Test an API endpoint.

6. View the complete HTTP transaction details of a web request.

## Exercise 6: Network Services and Ports

### TODO:
1. List all listening ports on your system.

2. Use an alternative tool to list listening ports.

3. Check which process is using a specific port.

4. List all established network connections.

5. Monitor real-time connections.

6. Check if common services are running by examining their default ports.

## Exercise 7: Network Configuration Files

### TODO:
1. Examine the network interface configuration files.

2. Look at your DNS resolver configuration.

3. Check your hosts file.

4. View your hostname configuration.

5. Examine any firewall rules.

6. Check if NetworkManager is managing your connections and its current status.

## Bonus Challenge:
Create a shell script called `network_info.sh` that:
1. Shows your primary IP address and interface
2. Lists all interfaces and their status
3. Shows your default gateway
4. Displays your DNS servers
5. Checks connectivity to 8.8.8.8 and google.com
6. Shows the route to google.com (first 5 hops)
7. Lists all listening ports 