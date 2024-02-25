# Network Port Scanner

This Python script is a simple yet efficient network port scanner. It allows you to scan a single port, a range of ports, or all ports on a given IP address. The script utilizes multithreading for faster scanning and supports both TCP and UDP port scanning.

## Notes

- This is slower than NMAP. It was made as a learning project.
- The ports.py file contains a list of the most used ports by NMAP, ensuring a higher efficiency, faster, 99% accuracy scan. This list was pulled directly from NMAP.

## Features

- **Single Port Scan:** Scan a single port on the specified IP address.
- **Port Range Scan:** Scan a range of ports on the specified IP address.
- **All Ports Scan:** Scan all ports (0-65535) on the specified IP address.
- **Optimized TCP Scan:** Perform a high-efficiency TCP scan using the top 3,328 TCP ports according to NMAP.

## Configuration

- Modify the `ip_address` variable in the script to specify the target IP address.

## Disclaimer

This was made as an educational project for me, don't do anything illegal with it.

## Acknowledgments

- The script utilizes the `scapy` library for packet manipulation and network scanning.
- Inspiration for the optimized TCP scan comes from NMAP's top TCP ports list.

---
**Note:** Please ensure you have appropriate permissions before scanning any network or IP address. Always use this tool responsibly and adhere to ethical hacking principles and guidelines.
