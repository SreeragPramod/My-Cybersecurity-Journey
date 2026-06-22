OPEN SYSTEM INTERCONNECTION REFERENCE MODEL (OSI)

What is OSI?
OSI is a conceptual framework that describes how data travels across a network from one device to another. It breaks down complex networking into 7 manageable layers.

Mnemonic (Layer 7 → Layer 1):
All People Seem To Need Data Processing

Application → Presentation → Session → Transport → Network → Data Link → Physical

Layer 1: Physical Layer

The Physical Layer is the raw physical medium through which data travels. It focuses on transmitting electrical signals, light, or radio waves from one point to another.

Real World:

Ethernet cables
Fiber optic cables
Wi-Fi radio frequencies
Electrical signals

Troubleshooting:
Layer 1 issues usually involve hardware problems such as broken cables, loose connections, faulty ports, or signal interference.

Layer 2: Data Link Layer

The Data Link Layer handles communication between devices within the same local network.

Also Known As:

MAC Address Layer
Switching Layer

Real World:

MAC Addresses
Switches
Frames

Layer 3: Network Layer

The Network Layer is responsible for sending data beyond the local network to other networks. It determines the best path for data using logical addressing.

Real World:

IP Addresses
Routers
Packets

Troubleshooting:
Common Layer 3 problems include incorrect IP addresses, subnet issues, or routing errors.

Layer 4: Transport Layer

The Transport Layer ensures data is delivered between applications reliably or quickly using port numbers.

Main Protocols:
TCP (Transmission Control Protocol)

Reliable
Checks delivery
Error recovery

UDP (User Datagram Protocol)

Faster
No delivery confirmation
Used when speed matters more than reliability

Real World:

TCP
UDP
Port Numbers

Layer 5: Session Layer

The Session Layer establishes, maintains, and terminates communication sessions between devices.

Real World:

Session control protocols
Tunneling protocols

Layer 6: Presentation Layer

The Presentation Layer ensures data is in a readable format for applications. It handles translation, compression, and encryption.

Real World:

SSL/TLS encryption
ZIP compression
Data encoding

Layer 7: Application Layer

The Application Layer is the layer closest to the user. It provides network services that applications use.

Real World:

HTTP (Web browsing)
FTP (File transfer)
DNS (Domain name resolution)

This is the layer where users interact with applications such as web browsers, email clients, and messaging apps.
