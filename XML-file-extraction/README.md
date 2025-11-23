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

## **Role 3 – _Title of Role_**  
**Name:** _Full Name_  
**Description:**  
Provide a short paragraph describing what this role is responsible for.  
Describe tools, features, or code they contributed.

---

## **Role 4 – _Title of Role_**  
**Name:** _Full Name_  
**Description:**  
Provide a short paragraph describing what this role is responsible for.  
Mention their major contributions or focus areas.

---
