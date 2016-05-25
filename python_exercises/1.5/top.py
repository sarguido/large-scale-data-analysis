#!/usr/bin/env python
import argparse
from collections import Counter
from operator import itemgetter
import sys

import ujson as json


def get_top_n(counter, n):
    ordered = sorted(counter.iteritems(), key=itemgetter(1), reverse=True)[:n]

    return ordered

def output_results(kind, results):
    for key, count in results:
        print('{}\t{}\t{}'.format(kind, key, count))



if __name__ == '__main__':
    # Setup the arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--agencies-file', dest='agencies_filename')
    parser.add_argument('--filter-agency', dest='filter_agency')
    args = parser.parse_args()

    filter_agency = args.filter_agency

    # Initialize the counters
    link_clicks = Counter()
    country_clicks = Counter()

    # Load agency data
    agencies_map = {}
    with open(args.agencies_filename, 'r') as agencies_file:
        for agencies_line in agencies_file:
            agencies_data = json.loads(agencies_line)
            agencies_map[agencies_data['Global Hash']] = agencies_data

    # Read from STDIN one line at a time
    for line in sys.stdin:
        # Parse the line as JSON
        data = json.loads(line)

        # Decide if this click has a relevant agency
        agency_data = agencies_map.get(data['g'])
        if agency_data is not None:
            if filter_agency != agency_data['Agency']:
                continue

        # Increment the counter for the global hash
        link_clicks[data['g']] += 1

        # Increment the counter for the country
        if 'c' in data:
            country_clicks[data['c']] += 1



    # Sort and trim results
    top_links = get_top_n(link_clicks, n=20)
    top_countries = get_top_n(country_clicks, n=20)

    # Output results
    output_results('link', top_links)
    output_results('country', top_countries)
