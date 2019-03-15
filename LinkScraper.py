import urllib3 #is an http client for python
from bs4 import BeautifulSoup #library for pulling data out of html files

url = 'your_link_goes_here'
url_html = urllib3.PoolManager().request('GET', url).data 
soup = BeautifulSoup(url_html,"lxml") #lxml is an html parser
for x in soup.find_all('a'):
    print(x.get('href'))

    