# Island Perimeter

This project includes the implementation of a Python function `island_perimeter` that calculates the perimeter of an island represented in a rectangular grid. The grid uses `1` to represent land and `0` to represent water. This function adheres to specific coding and execution requirements outlined below.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Implementation Details](#implementation-details)
7. [Testing](#testing)
8. [Resources](#resources)

---

## Introduction

The **Island Perimeter** problem involves determining the total length of the boundary of an island within a grid. The solution assumes:
- Cells are connected only horizontally or vertically.
- The grid is surrounded by water (`0`) and contains one or no islands.
- There are no lakes (water enclosed by land).

---

## Requirements

- **Environment**:  
  All scripts are executed and tested on **Ubuntu 20.04 LTS** with **Python 3.4.3**.
  
- **Coding Standards**:
  - Adhere to [PEP 8](https://peps.python.org/pep-0008/) style guide (version 1.7).
  - Do not import external modules.
  - Include module and function-level documentation.
  
- **File Guidelines**:
  - Each file must start with the shebang `#!/usr/bin/python3`.
  - Each file must end with a new line.
  - Files must be executable.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/island-perimeter.git
   cd island-perimeter
   ```

2. Ensure Python 3.4.3 or later is installed on your system:
   ```bash
   python3 --version
   ```

3. Make the script executable:
   ```bash
   chmod +x 0-island_perimeter.py
   ```

---

## Usage

### Function Signature
```python
def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.
    """
```

### Input
- **grid**: A list of lists of integers where:
  - `0` represents water.
  - `1` represents land.
  - The grid has a width and height not exceeding 100.

### Output
- Returns an integer representing the total perimeter of the island.

---

## Example

Here's an example of how to use the function:

### Input
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### Code
```python
#!/usr/bin/python3
from 0-island_perimeter import island_perimeter

if __name__ == "__main__":
    print(island_perimeter(grid))
```

### Output
```
12
```

---

## Implementation Details

The algorithm iterates through each cell in the grid:
1. For each `1` (land cell), it assumes a default of 4 sides.
2. It subtracts one side for each neighboring land cell:
   - Above
   - Below
   - Left
   - Right
3. Accumulates the total perimeter.

---

## Testing

1. Use the provided test file `0-main.py`:
   ```bash
   ./0-main.py
   ```

2. Verify the output:
   ```
   12
   ```

3. Test additional grids by modifying the `grid` variable in `0-main.py`.

---

## Resources

- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Official Documentation](https://docs.python.org/3/)

---

## Author

This project was developed as part of a Python scripting project to strengthen algorithmic and problem-solving skills by
 **Victor paul**.
