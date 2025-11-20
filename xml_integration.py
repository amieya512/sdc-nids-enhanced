import numpy as np
from scapy.all import rdpcap
from kitsune import Kitsune
import matplotlib.pyplot as plt

from xml_extractor import extract_xml_payloads     
from xml_parser import parse_xml                   
from xml_features import xml_features              

def get_xml_vector_from_packet(packet):
    if packet.haslayer("Raw"):
        try:
            payload = packet["Raw"].load.decode(errors="ignore")
        except:
            return [0]*8  

        if "<?xml" in payload:
            xml_start = payload.index("<?xml")
            xml_string = payload[xml_start:]

            root, malformed_flag = parse_xml(xml_string)
            return xml_features(root, malformed_flag, xml_string)

    # No XML present
    return [0] * 8

def kitsune_packet_features(packet, fe):
    try:
        return fe.process_packet(packet)
    except:
        return None

def train_kitsune(normal_pcap_path):

    print("\n=== TRAINING ON NORMAL XML TRAFFIC ===")

    packets = rdpcap(normal_pcap_path)
  
    fe = Kitsune(feature_number=None, mode="train")

    combined_vectors = []

    for pkt in packets:
        
        base = kitsune_packet_features(pkt, fe)
        if base is None:
            continue

      
        xml_vec = get_xml_vector_from_packet(pkt)


        combined = np.concatenate([base, xml_vec])
        combined_vectors.append(combined)

        fe.process(combined)

    print("Training complete.\nPackets processed:", len(combined_vectors))

    return fe

def test_kitsune(malicious_pcap_path, fe):

    print("\n=== TESTING ON MALICIOUS-LIKE XML TRAFFIC ===")

    packets = rdpcap(malicious_pcap_path)
    anomaly_scores = []

    for pkt in packets:
        base = kitsune_packet_features(pkt, fe)
        if base is None:
            continue

        xml_vec = get_xml_vector_from_packet(pkt)
        combined = np.concatenate([base, xml_vec])

        score = fe.process(combined)
        anomaly_scores.append(score)

    print("Testing complete. Packets processed:", len(anomaly_scores))

    return anomaly_scores

if __name__ == "__main__":

    normal_pcap = "normal.xml.pcap"
    malicious_pcap = "malicious.xml.pcap"

    # Train Kitsune
    fe = train_kitsune(normal_pcap)

    # Test Kitsune
    anomaly_scores = test_kitsune(malicious_pcap, fe)

    plt.figure(figsize=(12, 6))
    plt.plot(anomaly_scores)
    plt.title("Kitsune Anomaly Scores – Malicious XML Test")
    plt.xlabel("Packet Index")
    plt.ylabel("Anomaly Score")
    plt.grid(True)
    plt.show()

    print("\nMax Score:", max(anomaly_scores))
    print("Min Score:", min(anomaly_scores))
    print("Average Score:", sum(anomaly_scores)/len(anomaly_scores))
