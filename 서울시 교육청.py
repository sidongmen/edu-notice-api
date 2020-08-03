from bs4 import BeautifulSoup
import urllib.request

page=2
page_nav=10*(page-1) + 1;
taget_url = 'http://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=72&searchBean.searchKey=&appYn=&searchBean.searchVal=&searchBean.startDt=&startDt=&searchBean.endDt=&endDt=&ctgCd=&sex=&school=&grade=&year=&month=&schoolDiv=&establDiv=&hopearea=&searchBean.deptCd=&searchBean.currentPage=' + str(page_nav)
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
            print (link.attrs['href']) # link
