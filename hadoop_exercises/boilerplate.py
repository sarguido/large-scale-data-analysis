#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class MRCount(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, item):
        pass

    def combiner(self, key, values):
        pass

    def reducer(self, key, values):
        pass

    def steps(self):
        return([self.mr(
            mapper=self.mapper,
            combiner=self.combiner,
            reducer=self.reducer
        )])

if __name__ == '__main__':
    MRCount.run()