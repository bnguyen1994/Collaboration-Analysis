#!/usr/bin/env python
import sys

targetArticle = 'article1'
targetIdNum = ''

# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    article, idNum = line.split('\t')

    if article == targetArticle:
        targetIdNum = idNum
        print idNum
        #check to see if idNum copied over to targetIdNum
        print targetIdNum

    else:
        continue

# Output the count for the last word
if article == targetArticle:
    print '{0}\t{1}'.format(article, idNum)
