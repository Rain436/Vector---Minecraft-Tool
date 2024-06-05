## --- Info ---
## --- Module tag: Checker

import requests
import socket

print ("[+] Loaded - IP Checker")

ip = input("[!] Target IP:")

try:
        ip_address = socket.gethostbyname(ip)
        print(f"[+] {ip} - Loaded")
        print(f"[?] Target IP: {ip_address}")
except socket.gaierror:
        print(f"[-] {ip} - Failed Loaded")
