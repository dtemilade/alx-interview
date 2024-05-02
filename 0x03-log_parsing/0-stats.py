#!/usr/bin/python3
'''
Script that reads stdin line by line and computes metrics.
'''
import re
import sys


def read_input(line):
    '''
    Read sections of a line of an HTTP-request log.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<var_size>\d+)'
    )
    info = {'status_code': 0, 'var_size': 0}
    line_pattern = '{}\\-{}{}{}{}\\s*'.format(*pattern)
    match = re.fullmatch(line_pattern, line)
    if match is not None:
        status_code = match.group('status_code')
        var_size = int(match.group('var_size'))
        info['status_code'] = status_code
        info['var_size'] = var_size
    return info


def print_statistics(total_var_size, status_codes_stats):
    '''
    Output the accumulated statistics.
    '''
    print('File size:', total_var_size)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{}: {}'.format(status_code, num))


def update_metrics(line, total_var_size, status_codes_stats):
    '''
    Updates the metrics from a given HTTP-request.
    Args:
        line (str): The line of input to retrieve the metrics.
    Returns:
        int: The new total file size.
    '''
    line_info = read_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_var_size + line_info['var_size']


def run():
    '''
    Running the log parser.
    '''
    line_num = 0
    total_var_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin:
            total_var_size = update_metrics(line, total_var_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_var_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_var_size, status_codes_stats)


if __name__ == '__main__':
    run()
