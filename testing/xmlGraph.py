import xml.etree.ElementTree as ET
import time
from multiprocessing import Pool as ThreadPool

tree = ET.parse('scen1.xml')
root = tree.getroot()

def getCollabs(article):
    authors = list()
    authorsInArticle = article.findall('author')

    if len(authorsInArticle) > 1:
        for author in authorsInArticle:
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

def getEdgesPar():
    pool = ThreadPool(5)
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
