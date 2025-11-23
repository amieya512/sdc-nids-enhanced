from xml_parser import parse_xml

samples = [
    "<Metric><Value>50</Value></Metric>",
    "<Metric><Value>50</Value>",  # malformed
    "<A><B><C>123</C></B></A>",
    "<?xml version='1.0'?><Root></Root>",
    "<root><unclosed></root>"  # malformed
]

for xml in samples:
    root, malformed = parse_xml(xml)
    print(f"XML: {xml}")
    print("Malformed:", malformed)
    print("Parsed root:", root)
    print("-----------------------------------")
