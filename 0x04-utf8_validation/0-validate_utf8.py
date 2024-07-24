#!/usr/bin/python3
"""
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
"""
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize a variable to keep track of the number of expected bytes
    num_expected_bytes = 0

    # Iterate through each integer in the data
    for byte in data:
        # Check if the byte is a continuation byte (starts with '10')
        if num_expected_bytes == 0:
            if byte >> 5 == 0b110:
                num_expected_bytes = 1
            elif byte >> 4 == 0b1110:
                num_expected_bytes = 2
            elif byte >> 3 == 0b11110:
                num_expected_bytes = 3
            elif byte >> 7 == 0b0:
                continue  # Single-byte character
            else:
                return False
        else:
            # Check if the byte is a continuation byte (starts with '10')
            if byte >> 6 != 0b10:
                return False
            num_expected_bytes -= 1

    # If there are remaining expected bytes, it's invalid
    return num_expected_bytes == 0


