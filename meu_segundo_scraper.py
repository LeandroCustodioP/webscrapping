from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.globo.com/'
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('h3',{'class':'post__title'})

for name in nameList:
    print(name.get_text())
    

