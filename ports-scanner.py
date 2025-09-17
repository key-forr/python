import socket
import termcolor


def scan(target, ports):
    print('\n' + 'Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port is Opened " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))

    for ip_address in targets.split(','):
        scan(ip_address.strip(' '), ports)
else:
    scan(targets, ports)
