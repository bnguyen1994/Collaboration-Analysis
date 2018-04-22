#!/usr/bin/env python
import sys

authorA = 'Alice'
authorB = 'Eve'

# Read each line from stdin
for line in sys.stdin:

  # Get the words in each line
  authorAinLine = line.count(authorA)
  authorBinLine = line.count(authorB)
  exists = authorAinLine and authorBinLine

  # Generate the count for each word
  print '{0}\t{1}'.format('collab', exists)
