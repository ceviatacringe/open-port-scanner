import socket
import time
import threading
import random
from scapy.all import sr1, IP, TCP, UDP, ICMP
from ports import toptcpports


# Example: "45.33.32.156" or "scanme.nmap.org" - The script will resolve sites, do not use URL (http://scanme.nmap.org/)
# This is the ip of nmap scanme, a site meant for scanning and testing tools such as this one legally.
ip_address = "127.0.0.1"
lock = threading.Lock()


# Resolve IP from hostname
if any(char.isalpha() for char in ip_address):
    try:
        print(f"Resolved {ip_address} as {socket.gethostbyname(ip_address)}")
        ip_address = socket.gethostbyname(ip_address)
    except:
        print("Unable to get IP from hostname.")


# Timer decorator for functions
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Started running {func.__name__}")
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Finished {func.__name__} in {elapsed_time:.2f} seconds")
        return result
    return wrapper


# Function to scan a single port
def scan_single_port(ip: str, port: str) -> None:
    try:
        source_port = random.randint(1025, 65534)
        response = sr1(IP(dst=ip) / TCP(sport=source_port, dport=port, flags="S"), timeout=2, verbose=0)
        if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
            with lock:
                #Port is open
                print(f"Port {port} is open on {ip}")
    except Exception as e:
        with lock:
            print(f"An error occurred with port {port} on {ip}: {e}")


# Scan a range of ports
@timer
def scan_port_range(ip: str, port_range: dict) -> None:
    threads = []
    for port in range(port_range['min'], port_range['max'] + 1):
        thread = threading.Thread(target=scan_single_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Scans all possible ports, from 0 to 65535, will take a while.
@timer
def scan_all_ports(ip: str) -> None:
    scan_port_range(ip, {'min': 0, 'max': 65535})


@timer
def optimal_tcp_scan(ip):
    # Make sure toptcpports is imported, either through .py import or copy paste it inside as variable.
    """99% Accuracy, high efficiency TCP scanning using the top 3,328 TCP ports according to NMAP."""
    threads = []
    for port in toptcpports:
        thread = threading.Thread(target=scan_single_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


#scan_single_port(ip_address, 80)  # Example usage: scan only port 80
#scan_port_range(ip_address, {'min': 0, 'max': 8000})
optimal_tcp_scan(ip_address)
#scan_all_ports(ip_address)



