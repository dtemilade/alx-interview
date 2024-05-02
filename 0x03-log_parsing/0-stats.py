#!/usr/bin/python3
'''Script that reads stdin line by line and computes metrics.
'''

import re

def read_input_line(line):
    '''Reads and extracts information from a line of an HTTP-request log.
    Args:
        line (str): The line of input to extract information from.
    Returns:
        dict: A dictionary containing the extracted information.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {'status_code': 0, 'file_size': 0}
    line_pattern = '{}\-{}{}{}{}\\s*'.format(pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    match = re.fullmatch(line_pattern, line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info

def print_statistics(total_file_size, status_code_stats):
    '''Prints accumulated statistics.
    Args:
        total_file_size (int): The total size of all files.
        status_code_stats (dict): A dictionary containing status code statistics.
    '''
    print('Total file size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_stats.keys()):
        count = status_code_stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)

def update_statistics(line, total_file_size, status_code_stats):
    '''Updates statistics based on a given line of HTTP-request log.
    Args:
        line (str): The line of input to update statistics from.
        total_file_size (int): The current total file size.
        status_code_stats (dict): A dictionary containing status code statistics.
    Returns:
        int: The new total file size.
    '''
    line_info = read_input_line(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_code_stats:
        status_code_stats[status_code] += 1
    return total_file_size + line_info['file_size']

def run():
    '''Executes the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_code_stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    try:
        while True:
            line = input()
            total_file_size = update_statistics(
                line, total_file_size, status_code_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_code_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_code_stats)

if __name__ == '__main__':
    run()
