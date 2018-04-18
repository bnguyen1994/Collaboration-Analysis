#!/usr/bin/env python
import sys

idSearch = 'e401'

# Read each line from stdin
for line in sys.stdin:

  # Get the words in each line
  exists = line.count(idSearch)

  # Generate the count for each word
  print '{0}\t{1}'.format(idSearch, exists)
