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
    args = parser.parse_args()

    # Initialize the counters
    link_clicks = Counter()
    country_clicks = Counter()
    agency_clicks = Counter()

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

        # Increment the counter for the global hash
        link_clicks[data['g']] += 1

        # Increment the counter for the country
        if 'c' in data:
            country_clicks[data['c']] += 1

        # Increment the agencies counters
        agency = agencies_map.get(data['g'])
        if agency:
            agency_clicks[agency['Agency']] += 1
        else:
            agency_clicks['Unknown'] += 1



    # Sort and trim results
    top_links = get_top_n(link_clicks, n=20)
    top_countries = get_top_n(country_clicks, n=20)
    top_agencies = get_top_n(agency_clicks, n=20)

    # Output results
    output_results('link', top_links)
    output_results('country', top_countries)
    output_results('agency', top_agencies)