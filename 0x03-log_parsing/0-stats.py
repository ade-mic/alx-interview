#!/usr/bin/python3
'''
Log Parsing” the knowledge of Python programming is applied,
focusing on parsing and processing data streams in real-time.
This project involves reading from standard input (stdin),
handling data in a specific format, 
and performing calculations based on the input data.
'''
import sys

def parse_line(line):
    '''Line by line parse'''
    try:
        _, _, request, status_code, file_size = line.split('"')
        status_code = int(status_code.split()[0])
        file_size = int(file_size.split()[1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None

def main():
    ''' Main Program'''
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f"Total file size: {total_size}")
                    for code, count in sorted(status_counts.items()):
                        if count > 0:
                            print(f"{code}: {count}")

    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for code, count in sorted(status_counts.items()):
            if count > 0:
                print(f"{code}: {count}")

if __name__ == "__main__":
    main()
