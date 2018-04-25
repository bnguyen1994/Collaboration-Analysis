#! /usr/bin/python
import sys,re

# Read each line from stdin
for article in sys.stdin:
    authors = re.search(r'authors":\[([\w|\s|^"|^,]*)\]',article).group(1)
    print '{0}\t{1}'.format(authors, 1)
