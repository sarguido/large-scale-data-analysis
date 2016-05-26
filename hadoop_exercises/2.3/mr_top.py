#!/usr/bin/env python

from collections import Counter
from operator import itemgetter

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol


class MRTop(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, item):
        if 'g' in item:
            yield ('link', '{}|1'.format(item['g']))
        if 'c' in item:
            yield ('country', '{}|1'.format(item['c']))

    def summer(self, key, values):
        counts = Counter()
        for value in values:
            subkey, count = value.split('|')
            counts[subkey] += int(count)

        for subkey, count in counts.iteritems():
            yield(key, '{}|{}'.format(subkey, count))

    def top_20(self, key, values):
        counts = Counter()
        for value in values:
            subkey, count = value.split('|')
            counts[subkey] += int(count)

        ordered = sorted(counts.iteritems(), key=itemgetter(1), reverse=True)[:20]

        for subkey, count in ordered:
            yield(key, '{}|{}'.format(subkey, count))
            

    def steps(self):
        return([
            MRStep(
                mapper=self.mapper,
                combiner=self.summer,
                reducer=self.top_20,
            )
        ])

if __name__ == '__main__':
    MRTop.run()