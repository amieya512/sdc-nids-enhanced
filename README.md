SDC-NIDS-Enhanced

This project extends the Kitsune Network Intrusion Detection System by integrating XML payload extraction and analysis. The goal is to demonstrate how payload-level feature extraction can complement network-behavior anomaly detection for SDC-style medical device communication. The repository includes all source code, PCAP files, and dependencies required to run and reproduce the project results.

Project Overview

Kitsune NIDS
A lightweight online anomaly detection system based on an ensemble of autoencoders. It processes PCAP traffic sequentially and outputs per-packet RMSE anomaly scores.

XML Analysis Module
Extracts XML payloads from packets, parses them, creates XML-level features, and assigns a simple numerical XML anomaly score.

Integration
The main script executes both systems on the provided PCAPs and generates a combined visualization comparing Kitsune-based anomaly detection with XML-feature scoring.

Repository Structure
sdc-nids-enhanced/
│
├── xml_integration.py
├── Kitsune.py
├── FeatureExtractor.py
├── netStat.py
├── AfterImage.py
│
├── XML-file-extraction/
│   ├── xml_extraction.py
│   ├── xml_parser.py
│   ├── xml_feature_extractor.py
│   └── pcaps/
│       ├── malicious.xml.pcap
│       └── normal.xml.pcap
│
├── requirements.txt
└── README.md


The pcaps/ directory contains all data needed to test and reproduce the results.

Installation and Setup
1. Clone the repository
git clone https://github.com/<your-username>/sdc-nids-enhanced.git
cd sdc-nids-enhanced


Make the repository public before submitting the link.

2. Python Version

This project was developed and tested using:

Python 3.10

This version is recommended for full compatibility.

3. Create and activate a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate


macOS / Linux:

python3 -m venv venv
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Install system dependency: TShark

PyShark requires TShark to be installed.

Windows: Install Wireshark (includes TShark)

macOS: brew install wireshark

Linux: sudo apt install tshark

Ensure tshark is accessible in your system PATH.

Running the Application

To run the full integration (Kitsune + XML scoring + visualization):

python xml_integration.py


This performs:

PCAP parsing

XML payload extraction

Feature extraction for Kitsune

XML anomaly scoring

Combined graph visualization

All needed PCAP files are already included in the repository.

Scholarly References

Foundational Reference
Mirsky, Y., Doitshman, T., Elovici, Y., & Shabtai, A. (2018).
Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection.
Network and Distributed System Security Symposium (NDSS).
https://www.ndss-symposium.org/ndss-paper/kitsune-an-ensemble-of-autoencoders-for-online-network-intrusion-detection/

Contemporary Reference
Ćirić, V., Milojković, A., & Milošević, M. (2024).
Autoencoder-Based Network Intrusion Detection on Multiple Datasets.
2024 IEEE 22nd Mediterranean Electrotechnical Conference (MELECON).
doi: 10.1109/MELECON56669.2024.10608696

This contemporary paper continues the study of autoencoder-based network intrusion detection, demonstrating the ongoing evolution of techniques first established in foundational work such as Kitsune.

Reproducibility

All code, datasets (PCAPs), and scripts required to reproduce the project results are included within the repository. Running the integration script with Python 3.10 and the listed dependencies reproduces all outcomes shown in the project demonstration.