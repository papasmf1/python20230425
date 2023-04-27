# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#mode: append + read + write 
f = open("c:\\work2\\humor.txt", "a+", encoding="utf-8")
#페이지 주소를 1부터 10페이지까지 
for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 다시 해석 
        page = data.decode('utf-8', 'ignore')
        #2300줄 문자열 넘기는 코드 
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        #<td class="subject">
        # <a href="/board/view.php?table=bestofbest">전세사기 대안 근황</a><span class="list_memo_count_span"> [32]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td
        for item in list:
            title = item.find("a").text.strip()
            #print(title)
            if (re.search('한국', title)):
                print(title)
                f.write(title + "\n")

f.close() 


        
