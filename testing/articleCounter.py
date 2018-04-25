from mrjob.job import MRJob
import sys

class MRArticleCount(MRJob):

    def mapper(self, _, line):
        yield "articles", line.count('</article>')

    def reducer(self, key, counts):
        yield key, sum(counts)

if __name__ == '__main__':
    MRArticleCount.run()
