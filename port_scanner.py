#!/usr/bin/env python3
import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535


print("""
\t┏━━━┓┏━━━┳━┓╋┏┳━━┳━━━┳━━━┓
\t┃┏━━┛┃┏━┓┃┃┗┓┃┣┫┣┫┏━━┫┏━━┛
\t┃┗━━┓┃┗━━┫┏┓┗┛┃┃┃┃┗━━┫┗━━┓
\t┃┏━━┛┗━━┓┃┃┗┓┃┃┃┃┃┏━━┫┏━━┛
\t┃┗━━┓┃┗━┛┃┃╋┃┃┣┫┣┫┃╋╋┃┃
\t┗━━━┛┗━━━┻┛╋┗━┻━━┻┛╋╋┗┛""")
print("\n****************************************************************")
print("\n* Copyright of EnthernetCode, 2023                             *")
print("\n* https://www.enthernet.com______________comming_soon          *")
print("\n* https://www.github.com/Enthernetcode                         *")
print("\n****************************************************************")

open_ports = []
closed_ports = []
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")
    

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
        closed_ports.append(port)

for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")

print(r"Would you like to see the closed Ports")
opt = input("Yes or No: \t").lower()
if opt=="yes":
 for port in closed_ports:
    print(f"Port {port} is closed on {ip_add_entered}.")

