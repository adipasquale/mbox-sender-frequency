#!/usr/bin/env python3

import sys
req_version = (3, 0)
cur_version = sys.version_info

if cur_version < req_version:
    print("Error! you need to use this script with Python 3+")
    exit(0)

import mailbox
import argparse
from pathlib import Path
from collections import defaultdict
import re

DEFAULT_THRESHOLD = 50

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("mbox_path", help="the path of the mbox file")
    parser.add_argument("--threshold", help="number of mails to use as the threshold", default=DEFAULT_THRESHOLD, type=int)
    parser.add_argument("--group-by-email", help="mails will be grouped based on the email present in the FROM field. This can be hasardous, as formats may differ.", default=False, action="store_true")
    return parser.parse_args()

def open_mbox_file():
    my_file = Path(args.mbox_path)
    if not my_file.is_file():
        print("path '%s' is not a file" % args.mbox_path)
        exit(0)
    return mailbox.mbox(args.mbox_path)

def get_frequencies(mbox, group_by_email):
    frequencies = defaultdict(lambda: 0)
    for message in mbox:
        full_from = message.get_from()
        if group_by_email:
            matches = re.findall(r'[\w.+-]+@[\w.+-]+', full_from)
            key = matches[0] if len(matches) > 0 else "no email found"
        else:
            key = full_from
        frequencies[key] += 1
    return frequencies

def filter_frequencies(frequencies, threshold):
    return {
        key: count for key, count in frequencies.items()
        if count > threshold
    }

def sort_frequencies(frequencies):
    # this method will return a list of 2-Tuples
    return sorted(
        frequencies_filtered.items(),
        key=lambda kv: -kv[1]
    )

if __name__ == '__main__':
    args = parse_args()
    mbox = open_mbox_file()
    frequencies = get_frequencies(mbox, args.group_by_email)
    frequencies_filtered = filter_frequencies(frequencies, args.threshold)
    if len(frequencies_filtered) == 0:
        print("no matches ! no single sender sent you over %s mails" % args.threshold)
        exit(1)
    frequencies_sorted = sort_frequencies(frequencies_filtered)
    for line in frequencies_sorted:
        print("%s mails from : '%s'" % (line[1], line[0]))
