from bs4 import BeautifulSoup
import urllib.request
page = 2
taget_url = 'http://www.gne.go.kr/board/list.gne?orderBy=&boardId=gne_notice&searchStartDt=&searchEndDt=&startPage='+str(page)+'&menuCd=DOM_000000105011000000'
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')
trs = table.find_all('tr')
for idx, tr in enumerate(trs):
    if idx >= 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[2].text.strip()) # dept
        print(tds[3].text.strip()) # date
        for link in  tds[1].find_all('a'): # link
            print(link.attrs['title']) # title
            print('http://www.gne.go.kr/'+link.attrs['href'])
