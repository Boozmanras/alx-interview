# 0x08 Making Change

## Overview
This project implements a solution to the classic coin change problem, determining the fewest number of coins needed to meet a given total amount.

## Problem Description
The goal is to write a function `makeChange()` that calculates the minimum number of coins required to reach a specific total amount, given a list of coin denominations.

## Features
- Dynamic programming solution
- Handles various edge cases
- Supports multiple coin denominations
- Efficient algorithm with O(total * number of coins) time complexity

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style guidelines

## Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: List of available coin denominations
- `total`: Target amount to make change for

### Return Values
- Minimum number of coins needed to meet the total
- `0` if total is 0 or negative
- `-1` if the total cannot be met with given coins

## Example Usage
```python
print(makeChange([1, 2, 25], 37))  # Returns 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Returns -1
```

## Algorithm Approach
The solution uses dynamic programming to efficiently calculate the minimum number of coins:
1. Initialize a DP array to track minimum coins for each amount
2. Iterate through possible amounts
3. For each amount, try all coin denominations
4. Update minimum coins needed

## Installation
```bash
git clone https://github.com/your-username/alx-interview.git
cd alx-interview/0x08-making_change
```

## Running the Script
```bash
chmod +x 0-making_change.py
./0-main.py
```

## Author
Victor paul

## License
This project is open-source
