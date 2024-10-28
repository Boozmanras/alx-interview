# UTF-8 Validation Project

## Overview

This project is designed to determine if a given dataset represents valid UTF-8 encoding. Each character in UTF-8 can be encoded with 1 to 4 bytes, and this Python program ensures that each byte adheres to the UTF-8 standard by verifying the correct format of bits in each byte.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.4.3
- The project files should adhere to the PEP 8 style guide (version 1.7.x).
- All files are executable and should have a shebang line as the first line (`#!/usr/bin/python3`).
- A `README.md` file is mandatory.

## Structure

- `0-validate_utf8.py`: Python script containing the `validUTF8(data)` function.
- `0-main.py`: Example file to test the `validUTF8` function.

## Usage

The `validUTF8` function takes a list of integers, where each integer represents one byte (1 byte = 8 bits) and returns `True` if the list represents valid UTF-8 encoding, or `False` otherwise.

### Example

To test the function, you can use the following example code:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False

## Author

Victor paul

## License

Part of ALX backend SE specialisation
