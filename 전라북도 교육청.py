from bs4 import BeautifulSoup
import urllib.request
page = 1
taget_url = 'https://www.jbe.go.kr/main/board_unify.jbe?cmsid=101040100000&target=&psize=10&cc=&st=0&sk=&sunify=&method=l&idx=&page='+str(page)
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')
trs = table.find_all('tr')
for idx, tr in enumerate(trs):
    if idx > 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[3].text.strip()) # dept
        print(tds[4].text.strip()) # date
        print(tds[5].text.strip()) # view
        for link in  tds[1].find_all('a'): # link
            print(link.attrs['title']) # title
            print('https://www.jbe.go.kr/main/'+link.attrs['href'])
