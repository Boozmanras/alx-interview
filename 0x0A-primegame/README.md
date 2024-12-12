# Prime Game

## Overview
The Prime Game is a Python-based implementation of a mathematical game where two players, Maria and Ben, take turns selecting prime numbers and their multiples from a set of integers. The player who cannot make a move loses the game.

This project adheres to PEP 8 coding standards and is optimized for efficient execution with large inputs.

## Features
- Determines the winner of each round based on optimal moves.
- Implements an efficient prime number calculation using the Sieve of Eratosthenes.
- Handles up to 10,000 as the maximum value for any round.
- Compliant with Python 3.4.3 and tested on Ubuntu 20.04 LTS.

## Usage
### Prototype
```python
def isWinner(x, nums):
```
- **x**: Number of rounds.
- **nums**: List of integers representing the maximum number for each round.

### Return Value
- Returns the name of the player who won the most rounds ("Maria" or "Ben").
- Returns `None` if the winner cannot be determined.

## Example
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```
Output:
```
Winner: Ben
```

## Requirements
- **Editors**: vi, vim, emacs
- **Platform**: Ubuntu 20.04 LTS
- **Python Version**: 3.4.3
- All files must:
  - Start with `#!/usr/bin/python3`
  - Be executable
  - End with a new line
- Follow PEP 8 style guide (version 1.7.x)

## Project Structure
```
0x0A-primegame/
├── 0-prime_game.py  # Implementation of the Prime Game logic
├── main_0.py         # Example main file
├── README.md         # Project documentation
```

## Implementation Details
- **Prime Number Calculation**:
  Uses the Sieve of Eratosthenes to efficiently compute prime numbers up to the largest value in the input list.

- **Performance Optimization**:
  Precomputes cumulative prime counts for faster evaluation of rounds.

## Testing
To test the implementation, run the provided `main_0.py` file or create your own test cases. Ensure the environment meets the specified requirements.

## Author
This project was created for educational purposes to demonstrate problem-solving and optimization techniques in Python by Victor paul. Feel free to contribute or suggest improvements.
