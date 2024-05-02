#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics
'''
import re


def reads_inputs(lines):
    '''read sections of a line of an HTTP-request log.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<var_size>\d+)'
    )
    info = {
        'status_code': 0,
        'var_size': 0,
    }
    val_log = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    retval = re.fullmatch(val_log, lines)
    if retval is not None:
        status_code = retval.group('status_code')
        var_size = int(retval.group('var_size'))
        info['status_code'] = status_code
        info['var_size'] = var_size
    return info


def stat_retval(total_var_size, status_codes_stats):
    '''Output the accumulated statistics.
    '''
    print('File size: {:d}'.format(total_var_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_var_size, status_codes_stats):
    '''Updates the metrics from a given HTTP-request.
    Args:
        line (str): The line of input to retrieve the metrics.
    Returns:
        int: The new total file size.
    '''
    line_info = reads_inputs(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_var_size + line_info['var_size']


def run():
    '''Running the log parser.
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
        while True:
            line = input()
            total_var_size = update_metrics(
                line,
                total_var_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                stat_retval(total_var_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        stat_retval(total_var_size, status_codes_stats)


if __name__ == '__main__':
    run()
