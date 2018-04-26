from math import sqrt

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

#get all authors of an article
def getAuthors(article):
    #remove quotation marks
    authors = articleAuthorDict[article].replace('"','')
    #separate by colon delimite
    authors = authors.split(':')
    #join the by a space
    authors = ' '.join(authors)

    return authors

#get the number times authors of article have collabed
def getAuthorCollabs(article):
    authors = articleAuthorDict[article]
    return collabDict[authors]

def getAuthorCitationsPre(article):
    #get authors from article
    authors = articleAuthorDict[article].split(':')
    #get article date
    date = articleYearDict[article]
    #get articles for each author prior to date
    authorCitations = list()
    for author in authors:
        articlesOfAuthor = articlesByAuthor[author].split(':')
        citationSum = 0
        for entry in articlesOfAuthor:
            if articleYearsDict[entry] <= date:
                citationSum += citationDict[entry]

        authorCitations.append(citationSum)

    return authorCitations

def getAuthorCitationsPost(article):
    #get authors from article
    authors = articleAuthorDict[article].split(':')
    #get article date
    date = articleYearDict[article]
    #get articles for each author prior to date
    authorCitations = list()
    for author in authors:
        articlesOfAuthor = articlesByAuthor[author].split(':')
        citationSum = 0
        for entry in articlesOfAuthor:
            if articleYearsDict[entry] > date:
                citationSum += citationDict[entry]

        authorCitations.append(citationSum)

    return authorCitations

#get std dev of authors citations before article
def getStdDev(authorCitations):
    #calculate std dev of citations
    mean = sum(authorCitations)/len(authorCitations)
    diff = [x - mean for x in authorCitations]
    sq_dif = [d ** 2 for d in diff]

    return sqrt(sum(sq_dif)/len(authorCitations))
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


    #avg citations of authors before this article
    citesBefore = getAuthorCitationsPre(article)
    AvgCitesBefore = str(sum(citesBefore)/len(citesBefore)) + ','

    #std dev of authors citations
    stdDev = str(getStdDev(citesBefore) + ',')

    #avg citations of authors after this article
    citesAfter = getAuthorCitationsPost(article)
    AvgCitesAfter = str(sum(citesAfter)/len(citesAfter)) + ','

    #save into string, delimited by a comma
    entry = str(authors + 
            collabsBetweenAuthors + 
            citations + 
            stdDev + 
            AvgcitesBefore + 
            AvgcitesAfter + '\n')
    collabAnalysis.append(entry)
