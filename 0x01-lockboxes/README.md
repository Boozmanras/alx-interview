# Lockboxes

## Description
This project contains a Python function that solves the "Lockboxes" problem. Given n number of locked boxes, each containing keys to potentially open other boxes, the function determines if all boxes can be opened.

## Project Structure
```
.
├── 0-lockboxes.py
└── README.md
```

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Installation
Clone this repository to your local machine:
```
git clone https://github.com/Boozmanras/alx-interview.git
cd alx-interview/0x01-lockboxes
```

## Usage
The main function `canUnlockAll(boxes)` is located in the `0-lockboxes.py` file. You can import and use it in your Python scripts as follows:

```python
from 0-lockboxes import canUnlockAll

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Function Prototype
```python
def canUnlockAll(boxes)
```

### Parameters
- `boxes`: A list of lists where each inner list represents a box and contains keys to other boxes.

### Return Value
- `True` if all boxes can be opened
- `False` otherwise

## Testing
You can test the function using the provided `main_0.py` file:

```
./main_0.py
```

## Author
<Victor paul>

## License
This project is part of alx backend specialization; software engineering
