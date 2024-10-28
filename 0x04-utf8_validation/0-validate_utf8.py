#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determine if the data set represents a valid UTF-8 encoding.
    :param data: List of integers, each integer represents
    a byte (1 byte = 8 bits)
    :return: True if data is valid UTF-8 encoding, otherwise False
    """
    num_bytes = 0
    MASK1 = 1 << 7
    MASK2 = 1 << 6

    for num in data:

        byte = num & 0xFF

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:

            if not (byte & MASK1 and not (byte & MASK2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
