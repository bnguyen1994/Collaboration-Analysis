#Import of sys for finding
import sys

#Reach each line from stdin
for line in sys.stdin:
    
    #Get words in each line
    words = line.split()

    #Find "title" in line
    title = "title"
    for title in line:
        #print title and its count
        print '{0}\"{1}'.format(title,1)
