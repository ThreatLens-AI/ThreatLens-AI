from scapy.all import rdpcap

def load_pcap(file_path):
    packets = rdpcap(file_path)
    return packets

