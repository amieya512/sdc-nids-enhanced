import numpy as np
import matplotlib.pyplot as plt
from scapy.all import rdpcap

import sys, os
sys.path.append(os.path.abspath("XML-file-extraction"))

from xml_extraction import extract_xml_from_pcap
from xml_parser import parse_xml
from xml_feature_extractor import xml_features

from Kitsune import Kitsune


# -----------------------------------------------------
# XML scoring (this part works fine)
# -----------------------------------------------------
def extract_xml_from_packet(packet):
    if packet.haslayer("Raw"):
        try:
            payload = packet["Raw"].load.decode(errors="ignore")
        except:
            return None

        if "<?xml" in payload:
            idx = payload.index("<?xml")
            return payload[idx:]

    return None


def extract_xml_score(packet):
    xml_string = extract_xml_from_packet(packet)
    if xml_string is None:
        return 0

    root, malformed = parse_xml(xml_string)
    features = xml_features(root, malformed, xml_string)
    return sum(features)


# -----------------------------------------------------
# Run Kitsune the CORRECT way:
# Kitsune internally loads the pcap and the FE
# You simply call proc_next_packet() until finished
# -----------------------------------------------------
def run_kitsune(file_path):
    kit = Kitsune(
        file_path=file_path,
        limit=None,                 # read entire pcap
        max_autoencoder_size=10,
        FM_grace_period=1000,
        AD_grace_period=5000,
        learning_rate=0.1,
        hidden_ratio=0.75,
        sensitivity=1
    )

    rmses = []
    while True:
        score = kit.proc_next_packet()
        if score == -1:
            break
        rmses.append(score)

    return rmses


# -----------------------------------------------------
# XML scoring pipeline
# -----------------------------------------------------
def run_xml_detector(file_path):
    pkts = rdpcap(file_path)
    scores = []
    for p in pkts:
        scores.append(extract_xml_score(p))
    return scores


# -----------------------------------------------------
# Main: Run BOTH systems
# -----------------------------------------------------
def main():
    malicious_pcap = "XML-file-extraction/pcaps/malicious.xml.pcap"

    print("Running Kitsune...")
    kitsune_scores = run_kitsune(malicious_pcap)

    print("Running XML detector...")
    xml_scores = run_xml_detector(malicious_pcap)

    # Pad xml scores if fewer than Kitsune’s packets
    if len(xml_scores) < len(kitsune_scores):
        xml_scores += [0] * (len(kitsune_scores) - len(xml_scores))

    plt.figure(figsize=(12,6))
    plt.plot(kitsune_scores, label="Kitsune RMSE")
    plt.plot(xml_scores, label="XML Score")
    plt.legend()
    plt.xlabel("Packet Index")
    plt.ylabel("Score")
    plt.title("Kitsune + XML Detection")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
