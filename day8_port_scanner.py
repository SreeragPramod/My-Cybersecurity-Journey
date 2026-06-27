print("--- Network Reconnaissance: Port Scanner Simulator ---")

# This is a Python 'Dictionary'. It uses Key:Value pairs.
# We are creating a cheat sheet that maps a port number to its service name.
port_cheat_sheet = {
    21: "FTP (File Transfer)",
    22: "SSH (Secure Shell Login)",
    80: "HTTP (Unencrypted Web)",
    443: "HTTPS (Secure Web)",
    3389: "RDP (Remote Desktop)"
}

print("Scanning target IP: 192.168.1.100...\n")

# This is a list of open ports our scanner "found" on the target
found_ports = [22, 80, 3389]

# We loop through the ports we found to see what they are!
for port in found_ports:
    # We check if the port exists in our cheat sheet dictionary
    if port in port_cheat_sheet:
        service = port_cheat_sheet[port]
        # We use an 'f-string' (putting an 'f' before the quotes) to easily print variables inside the text!
        print(f"[!] OPEN PORT DETECTED: {port} -> {service}")
    else:
        print(f"[!] OPEN PORT DETECTED: {port} -> Unknown Service")

print("\n[!] WARNING: Remote Desktop (3389) is open. This is a major security risk!")
