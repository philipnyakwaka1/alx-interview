#!/usr/bin/python3
import sys
import signal
import re


def signal_handler(signum, frame):
    """signal handler"""
    print(f'File size: {file_size}')
    for key, value in sorted(status_dict.items()):
        print(f'{key}: {value}')


signal.signal(signal.SIGINT, signal_handler)
counter = 0
file_size = 0
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] "GET \/projects\/\d+ HTTP\/1\.1" \d{3} \d+$'
for line in sys.stdin:
    if re.match(pattern, line):
        status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
        data = line.split(' ')
        file_size += int(data[-1])
        if str(data[-2]) in status_dict.keys():
            status_dict[data[-2]] += 1
        if counter == 9:
            print(f'File size: {file_size}')
            for key, value in sorted(status_dict.items()):
                print(f'{key}: {value}')
            counter = 0
            continue
        counter += 1
