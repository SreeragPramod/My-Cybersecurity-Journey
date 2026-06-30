"""
Day 06 - Server Log Analyzer (Brute Force Detection)
Parses server logs to detect brute-force login attempts by tracking
failed login counts per IP address - without assuming in advance
which IP is suspicious.
Security use case: This is the core logic behind SIEM alerting rules
and cloud-native tools like AWS GuardDuty / CloudTrail anomaly
detection - flagging IPs that exceed a failed-attempt threshold.
"""
from collections import defaultdict


FAILED_ATTEMPT_THRESHOLD = 3

server_log = [
    "192.168.1.10 - LOGIN SUCCESS",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED",
    "192.168.1.12 - LOGIN SUCCESS",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED",
]


def parse_log(log_entries):
    """Parses raw log lines into (ip, status) tuples."""
    parsed = []
    for entry in log_entries:
        ip, status = entry.split(" - ")
        parsed.append((ip.strip(), status.strip()))
    return parsed


def detect_brute_force(log_entries, threshold=FAILED_ATTEMPT_THRESHOLD):
    """
    Counts failed login attempts per IP and flags any IP that meets
    or exceeds the threshold, regardless of which IP it is.
    """
    failed_counts = defaultdict(int)

    for ip, status in parse_log(log_entries):
        if status == "LOGIN FAILED":
            failed_counts[ip] += 1

    flagged = {ip: count for ip, count in failed_counts.items() if count >= threshold}
    return failed_counts, flagged


def print_report(failed_counts, flagged):
    print("Summary Report:")
    for ip, count in failed_counts.items():
        print(f"  {ip}: {count} failed login attempt(s)")

    if flagged:
        print("\n[!] CRITICAL ALERTS:")
        for ip, count in flagged.items():
            print(f"[!] {ip} - {count} failed attempts (threshold: {FAILED_ATTEMPT_THRESHOLD})")
            print(f"[!] ACTION: IP {ip} flagged for automatic blocking.")
    else:
        print("\nNo brute-force patterns detected.")


if __name__ == "__main__":
    print("Scanning logs for brute force attacks...\n")
    failed_counts, flagged = detect_brute_force(server_log)
    print_report(failed_counts, flagged)
