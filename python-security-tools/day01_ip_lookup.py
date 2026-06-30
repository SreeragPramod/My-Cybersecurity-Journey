"""
Day 01 - IP Lookup Tool
Resolves a domain name to its IP address using DNS.
Security use case: Reconnaissance - mapping domains to infrastructure
before further investigation.
"""
import socket

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] {domain} -> {ip}")
        return ip
    except socket.gaierror as e:
        print(f"[-] Could not resolve {domain}: {e}")
        return None

if __name__ == "__main__":
    targets = ["google.com", "github.com", "cloudflare.com"]
    for domain in targets:
        get_ip(domain)
