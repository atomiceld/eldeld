#web2.py
#웹서버에 페이지 실행 요청
from turtle import title
import urllib.request
#크롤링
from bs4 import BeautifulSoup
f= open("c:\\work\\webtoon.txt","wt", encoding="utf-8")
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="+str(i)

    data = urllib.request.urlopen(url)
    soup =BeautifulSoup(data,"html.parser")
    #검색하기
    cartoons = soup.find_all("td",class_="title")
    title = cartoons[0].find("a").text
    link=cartoons[0].find("a")["href"]
    print(title)
    print(link)

    for item in cartoons:
        title = item.find("a").text
        print(title.strip())
        f.write(title.strip()+"\n")
f.close()
