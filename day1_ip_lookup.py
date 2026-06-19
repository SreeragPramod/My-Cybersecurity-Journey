import socket
webiste = "google.com"
ip_address = socket.gethostbyname(website)
print("The IP address of", website, "is", ip_address)
