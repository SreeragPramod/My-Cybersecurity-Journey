"""
Day 08 - Network Reconnaissance: Port Scanner Simulator
Maps discovered open ports to known services and flags ones that pose
elevated security risk if exposed to the internet.
Security use case: This is the exact judgment a Cloud Security Engineer
applies when reviewing AWS Security Group rules or GCP Firewall rules -
not just "what's open" but "what's open that shouldn't be."
"""

# port -> (service name, risk level, reason)
PORT_INTEL = {
    21:   ("FTP (File Transfer)",        "HIGH",   "Transmits credentials in plaintext"),
    22:   ("SSH (Secure Shell Login)",   "MEDIUM", "Safe if key-based auth + restricted source IPs"),
    23:   ("Telnet",                     "HIGH",   "Unencrypted remote access - should never be exposed"),
    80:   ("HTTP (Unencrypted Web)",     "LOW",    "Fine if redirecting to HTTPS, risky if serving sensitive data"),
    443:  ("HTTPS (Secure Web)",         "LOW",    "Standard secure web traffic"),
    3306: ("MySQL Database",             "HIGH",   "Databases should never be directly internet-facing"),
    3389: ("RDP (Remote Desktop)",       "HIGH",   "Frequent target of brute-force and ransomware attacks"),
}

RISK_ORDER = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}


def assess_ports(open_ports):
    findings = []
    for port in open_ports:
        if port in PORT_INTEL:
            service, risk, reason = PORT_INTEL[port]
        else:
            service, risk, reason = "Unknown service", "UNKNOWN", "Unrecognized port - investigate manually"
        findings.append({"port": port, "service": service, "risk": risk, "reason": reason})
    return findings


def print_report(target_ip, findings):
    print(f"Scanning target: {target_ip}\n")
    for f in sorted(findings, key=lambda x: RISK_ORDER.get(x["risk"], 0), reverse=True):
        print(f"[{f['risk']:>7}] Port {f['port']} -> {f['service']}")
        print(f"          Reason: {f['reason']}\n")

    high_risk = [f for f in findings if f["risk"] == "HIGH"]
    if high_risk:
        print("--- Recommendations ---")
        for f in high_risk:
            print(f"- Close port {f['port']} ({f['service']}) or restrict to a specific IP range / VPN only.")


if __name__ == "__main__":
    target_ip = "192.168.1.100"
    found_ports = [22, 80, 3389]

    findings = assess_ports(found_ports)
    print_report(target_ip, findings)
