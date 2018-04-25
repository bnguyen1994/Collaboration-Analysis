import sys

for line in sys.stdin:
    articleName,citationNumber = line.split('\t')

    print'(0),(1)'.format(articleName,citationNumber)
