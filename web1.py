# web1.py 
#크롤링을 위한 선언 
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인)
page = open("c:\\work2\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

