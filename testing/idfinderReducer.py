#!/usr/bin/env python
import sys

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    article, idNum = line.split('\t')

    print '{0},{1}'.format(article, idNum[:-1])

