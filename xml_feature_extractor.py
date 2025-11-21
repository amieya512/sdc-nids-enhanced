import xml.etree.ElementTree as ET


def xml_features(root, malformed_flag, xml_string):
    """
    Extract a fixed-length feature vector from parsed XML.
    
    Args:
        root: Parsed XML element tree (or None if parsing failed)
        malformed_flag: Boolean indicating if XML parsing failed
        xml_string: Original XML string
    
    Returns:
        List of 8 numerical features:
        [tag_count, unique_tag_count, max_depth, attribute_count,
         text_length, has_metric, malformed, size_bytes]
    """
    # Handle malformed XML - return zeros with malformed flag set
    if malformed_flag or root is None:
        size_bytes = len(xml_string.encode('utf-8'))
        return [0, 0, 0, 0, 0, 0, 1, size_bytes]
    
    # Extract all tags from the XML tree
    tags = list(root.iter())
    
    # Feature 1: Total number of XML tags
    tag_count = len(tags)
    
    # Feature 2: Number of unique tag names
    unique_tag_count = len(set([elem.tag for elem in tags]))
    
    # Feature 3: Maximum depth of the XML tree
    def get_depth(element, level=1):
        """Recursively calculate the maximum depth of XML tree."""
        if len(element) == 0:
            return level
        return max(get_depth(child, level + 1) for child in element)
    
    max_depth = get_depth(root)
    
    # Feature 4: Total number of XML attributes
    attribute_count = sum(len(elem.attrib) for elem in tags)
    
    # Feature 5: Total length of text content within tags
    text_length = sum(len(elem.text.strip()) for elem in tags if elem.text)
    
    # Feature 6: Check for presence of MetricValue tag (domain-specific)
    has_metric = 1 if root.find(".//MetricValue") is not None else 0
    
    # Feature 7: Malformed flag (0 for valid XML)
    malformed = int(malformed_flag)
    
    # Feature 8: Size of XML string in bytes
    size_bytes = len(xml_string.encode('utf-8'))
    
    return [
        tag_count,
        unique_tag_count,
        max_depth,
        attribute_count,
        text_length,
        has_metric,
        malformed,
        size_bytes
    ]


def get_feature_names():
    """
    Return the names of features in the feature vector.
    Useful for debugging and visualization.
    
    Returns:
        List of feature names corresponding to the feature vector indices
    """
    return [
        'tag_count',
        'unique_tag_count',
        'max_depth',
        'attribute_count',
        'text_length',
        'has_metric',
        'malformed',
        'size_bytes'
    ]


def print_features(feature_vector, xml_sample=None):
    """
    Pretty print feature vector with labels.
    
    Args:
        feature_vector: List of numerical features
        xml_sample: Optional XML string sample (first 100 chars displayed)
    """
    feature_names = get_feature_names()
    
    if xml_sample:
        print(f"\nXML Sample: {xml_sample[:100]}{'...' if len(xml_sample) > 100 else ''}")
    
    print("\nExtracted Features:")
    print("-" * 40)
    for name, value in zip(feature_names, feature_vector):
        print(f"{name:20s}: {value}")
    print("-" * 40)


if __name__ == "__main__":
    print("This module provides xml_features() for Role 3.")
    print("Run xml_fe_tester.py to test the feature extraction.")