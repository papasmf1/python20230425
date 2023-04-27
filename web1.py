# web1.py 
#크롤링을 위한 선언 
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인)
page = open("c:\\work2\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>태그 전부 검색 
#print(soup.find_all("p"))
#<p>하나만 검색 
#print(soup.find("p"))
#<p class="outer-text"> 조건이 있는 경우 
#print(soup.find_all("p", class_="outer-text"))
#print( soup.find_all("p", attrs={"class":"outer-text"}) )
#태그 내부에 컨텐츠만 사용 
for item in soup.find_all("p"):
    #태그는 버리고 컨텐츠만 사용 
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)

