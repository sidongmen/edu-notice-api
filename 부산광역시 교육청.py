from bs4 import BeautifulSoup
import urllib.request
page = 2
taget_url = 'https://www.pen.go.kr/board/list.pen?boardId=BBS_0000014&menuCd=DOM_000000101001000000&paging=ok&startPage=' + str(page)
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
        print(tds[4].text.strip()) # view
        for link in  tds[1].find_all('a'): # link
            print(link.attrs['title'])
            print('https://www.pen.go.kr' + link.attrs['href'])
