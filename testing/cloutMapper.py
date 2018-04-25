#!/usr/bin/env python
import sys
import re

# Read each line from stdin
for line in sys.stdin:

  ref = re.search(r'references":"([a-zA-Z0-9]*)"',line).group(1)
  idNum = re.search(r'id":"([a-zA-Z0-9]*)"',line).group(1)

  print '{0}\t{1}'.format(idNum, ref)
