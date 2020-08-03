from bs4 import BeautifulSoup
import urllib.request
page = 1
taget_url = 'http://www.dje.go.kr/boardCnts/list.do?type=default&page=' + str(page) + '&m=030101&s=dje&menuID=030101&boardID=450'
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table',{'class':'wb'}).find('tbody')
trs = table.find_all('tr')
for idx, tr in enumerate(trs):
    if idx >= 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[1].text.strip()) # title
        print(tds[3].text.strip()) # dept
        print(tds[5].text.strip()) # date
        print(tds[4].text.strip()) # view
        for link in  tds[1].find_all('a'): # link
            print('http://www.dje.go.kr/boardCnts/view.do?boardID=450&boardSeq='+link.attrs['onclick'][25:32]+'&lev=0')



