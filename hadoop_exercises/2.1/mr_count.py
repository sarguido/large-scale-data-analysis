#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol


class MRCount(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, item):
        if 'g' in item:
            yield (item['g'], 1)

    def summer(self, key, values):
        yield (key, sum(values))

    def steps(self):
        return([
            MRStep(
                mapper=self.mapper,
                combiner=self.summer,
                reducer=self.summer,
            )
        ])

if __name__ == '__main__':
    MRCount.run()