OPEN SYSTEM INTERCONNECTION REFERENCE MODEL (OSI)

What is it?

A conceptual framework that describes exactly how data travels across a network from one device to another. It breaks down complex networking into 7 manageable pieces (layers).

The Golden Mnemonic (Top to Bottom: Layer 7 to 1)

All People Seem To Need Data Processing

(Application, Presentation, Session, Transport, Network, Data Link, Physical)

Layer 1: The Physical Layer ("The Cables")

This is the raw, physical way data travels. It's all about moving electrical signals, light, or radio waves from point A to point B.

Real World:
Cables (Ethernet/Fiber), radio frequencies (Wi-Fi), and raw electrical signals.

Troubleshooting:
If you have a Layer 1 problem, you might need to fix a broken cable, punch down a wire, run a loopback test, or simply plug something in.

Layer 2: The Data Link Layer ("The Local Switch")

This is the fundamental layer for communicating between two devices on the same local network.

Also known as:
The MAC Address Layer or the Switching Layer.

Real World:
MAC Addresses, Switches, and Data Frames.

Layer 3: The Network Layer ("The GPS / Routing")

This layer gets data out of your local network and sends it across the world. It looks at destination addresses and calculates the best path to get there. It can also fragment (split) data into smaller pieces to fit through the network.

Real World:
IP Addresses, Routers, and Packets.

Troubleshooting:
If you can't reach a website but your cable is plugged in, it is often a Layer 3 problem (bad IP address, bad routing table, etc.).

Layer 4: The Transport Layer ("The Post Office")

This layer is responsible for transporting data reliably (or quickly) from one application to another using Port Numbers.

The Big Two Protocols:

TCP:
Reliable and checks for delivery.

UDP:
Fast and does not check for delivery.

Real World:
TCP, UDP, and Port Numbers.

Layer 5: The Session Layer ("The Handshake")

Before any data transfer begins, devices need to agree to communicate. This layer sets up, maintains, and tears down the session (conversation) between devices.

Real World:
Control Protocols and Tunneling Protocols.

Layer 6: The Presentation Layer ("The Translator")

This layer ensures the data is in a format the application can read. It prepares data by translating, compressing, or securing it.

Real World:
Encryption (SSL/TLS), Compression (ZIP), and Encoding.

Layer 7: The Application Layer ("The Window")

This is the layer closest to the user. It provides network services that software applications (like a web browser) use to perform tasks.

Real World:
HTTP (Web), FTP (File Transfer), DNS (Translating names to IPs).

Note:
While "Eyes" is a great way to visualize it, technically what we see is the application UI using Layer 7 to fetch data.
