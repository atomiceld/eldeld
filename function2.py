# function2.py
from re import X


def intersect(prelist,postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))

x=5
def func1(a):
    return a+x
print(func1(1))
def func2(a):
    x=2
    return a+x
print(func2(1))

wordlist=["J","A","M"]
def change(x):
    x[0]="H"
change(wordlist)
print("함수 호출후 :{0}".format(wordlist))


wordlist=["J","A","M"]
def change(x):
    x1=x[:]
    x1[0]="H"
    print("함수내부:{0}".format(x1))

change(wordlist)    
print("함수 호출후 :{0}".format(wordlist))

a=1.2
print(id(a))
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))