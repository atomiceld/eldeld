#web1.py
#웹크롤링
from bs4 import BeautifulSoup
#페이지로딩
page=open("c:\\work\\test01.html","rt",encoding="utf-8").read()
soup = BeautifulSoup(page,"html.parser")
print(soup.prettify())
