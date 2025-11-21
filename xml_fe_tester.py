import xml.etree.ElementTree as ET
from xml_features import xml_features, get_feature_names, print_features


def test_xml_features():
    """
    Test the xml_features function with various XML inputs.
    """
    print("=" * 60)
    print("Role 3: XML Feature Extraction - Test Suite")
    print("=" * 60)
    
    results = {
        'passed': 0,
        'failed': 0,
        'valid_parsed': 0,
        'malformed_detected': 0
    }
    
    # Test Case 1: Normal, valid XML
    print("\n[TEST 1] Normal XML with MetricValue")
    xml_normal = """<?xml version="1.0"?>
<Metric>
    <MetricValue>98.6</MetricValue>
    <Timestamp>2025-11-18T10:30:00</Timestamp>
    <Unit>Celsius</Unit>
</Metric>"""
    
    try:
        root = ET.fromstring(xml_normal)
        features = xml_features(root, False, xml_normal)
        print_features(features, xml_normal)
        results['valid_parsed'] += 1
        if len(features) == 8 and features[5] == 1:  # has_metric should be 1
            results['passed'] += 1
            print("[PASS] Feature vector length correct, MetricValue detected")
        else:
            results['failed'] += 1
            print("[FAIL] Unexpected feature values")
    except ET.ParseError:
        features = xml_features(None, True, xml_normal)
        print_features(features, xml_normal)
        results['failed'] += 1
    
    # Test Case 2: Complex valid XML with attributes
    print("\n[TEST 2] Complex XML with attributes and deeper nesting")
    xml_complex = """<?xml version="1.0"?>
<Alert id="1001" priority="high">
    <Code>1001</Code>
    <Message type="warning">
        <Text>System temperature elevated</Text>
        <Details>
            <Location>Sensor 3</Location>
            <Value>105.2</Value>
        </Details>
    </Message>
</Alert>"""
    
    try:
        root = ET.fromstring(xml_complex)
        features = xml_features(root, False, xml_complex)
        print_features(features, xml_complex)
        results['valid_parsed'] += 1
        if len(features) == 8 and features[3] > 0:  # should have attributes
            results['passed'] += 1
            print("[PASS] Feature vector length correct, attributes detected")
        else:
            results['failed'] += 1
            print("[FAIL] Unexpected feature values")
    except ET.ParseError:
        features = xml_features(None, True, xml_complex)
        print_features(features, xml_complex)
        results['failed'] += 1
    
    # Test Case 3: Malicious-like XML
    print("\n[TEST 3] Malicious-like XML with unusual structure")
    xml_malicious = """<?xml version="1.0"?>
<Metric>
    <MetricValue>999999999</MetricValue>
    <DebugMode>ON</DebugMode>
    <AdminAccess>ENABLED</AdminAccess>
    <Command>rm -rf /</Command>
</Metric>"""
    
    try:
        root = ET.fromstring(xml_malicious)
        features = xml_features(root, False, xml_malicious)
        print_features(features, xml_malicious)
        results['valid_parsed'] += 1
        if len(features) == 8:
            results['passed'] += 1
            print("[PASS] Malicious-like XML processed correctly")
        else:
            results['failed'] += 1
    except ET.ParseError:
        features = xml_features(None, True, xml_malicious)
        print_features(features, xml_malicious)
        results['failed'] += 1
    
    # Test Case 4: Malformed XML (missing closing tag)
    print("\n[TEST 4] Malformed XML (missing closing tag)")
    xml_malformed = """<?xml version="1.0"?>
<Metric>
    <MetricValue>54"""
    
    try:
        root = ET.fromstring(xml_malformed)
        features = xml_features(root, False, xml_malformed)
        print_features(features, xml_malformed)
        results['failed'] += 1
        print("[FAIL] Should have detected malformed XML")
    except ET.ParseError:
        features = xml_features(None, True, xml_malformed)
        print_features(features, xml_malformed)
        results['malformed_detected'] += 1
        if features[6] == 1:  # malformed flag should be 1
            results['passed'] += 1
            print("[PASS] Malformed flag correctly set to 1")
        else:
            results['failed'] += 1
    
    # Test Case 5: XML without MetricValue
    print("\n[TEST 5] Valid XML without MetricValue tag")
    xml_no_metric = """<?xml version="1.0"?>
<SystemStatus>
    <CPU>45</CPU>
    <Memory>2048</Memory>
    <Disk>512</Disk>
</SystemStatus>"""
    
    try:
        root = ET.fromstring(xml_no_metric)
        features = xml_features(root, False, xml_no_metric)
        print_features(features, xml_no_metric)
        results['valid_parsed'] += 1
        if features[5] == 0:  # has_metric should be 0
            results['passed'] += 1
            print("[PASS] has_metric correctly set to 0")
        else:
            results['failed'] += 1
            print("[FAIL] has_metric should be 0")
    except ET.ParseError:
        features = xml_features(None, True, xml_no_metric)
        print_features(features, xml_no_metric)
        results['failed'] += 1
    
    # Print Summary
    print_summary(results)


def print_summary(results):
    """Print test summary and feature vector format."""
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"Tests Passed:        {results['passed']}")
    print(f"Tests Failed:        {results['failed']}")
    print(f"Valid XML Parsed:    {results['valid_parsed']}")
    print(f"Malformed Detected:  {results['malformed_detected']}")
    
    print("\n" + "=" * 60)
    print("FEATURE VECTOR FORMAT")
    print("=" * 60)
    print("\nAll feature vectors have 8 elements:")
    for i, name in enumerate(get_feature_names()):
        print(f"  [{i}] {name}")
    
    print("\nVector length is consistent for both valid and malformed XML.")
    print("This ensures compatibility with Kitsune integration (Role 4).")
    print("=" * 60)


if __name__ == "__main__":
    test_xml_features()
    
    print("\n" + "=" * 60)
    print("Role 3 testing complete!")
    print("=" * 60)