#!/usr/bin/env python
'''
Parse a Kuma papertrail log, mostly to count IP addresses to find the scrapers.

To get some log entries, use command line papertrail, like:

papertrail --min-time '2017-11-12 4:00 AM' --max-time '2017-11-12 5:00 AM'\
  -g k8s-oregon -- mdn-prod_web '-"GET /readiness"' '-"GET /healthz"'\
  '-"- - HTTP/1.0"' > trouble.log

A simplier version can be used to just count IP addresses, but I was being
bolder, so I could parse on other elements.

To do:
- Split logs by pod, so that multi-line logs (like backtraces) can be handled
  as a single event.
- Write a simplier version that just does the IP address bucketing.
'''

from __future__ import unicode_literals, print_function
from collections import Counter
import datetime
import json
import re
import pprint

from dateutil.parser import parse

line_re = re.compile(r"""(?x)^              # Be verbose
    (?P<log_month>[A-Z][a-z][a-z])\s        # Month (Jan, Feb, Mar)
    (?P<log_day>\d+)\s                      # Day (1, 2, 31)
    (?P<log_hour>\d+):                      # Hour
    (?P<log_min>\d+):                       # Minute
    (?P<log_sec>\d+)\s+                     # Second
    (?P<machine>ip-[\d-]+)\s+               # Machine (ip-172-20-59-215)
    (?P<log_path>[^ :]+):\s                 # Log path
    (?P<payload>{.*)                        # JSON payload
""")

log_re = re.compile(r"""(?x)^               # Be verbose
    (?P<ip>[^ ]+)\s                         # IP address
    (?P<dash1>[^ ]+)\s                      # First dash -
    (?P<dash2>[^ ]+)\s                      # Second dash -
    \[(?P<time>[^]]+)\]\s   # Request time [12/Nov/2017:12:59:58 -0800]
    "(?P<method>(GET|POST|HEAD|OPTIONS))\s  # Method
    (?P<path>.*)\s                          # Request path
    (?P<http>HTTP/[^"]+)"\s                 # HTTP protocol
    (?P<status_code>[^ ]+)\s                # Status code
    (?P<length>[^ ]+)\s                     # Content length
    "(?P<referrer>[^"]+)"\s                 # Referrer
    "(?P<agent>[^"]+)"                      # User Agent
    \s+                                     # End garbage
""")

months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}
today = datetime.date.today()

papertrail_ok = [
    "fluent.info: detected rotation",
    'fluent.info: following tail of',
    'fluent.warn: /var/log/containers',
]


def extract_papertrail_log(papertrail_line):
    match = line_re.match(papertrail_line)
    if not match:
        is_ok = any(ok in papertrail_line for ok in papertrail_ok)
        if is_ok:
            return {}
        else:
            raise ValueError(papertrail_line)
    items = match.groupdict()
    month = months[items['log_month']]
    day = int(items['log_day'])
    year = today.year
    hour = int(items['log_hour'])
    minute = int(items['log_min'])
    second = int(items['log_sec'])
    log_date = datetime.datetime(year, month, day, hour, minute, second)
    log = {
        'pt_ts': log_date,
        'pt_machine': items['machine'],
        'pt_path': items['log_path']
    }
    payload = json.loads(items['payload'])
    for key, value in payload.items():
        if key == 'time':
            log['time'] = parse(value)
        elif key == 'log':
            for lkey, lvalue in extract_log(value).items():
                log['log_%s' % lkey] = lvalue
        else:
            log[key] = value
    return log


def extract_log(log_line):
    match = log_re.match(log_line)
    if match:
        return match.groupdict()
    else:
        return {'raw': log_line}


test_lines = [
   ('Nov 12 15:00:00 ip-172-20-59-215'
    ' kubernetes.var.log.containers.web-2866707077-4hflx_mdn-prod_web-:'
    ' {"log":"84.211.233.100 - - [12/Nov/2017:12:59:58 -0800]'
    ' \\"GET /en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions'
    ' HTTP/1.1\\"'
    ' 200 1814'
    ' \\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/'
    'Using_CSS_transitions\\"'
    ' \\"Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36\\"\\n",'
    '"stream":"stdout","time":"2017-11-12T20:59:59.183950049Z"}'),
   ('Nov 12 15:00:14 ip-172-20-37-202'
    ' kubernetes.var.log.containers.web-2866707077-pdmtl_mdn-prod_web-:'
    ' {"log":"85.212.141.189 - - [12/Nov/2017:13:00:14 -0800]'
    ' \\"GET /en-US/docs/tag/Firefox 3.6 HTTP/1.1\\"'
    ' 200 22867'
    ' \\"https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM/'
    'Reference/Interface/nsIDOMFileError\\"'
    ' \\"Wget/1.19.1 (linux-gnu)\\"\\n",'
    '"stream":"stdout","time":"2017-11-12T21:00:14.48437681Z"}\n'),

]


def test():
    for test_line in test_lines:
        m = line_re.match(test_line)
        assert m
        print("Raw line:", test_line)
        print("Extract line:")
        pprint.pprint(m.groupdict())
        log = extract_papertrail_log(test_line)
        print("Extract log:")
        pprint.pprint(log)
        assert 'log_raw' not in log
        print()


# Log lines that aren't web requests but OK
default_ignore_strings = [
    '[ERROR] IOError: [Errno 32] Broken pipe',  # User hung up
    '[ERROR] Traceback ',  # Kuma threw up
    '[INFO] Booting worker with pid: ',  # Kuma restarted
    'newrelic.core.',  # New Relic booting up
    '[CRITICAL] WORKER TIMEOUT',  # gunicorn hung up?
    '[info]: detected rotation of ',  # fluentd fell behind
    '[info]: following tail of ',  # fluentd caught up
    '[INFO] Handling signal: term',  # kubernetes is killing gunicorn
    '[INFO] Worker exiting',  # gunicorn is exiting
    'newrelic.config INFO - ',  # newrelic is reading config
    '[INFO] Starting gunicorn ',  # gunicorn is starting
    '[INFO] Listening at: ',  # gunicorn is starting
    '[INFO] Using worker: meinheld',  # gunicorn is starting
    '[INFO] Shutting down: Master',  # gunicorn is stopping
]


def process_lines(logfile, process_func, process_context=None,
                  ignore_strings=None, fail_limit=20, report_fails=False):
    num = 0
    raws = 0
    if ignore_strings is None:
        ignore_strings = default_ignore_strings
    for line in logfile:
        num += 1
        log = extract_papertrail_log(line)
        if 'log_raw' in log:
            log_raw = log['log_raw']
            if log_raw == '\n':
                continue
            uline = line.decode('utf8')
            is_ok = any(ignore in uline for ignore in ignore_strings)
            if not is_ok:
                raws += 1
                if report_fails:
                    print("line %d: raw log on line %s" % (num, repr(line)))
                if fail_limit and raws >= fail_limit:
                    print("Aborting, too many missed logs.")
                    break
        elif log:
            process_context = process_func(log, process_context)
    return process_context, num, raws


def collect_ips(log, context=None):
    if context is None:
        context = {
            'count': 0,
            'ips': Counter()
        }
    if context.get('debug'):
        out = "%(log_ip)s: %(log_method)s %(log_path)s" % log
        print(out)
    context['count'] += 1
    context['ips'][log['log_ip']] += 1
    return context


def report_ips(result, verbose, processed_count, total_count):
    print("Top IP addresses:")
    pprint.pprint(result['ips'].most_common(10))


def create_ip_context(ip):
    """Create a context suitable for collect_requests_by_ip"""
    return {
        'ip': ip,
        'path': Counter(),
        'status_code': Counter(),
        'count': 0
    }


def collect_requests_by_ip(log, context):
    """Analyze the requests by an IP address."""
    assert 'ip' in context
    if log['log_ip'] == context['ip']:
        context['count'] += 1
        context['path'][log.get('log_path')] += 1
        context['status_code'][log.get('log_status_code')] += 1
    return context


def report_requests_by_ip(result, verbose, processed_count, total_count):
    print("%d requests by IP %s." % (result['count'], result['ip']))
    if verbose:
        for path, count in sorted(result['path'].most_common()):
            print("%d\t%s" % (count, path))
    else:
        print("Top requests:")
        for path, count in result['path'].most_common(20):
            print('%d\t%s' % (count, path))
        print("Status codes:")
        pprint.pprint(result['status_code'].most_common())


def get_parser():
    from argparse import ArgumentParser, RawDescriptionHelpFormatter

    # Construct the sample papertrail command line
    now = datetime.datetime.now()
    minutes = now.minute - (now.minute % 5)
    maxtime = datetime.datetime(now.year, now.month, now.day, now.hour, minutes)
    mintime = maxtime - datetime.timedelta(seconds = 60 * 30)
    fmt = '%Y-%m-%d %I:%M %p'
    epilog = """\
Logs are generated using the papertrail command line app:
papertrail --min-time '%(mintime)s' --max-time '%(maxtime)s'\
 -g k8s-oregon -- mdn-prod_web '-"GET /readiness"' '-"GET /healthz"'\
 '-"- - HTTP/1.0"' > %(outfile)s""" % {
         'mintime': mintime.strftime(fmt),
         'maxtime': maxtime.strftime(fmt),
         'outfile': now.date().strftime('%Y-%m-%d.log'),
    }

    # Create the command line parser
    parser = ArgumentParser(description='Process a papertrail log',
                            epilog=epilog,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('logfile', help="A papertrail log", nargs='?')
    parser.add_argument('--test', help="Run parser tests", action='store_true')
    parser.add_argument('--verbose', '-v', action='count',
                        help='Increase verbosity of report')
    parser.add_argument('-i', '--ip',
                        help="Analyze requests for IP address")
    return parser


if __name__ == '__main__':
    import codecs
    import locale
    import sys

    # Wrap sys.stdout into a StreamWriter to allow writing unicode.
    # https://stackoverflow.com/a/4546129/10612
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

    parser = get_parser()
    args = parser.parse_args()
    if args.test:
        test()
        sys.exit(0)
    elif not args.logfile:
        parser.print_help()
        print("\nerror: logfile is required.")
        sys.exit(1)

    if args.ip:
        context = create_ip_context(args.ip)
        collecter = collect_requests_by_ip
        report = report_requests_by_ip
    else:
        context = None
        collecter = collect_ips
        report = report_ips

    with open(args.logfile, 'r') as logfile:
        result, lines, unprocessed = process_lines(
            logfile, process_func=collecter, process_context=context,
            fail_limit=None)
    processed = lines - unprocessed

    print("Done, processed %d of %d lines" % (processed, lines))
    report(result, args.verbose, processed, lines)
