import socket
import termcolor


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port is Opened " + str(port))
        sock.close()
    except:
        print("[-] Port is Closed" + str(port))


targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = input("[*] Enter How Many Ports You Want to Scan: ")

if ',' in targets:
    print("[*] Scanning Multiple Targets")

    for ip_address in targets.split(','):
        scan(ip_address.strip(' '), ports)
else:
    scan(targets, ports)
