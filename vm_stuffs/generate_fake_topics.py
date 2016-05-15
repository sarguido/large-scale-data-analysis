#!/usr/bin/env python

import ujson as json
import random
import sys


TOPICS = [
    'news',
    'sports',
    'entertainment',
    'cats',
    'dogs',
    'education',
    'hobbies',
    'movies',
    'books',
    'foo',
    'bar'
]


if __name__ == '__main__':
    processed = set()

    for decode_str in sys.stdin:
        decode = json.loads(decode_str)
        ghash = decode['g']

        if ghash in processed:
            continue

        num_topics = random.randint(0, 3)
        if num_topics > 0:
            print json.dumps({'g': ghash, 'topics': random.sample(TOPICS, num_topics)})

        processed.add(ghash)
