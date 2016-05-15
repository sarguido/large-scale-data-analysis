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
    parser.add_argument('--topics-file', dest='topics_filename')
    args = parser.parse_args()

    # Initialize the counters
    link_clicks = Counter()
    country_clicks = Counter()
    topic_clicks = Counter()

    # Load topic data
    topics_map = {}
    with open(args.topics_filename, 'r') as topics_file:
        for topics_line in topics_file:
            topics_data = json.loads(topics_line)
            topics_map[topics_data['g']] = topics_data['topics']

    # Read from STDIN one line at a time
    for line in sys.stdin:
        # Parse the line as JSON
        data = json.loads(line)

        # Increment the counter for the global hash
        link_clicks[data['g']] += 1

        # Increment the counter for the country
        country_clicks[data['c']] += 1

        # Increment the topics counters
        topics = topics_map.get(data['g'], [])
        for topic in topics:
            topic_clicks[topic] += 1


    # Sort and trim results
    top_links = get_top_n(link_clicks, n=20)
    top_countries = get_top_n(country_clicks, n=20)
    top_topics = get_top_n(topic_clicks, n=20)

    # Output results
    output_results('link', top_links)
    output_results('country', top_countries)
    output_results('topics', top_topics)