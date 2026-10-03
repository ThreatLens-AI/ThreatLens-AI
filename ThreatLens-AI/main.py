from packet_analyzer import load_pcap

print("=== ThreatLens-AI ===")

pcap_file = input("Enter PCAP file path: ")
packets = load_pcap(pcap_file)
print("Packets Captured:", len(packets))
