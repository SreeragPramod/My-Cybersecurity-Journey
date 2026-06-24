print("--- Server Log Analyzer (Incident Response) ---")

# This is a simulated server log (in reality, this would be a massive text file)
server_log = [
    "192.168.1.10 - LOGIN SUCCESS",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED",
    "192.168.1.12 - LOGIN SUCCESS",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED",
    "10.0.0.5 - LOGIN FAILED"
]

print("Scanning logs for Brute Force attacks...\n")

# We start our counter at zero
failed_attempts = 0
suspicious_ip = "10.0.0.5"

# A 'for loop' to check every single line in the log
for log_entry in server_log:
    # We check if both the hacker's IP AND the word "FAILED" are in the sentence
    if suspicious_ip in log_entry and "FAILED" in log_entry:
        failed_attempts = failed_attempts + 1

print("Summary Report:")
print("IP", suspicious_ip, "failed to login", failed_attempts, "times.")

# If they fail too many times, we trigger an alarm!
if failed_attempts >= 3:
    print("\n[!] CRITICAL ALERT: Brute Force attack detected!")
    print("[!] ACTION: IP Address blocked automatically.")
