import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    """
    Takes a string containing XML and attempts to parse it.
    Returns:
        (root, False) if XML is valid
        (None, True) if XML is malformed
    """
    try:
        root = ET.fromstring(xml_string)
        return root, False  # not malformed
    except ET.ParseError:
        return None, True  # malformed
