#!/usr/bin/env python
from collections import Counter
import sys

import ujson as json


if __name__ == '__main__':
    # Initialize the counters
    link_clicks = Counter()
    country_clicks = Counter()

    # Read from STDIN one line at a time
    for line in sys.stdin:
        # Parse the line as JSON
        data = json.loads(line)

        # Increment the counter for the global hash
        link_clicks[data['g']] += 1

        # Increment the counter for the country
        country_clicks[data['c']] += 1

    # Output our results
    for ghash, count in link_clicks.iteritems():
        print('link\t{}\t{}'.format(ghash, count))

    for country, count in country_clicks.iteritems():
        print('country\t{}\t{}'.format(country, count))