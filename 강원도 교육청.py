import json
from bs4 import BeautifulSoup
import urllib.request
from collections import OrderedDict
page = 1
taget_url = 'http://www.gwe.go.kr/user/boardList.do?command=list&page='+ str(page) + '&boardId=741&boardSeq=1431042'
html = urllib.request.urlopen(taget_url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')
trs = table.find_all('tr')
list = []
for idx, tr in enumerate(trs):
    if idx > 0:
        tds = tr.find_all('td')
        for link in  tr.find_all('a'): # link
            notice_data = OrderedDict()
            notice_data['id'] = int(tds[0].text.strip())
            notice_data['title'] = tds[1].find('a').text.strip()
            notice_data['dept'] = tds[2].text.strip()
            notice_data['name'] = tds[3].text.strip()
            notice_data['date'] = tds[4].text.strip()
            notice_data['view'] = int(tds[5].text.strip())
            notice_data['href'] = 'http://www.gwe.go.kr/user/'+link.attrs['href']
            list.append(notice_data)
print(json.dumps(list, ensure_ascii=False, indent="\t") )
