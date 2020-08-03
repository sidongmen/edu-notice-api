from bs4 import BeautifulSoup
import urllib.request

page=1

taget_url = 'http://m.use.go.kr/board/board.do?actMode=list&cPage='+str(page)+'&sec=&gubun=alrNotice&sKeyKind=&sKey=&sKeyword='
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div',{'class':'listUL'})
trs = table.find_all('li')

for idx, tr in enumerate(trs):
    if idx >= 0:
        tds = tr.find_all('p')
        print(tds[0].text.strip()) # title
        print(tds[1].text.strip()) # date
        for link in  tr.find_all('a'):
            print (link.attrs['href']) # link

