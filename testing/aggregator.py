#===================================Data============================#
#open the files we calculated with hadoop
collabCount = open('collabCount','r')
citationCount= open('citationCount','r')
articleList = open('articleList','r')
authorList = open('articleAuthors','r')

#store values in dict (pythons built in hash table)
collabDict = {}
citationDict = {}
articleAuthorDict = {}
articleYearsDict = {}
articleIdList = list()

for line in collabCount:
    collabDict[line.split(',')[0]] = line.split(',')[1][:-1]

for line in citationCount:
    citationDict[line.split(',')[0]] = line.split(',')[1][:-1]

for line in articleList:
    articleYearsDict[line.split(',')[1]] = line.split(',')[2][:-1]

for line in authorList:
    articleAuthorDict[line.split(',')[0]] = line.split(',')[1][:-1]
    articleIdList.append(line.split(',')[0])

print 'collabCount = ',collabDict
print 'citationDict = ',citationDict
print 'articleYearsDict = ',articleYearsDict
print 'articleAuthorDict = ',articleAuthorDict

collabCount.close()
citationCount.close()
articleList.close()
authorList.close()

#=================================Functions========================#

def getAuthors(article):
    authors = articleAuthorDict[article].replace('"','')
    authors = authors.split(':')
    authors = ' '.join(authors)

    return authors

def getAuthorCollabs(article):
    authors = articleAuthorDict[article]
    return collabDict[authors]

def getStdDev(article):
    return

def getAvgCitesBefore(article):
    return

def getAvgCitesAfter(article):
    return


#=================================Analysis=========================#

#data will be saved to this list as an entry
collabAnalysis = list()

for article in articleIdList:
    #names of the authors
    authors = str(getAuthors(article)) + ','

    #number of collaborations between authors
    collabsBetweenAuthors = str(getAuthorCollabs(article)) + ','

    try:
        #this articles citation count
        citations = str(citationDict[article]) + ','
    except KeyError:
        citations = 0

#    print (article +','),authors,collabsBetweenAuthors,citations

    #std dev of authors citations
    stdDev = str(getStdDev(article) + ',')

    #avg citations of authors before this article
    citesBefore = str(getAvgCitesBefore(article) + ',')

    #avg citations of authors after this article
    citesAfter = str(getAvgCitesAfter(article))

    #save into string, delimited by a comma
    entry = str(authors + 
            collabsBetweenAuthors + 
            citations + 
            stdDev + 
            citesBefore + 
            citesAfter + '\n')
    collabAnalysis.append(entry)
