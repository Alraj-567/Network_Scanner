# Network_Scanner
A simple Python network scanner using Scapy. It scans a local subnet via ARP requests and lists active devices with their IP and MAC addresses. Great for learning basic networking and ethical hacking. Requires root privileges to run.



# 🔍 Python Network Scanner

A simple yet powerful Python tool that scans your local network using ARP requests and lists all active devices with their IP and MAC addresses.

## 📦 Features

- ✅ Scans local subnet for live devices
- 📡 Displays IP and MAC addresses
- ⚡ Fast and efficient ARP-based discovery
- 🧠 Easy to understand and beginner-friendly
- 🛡️ Useful for ethical hacking and network diagnostics

## 🧰 Requirements

- Python 3.x
- Scapy library  
  Install it using:
  ```bash
  pip install scapy

🚀 Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
Run the script with sudo:


sudo python3 Network_Scanner.py
When prompted, enter your subnet range:


Enter your IP you want to scan for : 192.168.1.0/24
Output:


Available devices in network:

IP                  MAC
192.168.1.1         00:11:22:33:44:55
192.168.1.100       aa:bb:cc:dd:ee:ff
🧠 How It Works
This tool sends ARP requests to all IPs in the specified subnet. Devices that respond are considered "alive" and their details are printed in a neat table format.

⚠️ Disclaimer
This tool is intended for educational and authorized use only. Do not scan networks you don't own or have permission to audit.



