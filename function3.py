# function3.py
from tkinter import Y


def connectURI(server,port):
    strURL="http://"+ server + ":" +port
    return strURL
print(connectURI("credu.com", "80"))
print(connectURI(port="80",server="credu.com"))

def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))
print(union("HAM","EGG","SPAM","HAPPY"))

def userURIBuilder(server,port,**user):
    strURL="http://"+server+":"+port+"/?"
    for key in user.keys():
        strURL += key +"="+user[key]+"&"
    return strURL

print(userURIBuilder("naver","80",id="kim",passwd="1234"))
print(userURIBuilder("naver","80",id="kim",passwd="1234",
    name="mike",age="30"))

g=lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda a:a*a)(3)) 
print(globals())

