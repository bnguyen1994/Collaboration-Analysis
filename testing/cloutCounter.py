from mrjob.job import MRJob

ID = 'e401'

class MRCloutCount(MRJob):

    def mapper(self, _, line):
        yield "citations", line.count(ID)

    def reducer(self, key, counts):
        yield key, sum(counts)

if __name__ == '__main__':
    MRCloutCount.run()
