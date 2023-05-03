#!/usr/bin/env python3
# Sierra Maldonado
# Worked with Geneva, Justin H, and Nick A


import ipaddress
from scapy.all import IP, ICMP, sr1, TCP

# Define the function to perform the ICMP ping sweep
def IPsweep(ip):
    # Create an IPv4Address object from the IP address
    ipA = ipaddress.IPv4Address(ip)
    # Send an ICMP echo request packet and wait for a response
    response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
    # Check if a response was received
    if response:
        if response[ICMP].code == 3:
        # Display a message indicating that the network is blocking ICMP traffic
            print(f"{ip}: Network is actively blocking ICMP traffic")
        # Display the IP address and ICMP code
        else:
            print(f"{ipA}: {response[ICMP].code}")
            print(f"({ipA}) is up")
            ip_network = ipaddress.ip_network(ipA)
            network_mask = ip_network.netmask
            print("The network mask IP is: ", network_mask)
            scanner(ip)
        
    else:
        print(f"No response from {ip}")
        
def scanner(ip):
    port_range = [22, 23, 80, 443, 3389]
    source_port = 1025
    for dsp_port in port_range:
        response = sr1(IP(dst=ip)/TCP(sport=source_port, dport=dsp_port, flags="S"), timeout=1, verbose=0)
    # If flag Ox12 received, send a RST packet. Se1()
        if (response.haslayer(TCP)):
            if (response.getlayer(TCP).flags == 0x12):
                answer = ("Open")
                print(f"Port {dsp_port} is {answer}")
                
        # If Ox14 received, notfiy if close
        elif (response.haslayer(TCP)):
            if (response.getlayer(TCP).flags == 0x14):
                    answer = ("Closed")
                    print(f"Port {dsp_port} is {answer}")
                    
        # If no flag was received 
        else:
            answer = (f"No respose received from {ip}")
            print(f"Port {dsp_port} is {answer}")
            
while True:
    # IP address ' 45.33.32.156 ' - test IP
    ip = input("Please type in a IP address: ")
    IPsweep(ip)
    