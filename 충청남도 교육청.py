from bs4 import BeautifulSoup
import urllib.request
page = 1
taget_url = 'http://www.cne.go.kr/boardCnts/list.do?type=default&page='+str(page)+'&m=021201&s=cne&boardID=46'
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')
trs = table.find_all('tr')
for idx, tr in enumerate(trs):
    if idx >= 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[2].text.strip()) # dept
        print(tds[4].text.strip()) # date
        print(tds[3].text.strip()) # view
        for link in  tds[1].find_all('a'): # link
            print(link.attrs['title']) # title
            print('http://www.cne.go.kr/boardCnts/view.do?boardID=46&boardSeq=' + link.attrs['onclick'][24:31] + '&lev=0')
