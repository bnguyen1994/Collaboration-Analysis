import xml.etree.ElementTree as ET
import time
import multiprocessing


#represet xml data as tree
tree = ET.parse('scen1.xml')
root = tree.getroot()

'''
in: xml element 'article'
out: list of authors in article
'''
def getCollabs(article):
    authors = list()

    #find all instances of 'author' in article
    authorsInArticle = article.findall('author')

    #we only care about articles with multiple authors
    if len(authorsInArticle) > 1:

        for author in authorsInArticle:

            #add author string to list
            authors.append(author.text)

        return authors


def getEdges():
    edges = list()
    for article in root.findall('article'):
        authors = list()
        authorsInArticle = article.findall('author')

        for author in authorsInArticle:
            authors.append(author.text)

        edges.append(authors)

    return edges

'''
in:
out: edge list format of collabs
'''
def getEdgesPar():
    #create pool of n threads
    pool = multiprocessing.Pool()

    #apply getCollabs function to all articles in xml file
    collabs = pool.map(getCollabs,root.findall('article'))

    pool.close()
    pool.join()
    return collabs

#Calculate Mulithread Time
start = time.time()
getEdgesPar()
stop = time.time()
parTime = stop - start

#Calculate Serial Time
start = time.time()
getEdges()
stop = time.time()
serTime = stop - start


print "Serial time:",serTime
print "Parallel time:",parTime
speedup = serTime/parTime
print "Speedup:",speedup
