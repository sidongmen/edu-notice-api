from bs4 import BeautifulSoup
import urllib.request
page = 1
taget_url = 'http://www.jje.go.kr/board/list.jje?boardId=BBS_0000030&listRow=10&listCel=1&menuCd=DOM_000000203001000000&startPage=' + str(page)
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')
trs = table.find_all('tr')
for idx, tr in enumerate(trs):
    if idx >= 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[1].text.strip()) # title
        print(tds[3].text.strip()) # dept
        print(tds[4].text.strip()) # date
        print(tds[5].text.strip()) # view
        for link in  tds[1].find_all('a'): # link
            print('http://www.jje.go.kr'+link.attrs['href'])
