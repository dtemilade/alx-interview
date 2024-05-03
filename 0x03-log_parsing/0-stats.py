#!/usr/bin/python3
'''Script that reads stdin line by line and computes metrics.
'''
import re

def parse_input(line):
    '''Parse each line of input in the correct format.
    Returns a dictionary containing relevant information.
    '''
    pattern = r'^(\S+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        ip_address = match.group(1)
        status_code = match.group(3)
        file_size = int(match.group(4))
        return {'ip_address': ip_address, 'status_code': status_code, 'file_size': file_size}
    else:
        return None

def print_statistics(total_file_size, status_code_counts):
    '''Print statistics based on the accumulated data.
    '''
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_counts.keys()):
        if code.isdigit() and int(code) in {200, 301, 400, 401, 403, 404, 405, 500}:
            print(f'{code}: {status_code_counts[code]}')

def run():
    '''Read input line by line and compute metrics.
    '''
    total_file_size = 0
    status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        while True:
            line = input()
            parsed_data = parse_input(line)
            if parsed_data:
                total_file_size += parsed_data['file_size']
                status_code = parsed_data['status_code']
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_code_counts)

if __name__ == '__main__':
    run()
