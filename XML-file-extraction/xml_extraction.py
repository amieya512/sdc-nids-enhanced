from scapy.all import rdpcap
from xml_parser import parse_xml

def extract_xml_from_pcap(pcap_path):
    """
    Reads a PCAP file, scans packet payloads for XML content,
    extracts XML strings, and returns them as a list.
    """

    packets = rdpcap(pcap_path)
    xml_strings = []

    for pkt in packets:
        if pkt.haslayer("Raw"):
            raw_bytes = bytes(pkt["Raw"].load)

            # Attempt to decode payload safely
            try:
                text = raw_bytes.decode("utf-8", errors="ignore")
            except:
                continue

            # Detect any XML-like payloads
            if "<" in text and ">" in text and ("<Metric" in text or "<?xml" in text):
                # Extract only the XML portion (strip out noise)
                start = text.find("<")
                end = text.rfind(">") + 1
                xml_candidate = text[start:end].strip()

                xml_strings.append(xml_candidate)

    return xml_strings


def test_role1_with_role2(pcap_path):
    """
    Helper function to show Role 1 + Role 2 working together.
    Prints each extracted XML and whether Role 2 thinks it is malformed.
    """

    xml_list = extract_xml_from_pcap(pcap_path)

    print(f"\n[+] Extracted {len(xml_list)} XML payload(s) from {pcap_path}")

    for xml_string in xml_list:
        print("\n--- Extracted XML ---")
        print(xml_string)

        root, malformed = parse_xml(xml_string)
        print("Parsed OK?" , not malformed)
        print("Malformed:", malformed)
        print("---------------------")


if __name__ == "__main__":
    # Update paths to your local PCAP folder
    normal_pcap = "pcaps/normal.xml.pcap"
    malicious_pcap = "pcaps/malicious.xml.pcap"

    print("\n=== Testing Normal PCAP ===")
    test_role1_with_role2(normal_pcap)

    print("\n=== Testing Malicious PCAP ===")
    test_role1_with_role2(malicious_pcap)
