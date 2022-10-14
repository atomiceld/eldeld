#web1.py
#웹크롤링
from bs4 import BeautifulSoup
#페이지로딩
page=open("c:\\work\\test01.html","rt",encoding="utf-8").read()
soup = BeautifulSoup(page,"html.parser")
# print(soup.prettify())
#<p> 전부 검색
# print(soup.find_all("p"))
#첫번째<p>
# print(soup.find("p"))
#조건이 있는 경우: <p class =outer-text">
#파이썬 class키워드 충돌을 막기 위해서 class_ 로 사용함
# print(soup.find_all("p", class_="outer-text"))
#태그를 버리고 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)