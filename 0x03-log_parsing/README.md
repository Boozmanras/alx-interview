# Log Parsing Project

## Description
This project contains a Python script that reads stdin line by line and computes metrics from log data. The script processes log entries in a specific format and provides statistical information about file sizes and HTTP status codes.

## Features
- Reads log data from standard input
- Processes logs in the format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- Computes and displays:
  - Total file size
  - Count of different HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)
- Updates statistics every 10 lines
- Handles keyboard interruption (CTRL + C) gracefully

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Usage
```bash
./0-generator.py | ./0-stats.py
```

## Input Format
Each line of input should match the following format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
Lines that don't match this format are skipped.

## Output Format
The script outputs statistics in the following format:
```
File size: <total size>
<status code>: <number>
<status code>: <number>
...
```
- Status codes are printed in ascending order
- Only status codes that appear in the input are displayed

## Files
- `0-stats.py`: Main script that processes the log data
- `0-generator.py`: Helper script to generate sample log data (provided in the project description)

## Author
Victor paul

## License
This project is part of a short Alx backend software engineering specialisation
