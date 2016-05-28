#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class MRCount(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    # def configure_options(self):
    #     super(MRTop, self).configure_options()
    #     self.add_passthrough_option(
    #         '--filter-agency', help="Agency to filter results to"
    #         )

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