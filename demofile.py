#demofile.py
url = "http://www.naver.com/?page=" +str(1)
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1500000))

f=open("c:\\work\\demo.txt","wt",encoding="utf-8")
f.write("하나\n둘\n셋\n")
f.close()
#파일읽기
f=open("c:\\work\\demo.txt","rt",encoding="utf-8")
print(f.read())

print(f.tell())
#다시 처음 보기
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
print(f.tell())
#다시 처음 보기
f.seek(0)
print(f.readlines(), end="")
f.close()