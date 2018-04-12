from mrjob.job import MRJob
import sys

class MRCloutCount(MRJob):

    def configure_options(self):
        super(MRCloutCount, self).configure_options()
        self.add_passthrough_option(
                '--article_id',type='string',default='e401')

    def mapper(self, _, line):
        yield "citations", line.count(self.options.article_id)

    def reducer(self, key, counts):
        yield key, sum(counts)

if __name__ == '__main__':
    MRCloutCount.run()
