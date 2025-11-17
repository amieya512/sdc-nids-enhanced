import pyshark

def extract_xml_payloads(pcap_path):
    print(f"[+] Reading packets from: {pcap_path}")
    capture = pyshark.FileCapture(pcap_path, use_json=True)

    for packet in capture:
        try:
            if 'http' in packet:
                if hasattr(packet.http, 'file_data'):
                    payload = packet.http.file_data.binary_value.decode(errors='ignore')
                    if payload.strip().startswith('<?xml'):
                        print("\n--- XML Payload Found ---")
                        print(payload[:500])  # Print only first 500 characters
        except Exception as e:
            continue  # Ignore parsing issues

    capture.close()
    print("[+] Done.")

if __name__ == "__main__":
    pcap_file = "data_sdc11073/test_capture.pcapng"
  # Replace with your file
    extract_xml_payloads(pcap_file)
