import sys

articleTitle = ''
citationNumber = 0

# Read from line from stdin
for line in sys.stdin:

    # Grab article title
    articleTitle = re.search(r'title":"([a-zA-Z0-9]*)',line).group(1)

    # Print as (Article Name,citation number)
    print '(0)\t(1)'.format(articleTitle,citationNumber)
