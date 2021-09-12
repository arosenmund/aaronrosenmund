#!/bin/usr python3
# dhcp server
# https://projects2009developer.files.wordpress.com/2009/03/scapy.pdf
from scapy.all import *

#input info
server_ip="12.154.254.33"
client_ip="10.154.254.15"
server_mac="00:0B:CD:AE:9F:C6"
client_mac="00:02:a5:ea:54:20"
subnet_mask="255.255.255.192"
gateway="12.154.254.10"

#DHCP leases
def detect_dhcp(pkt):
    #If DHCP Discover then DHCP Offer
    if pkt[DHCP] and pkt[DHCP].options[0][1] == 1:
        print("\nDHCP Discover packet detected")
        sendp(
            Ether(src=server_mac,dst="ff:ff:ff:ff:ff:ff")/
            IP(src=server_ip,dst="255.255.255.255")/
            UDP(sport=67,dport=68)/
            BOOTP(op=2,yiaddr=client_ip,siaddr=server_ip,giaddr=gateway,chaddr=client_mac,xid=pkt[BOOTP].xid)/
            DHCP(options=[('message­type','offer')])/
            DHCP(options=[('subnet_mask',subnet_mask)])/
            DHCP(options=[('server_id',server_ip),('end')])
        )
        print("DHCP Offer packet sent\n.")
    #If DHCP Request then DHCP Ack
    if pkt[DHCP] and pkt[DHCP].options[0][1] == 3:
        print("DHCP Request packet detected")
        sendp(
            Ether(src=server_mac,dst="ff:ff:ff:ff:ff:ff")/
            IP(src=server_ip,dst="255.255.255.255")/
            UDP(sport=67,dport=68)/
            BOOTP(
                op=2,
                yiaddr=client_ip,siaddr=server_ip,
                giaddr=gateway,
                chaddr=client_mac,
                xid=pkt[BOOTP].xid
                )/
            DHCP(options=[('message­type','ack')])/
            DHCP(options=[('subnet_mask',subnet_mask)])/
            DHCP(options=[('server_id',server_ip),('end')]))
        print("DHCP Ack packet sent\n\nCtrl+C to exit\n")
#exit when lease has been granted
    #sys.exit(0)
#sniff DHCP requests
def start():
    #may need to set count so it runs more often
    sniff(filter="arp or (udp and (port 67 or 68))", prn=detect_dhcp, iface="Intel(R) Dual Band Wireless-AC 3165", store=0)

start()
