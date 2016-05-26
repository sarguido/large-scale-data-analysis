#!/usr/bin/env python

from collections import Counter
from operator import itemgetter

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol, JSONProtocol


class MRTop(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def configure_options(self):
        super(MRTop, self).configure_options()
        self.add_passthrough_option(
            '--filter-agency', help="Agency to filter results to"
            )

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
                if self.options.filter_agency != agency_data['Agency']:
                    self.increment_counter('mr_top', 'skipped_agency_ghashes', 1)
                    return
                else:
                    self.increment_counter('mr_top', 'processed_agency_ghashes', 1)

                for decode in decodes:
                    yield None, decode
                decodes = None
            else:
                if agency_data:
                    yield None, value

    def second_mapper(self, _, item):
        if 'g' in item:
            yield ('Hash', '{}|1'.format(item['g']))

        if 'c' in item:
            yield ('Country', '{}|1'.format(item['c']))

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