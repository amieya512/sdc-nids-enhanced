# SDC-NIDS-Enhanced

This project extends the Kitsune Network Intrusion Detection System by integrating XML payload extraction and analysis. The repository includes all source code, PCAP files, and instructions needed to reproduce the results.

---

## Project Overview

### Kitsune NIDS
A lightweight online anomaly detection system based on an ensemble of autoencoders. It processes PCAP traffic sequentially and outputs per-packet RMSE anomaly scores.

### XML Analysis Module
Extracts XML payloads from packets, parses them, generates XML-level features, and assigns an XML anomaly score.

### Integration
The main script executes both systems on the provided PCAPs and generates a combined visualization comparing Kitsune anomaly scores and XML feature scores.

---

## Repository Structure

```
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
```

---

## Installation and Setup

### 1. Clone the repository
```
git clone https://github.com/<your-username>/sdc-nids-enhanced.git
cd sdc-nids-enhanced
```

### 2. Python Version
This project was tested with:

**Python 3.10**

### 3. Create and activate a virtual environment

**Windows:**
```
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Install TShark (required for PyShark)

**Windows:** Install Wireshark  
**macOS:** `brew install wireshark`  
**Linux:** `sudo apt install tshark`

Ensure `tshark` is in your PATH.

---

## Running the Application

To run both Kitsune and the XML detector:

```
python xml_integration.py
```

This performs:

- PCAP parsing  
- XML extraction  
- XML feature generation  
- Kitsune anomaly detection  
- Combined graph generation  

All necessary PCAPs are included.

---

## Scholarly References

### Foundational Reference
Mirsky, Y., Doitshman, T., Elovici, Y., & Shabtai, A. (2018).  
*Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection.*  
NDSS Symposium.  
https://www.ndss-symposium.org/ndss-paper/kitsune-an-ensemble-of-autoencoders-for-online-network-intrusion-detection/

### Contemporary Reference
Ćirić, V., Milojković, A., & Milošević, M. (2024).  
*Autoencoder-Based Network Intrusion Detection on Multiple Datasets.*  
2024 IEEE MELECON Conference.  
doi: 10.1109/MELECON56669.2024.10608696

---

## Reproducibility
All code, datasets (PCAPs), and scripts required to reproduce the results are included. Running the integration script with Python 3.10 and the listed dependencies reproduces the demonstrated output.
