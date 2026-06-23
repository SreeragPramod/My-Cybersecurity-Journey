print("--- Firewall Traffic Simulator ---")

# A Python 'List' of known malicious IP addresses (The Blacklist)
blocked_ips = ["192.168.1.50", "10.0.0.99", "172.16.0.5", "8.8.8.8"]
print("Firewall is active. Monitoring incoming connections...\n")
# A batch of incoming traffic trying to connect to our server right now
incoming_traffic = ["192.168.1.15", "10.0.0.99", "192.168.1.20", "8.8.8.8", "10.0.0.5"]
# A 'for loop' goes through the incoming_traffic list one-by-one
for ip in incoming_traffic:
    print("Checking IP:", ip)
# We check if the IP is inside our blacklist
    if ip in blocked_ips:
        print("  -> [!!!!!] THREAT DETECTED! Connection Dropped.\n")
    else:
        print("  ->  Safe traffic. Connection Allowed.\n")

print("Traffic scan completeddd.")
