Networking Devices Study Guide

Data centers rely on a whole team of specialized hardware devices working together to move data around the world. Here is the ultimate breakdown:

The Traffic Cops: Routers & Switches

Router (Layer 3):
The GPS of the network. It connects different IP subnets together (like connecting your home network to the internet). It uses IP Addresses to determine the next "hop" to get data to its destination. It connects LANs and WANs using copper or fiber cables.

Note: Sometimes routers are built directly into switches.

Switch (Layer 2):
The local postmaster. It connects devices within the same network. It uses MAC Addresses to send data to the exact right device.

ASIC:
Switches are incredibly fast because their switching logic is built directly into physical hardware chips called ASICs (Application-Specific Integrated Circuits).

PoE (Power over Ethernet):
Many enterprise switches can send electricity down the network cable to power devices like phones and cameras.

The Security Guards: Firewalls, IDS & IPS

Firewall:
Sits at the Ingress (entrance) and Egress (exit) of a network to control who is allowed in or out. It can also act as a Layer 3 Router.

Traditional Firewall:
Filters traffic based on basic rules like TCP/UDP port numbers.

NGFW (Next-Generation Firewall):
Much smarter than traditional firewalls. It can inspect traffic deeply to identify specific applications and block or allow them.

VPNs:
Firewalls are often used to create encrypted tunnels (VPNs) between two remote sites so they can share data securely over the public internet.

IDS (Intrusion Detection System):
The alarm system. It watches for attacks and alerts administrators, but it cannot stop the attack.

IPS (Intrusion Prevention System):
The bouncer. It watches for attacks and actively blocks or drops malicious traffic.

Note: IPS functionality is often built into modern firewalls.

The Traffic Managers: Load Balancers & Proxies

Load Balancer:
The reason huge websites don’t crash. It sits between the internet and a farm of servers.

Distribution:
It spreads millions of user requests evenly across multiple servers.

Health Checks:
If server hardware or software fails, the load balancer notices and removes it from rotation instantly.

Extra Features:
It can handle TCP/SSL encryption (SSL offloading), cache data for faster responses, and prioritize certain types of traffic.

Proxy Server:
The middleman. It sits between the user and the internet.

How it works:
You send a request to the proxy, the proxy requests the website on your behalf, checks the response for malicious content, and then sends it back to you.

Benefits:
Caching, access control, and virus scanning.

Types:
Explicit Proxy (the application knows it is using the proxy)
Transparent Proxy (invisible to the user)

The Vaults: NAS vs SAN

Both require massive bandwidth, so they are usually kept on isolated, highly efficient networks.

NAS (Network Attached Storage):
Works at the File Level. If you want to change one sentence in a document, you must pull the entire file across the network, change it, and send the entire file back.

Easier to set up, but slower for large edits.

SAN (Storage Area Network):
Works at the Block Level. If you want to change one sentence in a massive database, you only pull and modify the specific block of data you need.

Much faster and more efficient for heavy reading and writing.

The Airwaves: Access Points & WLCs

Access Point (AP):
A Layer 2 device that acts as a bridge between a wired Ethernet network and a wireless Wi-Fi network. It extends network connectivity through the air.

WLC (Wireless LAN Controller):
A centralized management device. Instead of configuring 50 Access Points individually, you use a WLC to manage, update, and configure all of them from one screen.

Usually, all APs and the WLC need to be made by the same manufacturer (for example, Cisco).
