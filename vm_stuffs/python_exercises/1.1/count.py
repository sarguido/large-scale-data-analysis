#!/usr/bin/env python
from collections import Counter
import sys

import ujson as json


if __name__ == '__main__':
    # Initialize the counter
    clicks = Counter()

    # Read from STDIN one line at a time
    for line in sys.stdin:
        # Parse the line as JSON
        data = json.loads(line)

        # Increment the counter for the global hash
        clicks[data['g']] += 1

    # Output our results
    for ghash, count in clicks.iteritems():
        print('{}\t{}'.format(ghash, count))