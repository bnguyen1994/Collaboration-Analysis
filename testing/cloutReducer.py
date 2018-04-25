#!/usr/bin/env python
import sys

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    idNum, count = line.split('\t')
    count = int(count)-1
    print '{0},{1}'.format(idNum, count)
