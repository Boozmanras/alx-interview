#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print statistics for the given total file size and status codes
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to process log lines and compute metrics
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:

                parts = line.split()
                if len(parts) < 7:
                    continue

                size = parts[-1]
                if size.isdigit():
                    total_size += int(size)

                status = parts[-2]
                if status.isdigit() and int(status) in status_codes:
                    status_codes[int(status)] += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (IndexError, ValueError):
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    if line_count % 10 != 0:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
