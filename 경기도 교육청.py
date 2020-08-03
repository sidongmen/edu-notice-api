from bs4 import BeautifulSoup
import urllib.request

page=2
taget_url = 'http://www.goe.go.kr/home/bbs/noticeList.do?menuId=100000000000058&menuInit=2%2C1%2C0%2C0%2C0&pageIndex=' + str(page)
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
trs = table.find_all('tr')

for idx, tr in enumerate(trs):
    if idx > 0:
        tds = tr.find_all('td')
        print(tds[0].text.strip()) # id
        print(tds[1].text.strip()) # title
        print(tds[3].text.strip()) # dept
        print(tds[4].text.strip()) # date
        print(tds[5].text.strip()) # view
        for link in  tr.find_all('a'):
            print('http://www.goe.go.kr/home/bbs/noticeDetail.do?bbsId='+link.attrs['onclick'][45:52]+'&bbsMasterId=' + link.attrs['onclick'][21:41]) #link
