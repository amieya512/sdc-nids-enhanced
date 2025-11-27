# XML FILE EXTRACTION


## 📘 Overview
This project extends the Kitsune Network Intrusion Detection System to analyze XML-based network traffic. Many devices communicate using XML, and these messages can be manipulated or altered by attackers. To support detection of abnormal XML behavior, the project captures network traffic, extracts XML payloads from PCAP files, parses the XML, and converts it into features that Kitsune can process

---

## 🎯 Project Goal
The goal of this project is to create an end-to-end XML intrusion detection pipeline. Success includes capturing network traffic containing XML, extracting XML messages from PCAP files, parsing and validating the XML structure, and generating numerical features that allow Kitsune to learn normal XML behavior. The final objective is for Kitsune to detect differences between normal XML traffic and intentionally altered or malicious XML samples.

---

# 👥 Team Members & Roles

## **Role 1 – XML Payload Extraction**  
**Name:** Ami Bell
**Description:**  
Responsible for extracting XML payloads from PCAP files using Scapy. This role reads captured network traffic, identifies packets containing XML, isolates complete XML strings, and prepares them for XML parsing in Role 2.
---

## **Role 2 – XML Parsing**  
**Name:** CJ Faircloth  
**Description:**  
Implemented the XML parsing component of the pipeline by creating two files:

- xml_parser.py
- xml_parser_tester.py

xml_parser.py contains the required 'parse_xml(xml_string)' function.  
This function:

- Returns **(root, False)** if the XML string is *valid* and successfully parsed  
- Returns **(None, True)** if the XML string is *malformed* or fails to parse  

xml_parser_tester.py tests the parser using both valid and invalid XML samples to verify correct behavior.

---

## **Role 3 – XML Feature Extractor**  
**Name:** Nivah Nyangaresi  
**Description:**  
Implemented the XML feature extraction component of the pipeline by creating two files:

xml_features.py
xml_fe_tester.py

xml_features.py contains the required xml_features(root, malformed_flag, xml_string) function.
This function takes the parsed XML output from Role 2 and converts it into a fixed-length numerical feature vector for use with Kitsune.
The function extracts 8 features:

tag_count – Total number of XML tags
unique_tag_count – Number of unique tag names
max_depth – Maximum depth of the XML tree
attribute_count – Total number of XML attributes
text_length – Total length of text content within tags
has_metric – 1 if <MetricValue> tag is present, 0 otherwise
malformed – 1 if XML parsing failed, 0 if valid
size_bytes – Size of the XML string in bytes

For valid XML, the function returns a meaningful feature vector.
For malformed XML, the function returns a zero-structure vector with the malformed flag set to 1.
xml_fe_tester.py tests the feature extractor using valid, malicious-like, and malformed XML samples to verify correct behavior and consistent vector length.
---

## **Role 4 – XML integration 
**Name:** Jeremy Adiuku
**Description:**  
integration of all 3 roles with the responsiblity of training and testing of the Kitsune. In the xml_integration.py file are the functions: def get_xml_vector_from_packet(packet), def kitsune_packet_features(packet, fe), def train_kitsune(normal_pcap_path), def test_kitsune(malicious_pcap_path, fe), which all include functions from the other files from the other roles.

---
