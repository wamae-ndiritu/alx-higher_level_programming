#!/usr/bin/python3


"""
A script that reads stdin line by line and computes
metrics
"""
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0


status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0,
                      405: 0, 500: 0}

# Function to print the metrics


def print_metrics():
    """
    Prints metrics
    """
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTR + C)
    """
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL + C


signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        # Parse the input line
        parts = line.split()
        if len(parts) >= 9:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_metrics()
    sys.exit(0)
