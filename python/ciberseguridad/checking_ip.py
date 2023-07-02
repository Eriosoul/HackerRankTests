import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"The name of this advice is: {hostname}")
print(f"The ip of this advice is: {ip}")