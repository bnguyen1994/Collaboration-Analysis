import re

jsonFile = open('scen1-ref.json','r')

for line in jsonFile:
    article = re.search(r'title":"([a-zA-Z0-9]*)',line).group(1)
    idNum = re.search(r'id":"([a-zA-Z0-9]*)"',line).group(1)

    print article,idNum
