from bs4 import BeautifulSoup
import urllib.request
page=1
location=1

def function_get_notice(l, p):
    if l==1:
        sen(p) # 서울시
    if l==2:
        goe(p) # 경기도
    if l==3:
        kwe(p) # 강원도
    if l==4:
        jne(p) # 전라남도
    if l==5:
        jbe(p) # 전라북도
    if l==6:
        gne(p) # 경상남도
    if l==7:
        kbe(p) # 경상북도
    if l==8:
        jje(p) # 제주도
    if l==9:
        cne(p) # 충청남도
    if l==10:
        cbe(p) # 충청북도
    if l==11:
        pen(p) # 부산광역시
    if l==12:
        gen(p) # 광주광역시
    if l==13:
        dje(p) # 대전광역시
    if l==14:
        ice(p) # 인천광역시


def sen(page): # 서울시 교육청
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

def goe(page): # 경기도 교육청
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

def kwe(page): # 강원도 교육청
    taget_url = 'http://www.gwe.go.kr/user/boardList.do?command=list&page='+ str(page) + '&boardId=741&boardSeq=1431042'
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].find('a').text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # name
            print(tds[4].text.strip()) # date
            print(tds[5].text.strip()) # view
            for link in  tr.find_all('a'): # link
                print('http://www.gwe.go.kr/user/'+link.attrs['href'])

def jne(page): # 전라남도 교육청
    taget_url = 'http://www.jne.go.kr/board/list.jne?boardId=BBS_0000136&menuCd=DOM_000000102001000000&startPage='+str(page)
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].find('a').text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # date
            print(tds[4].text.strip()) # view
            for link in  tds[1].find_all('a'): # link
                print('http://www.jne.go.kr/'+link.attrs['href'])

def jbe(page): # 전라북도 교육청
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

def gne(page): # 경상남도 교육청
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

def kbe(page): # 경상북도 교육청
    taget_url = 'http://www.gbe.kr/main/na/ntt/selectNttList.do?mi=3439&bbsId=1876&currPage=' + str(page)
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx >= 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # date
            for link in  tds[1].find_all('a'): # link
                print('http://www.gbe.kr/main/na/ntt/selectNttInfo.do?mi=3439&bbsId=1876&nttSn='+link.attrs['data-id'])

def jje(page): # 제주도 교육청
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

def cne(page): # 충청남도 교육청
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

def cbe(page): # 충청북도 교육청
    taget_url = 'http://www.cbe.go.kr/home/sub.php?menukey=705&page=' + str(page)
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx >= 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # date
            print(tds[4].text.strip()) # view
            for link in  tds[1].find_all('a'): # link
                print('http://www.cbe.go.kr/home/' + link.attrs['href'])

def pen(page): # 부산광역시 교육청
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

def gen(page): # 광주광역시 교육청
    taget_url = 'http://www.gen.go.kr/xboard/board.php?&tbnum=20&page=' + str(page)
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx >= 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # date
            print(tds[4].text.strip()) # view
            for link in  tds[1].find_all('a'): # link
                print('http://www.gen.go.kr/xboard/' + link.attrs['href'])

def dje(page): # 대전광역시 교육청
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

def ice(page): # 인천광역시 교육청
    taget_url = 'http://www.ice.go.kr/boardCnts/list.do?searchStr=&boardID=553&m=0401&s=ice&page='+str(page)
    html = urllib.request.urlopen(taget_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    trs = table.find_all('tr')
    for idx, tr in enumerate(trs):
        if idx >= 0:
            tds = tr.find_all('td')
            print(tds[0].text.strip()) # id
            print(tds[1].text.strip()) # title
            print(tds[2].text.strip()) # dept
            print(tds[3].text.strip()) # date
            print(tds[4].text.strip()) # view
            for link in  tds[1].find_all('a'): # link
                print('http://www.ice.go.kr/boardCnts/view.do?boardID=553&boardSeq='+link.attrs['onclick'][25:32]+'&lev=0')

def use(page): # 울산광역시 교육청
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

function_get_notice(5,1)
