"""
Day 05 - Firewall Traffic Simulator
Simulates a basic firewall checking incoming connections against a
blocklist of known malicious IP addresses.
Security use case: This is the same core logic behind security groups,
network ACLs, and WAF rules in cloud environments (e.g. AWS Security
Groups, GCP Firewall Rules) - allow/deny decisions based on IP.
"""
from datetime import datetime


BLOCKED_IPS = {
    "192.168.1.50": "Known botnet C2 server",
    "10.0.0.99": "Repeated brute-force attempts",
    "172.16.0.5": "Flagged by threat intelligence feed",
    "8.8.8.8": "Policy violation - unauthorized DNS exfil attempt",
}


def check_traffic(incoming_ips):
    log = []
    for ip in incoming_ips:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if ip in BLOCKED_IPS:
            reason = BLOCKED_IPS[ip]
            status = "BLOCKED"
            print(f"[{timestamp}] {ip} -> THREAT DETECTED ({reason}). Connection dropped.")
        else:
            status = "ALLOWED"
            print(f"[{timestamp}] {ip} -> Safe traffic. Connection allowed.")
        log.append({"ip": ip, "status": status, "timestamp": timestamp})
    return log


def print_summary(log):
    blocked = sum(1 for entry in log if entry["status"] == "BLOCKED")
    allowed = len(log) - blocked
    print("\n--- Scan Summary ---")
    print(f"Total connections checked: {len(log)}")
    print(f"Allowed: {allowed}")
    print(f"Blocked: {blocked}")
    if blocked:
        print(f"Block rate: {blocked / len(log):.1%}")


if __name__ == "__main__":
    incoming_traffic = ["192.168.1.15", "10.0.0.99", "192.168.1.20", "8.8.8.8", "10.0.0.5"]
    print("Firewall active. Monitoring incoming connections...\n")
    traffic_log = check_traffic(incoming_traffic)
    print_summary(traffic_log)
