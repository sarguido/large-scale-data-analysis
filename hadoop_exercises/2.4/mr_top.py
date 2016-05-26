#!/usr/bin/env python

from collections import Counter
from operator import itemgetter

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol, JSONProtocol


class MRTop(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def first_mapper(self, _, item):
        if 'g' in item:
            yield (item['g'], item)
        elif 'Global Hash' in item:
            yield (item['Global Hash'], item)

    def reducer(self, key, values):
        agency_data = None
        decodes = []

        for value in values:
            if 'Global Hash' in value:
                agency_data = value
                for decode in decodes:
                    decode.update(value)
                    yield None, decode
                decodes = None
            else:
                if agency_data:
                    value.update(agency_data)
                    yield None, value
                else:
                    decodes.append(value)

    def second_mapper(self, _, item):
        if 'g' in item:
            yield ('Hash', '{}|1'.format(item['g']))

        if 'c' in item:
            yield ('Country', '{}|1'.format(item['c']))

        if 'Agency' in item:
            yield ('Agency', '{}|1'.format(item['Agency']))

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
                mapper=self.first_mapper,
                reducer=self.reducer,
            ),
            MRStep(
                mapper=self.second_mapper,
                combiner=self.summer,
                reducer=self.top_20,
            )
        ])

if __name__ == '__main__':
    MRTop.run()