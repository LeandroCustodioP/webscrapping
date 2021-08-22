from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
        nameList = bs.findAll('span', {'class':'green'})
        for name in nameList:
            print(name.get_text())
    except AttributeError as e:
        return None
    else:    
        return title
    
title = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')
if title == None:
    print('Title could not be found')
else:
    print(title)