from scapy.all import IP, TCP, UDP, ICMP, wrpcap

packets = [
    IP(src="192.168.1.10", dst="192.168.1.20") / TCP(sport=5000, dport=80),
    IP(src="192.168.1.20", dst="192.168.1.10") / TCP(sport=80, dport=5000),
    IP(src="192.168.1.10", dst="8.8.8.8") / UDP(sport=5001, dport=53),
    IP(src="192.168.1.10", dst="192.168.1.1") / ICMP()

]