import sys
import socket

objective = socket.gethostbyname(input("Insert the IP: "))

print(f"Scanning: {objective}")

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        result = s.connect_ex((objective,port))
        if result == 0:
            print("The port {} is open".format(port))
        s.close()
except:
    print("\n Exit...")
    sys.exit(0)