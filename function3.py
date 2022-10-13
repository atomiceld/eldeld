# function3.py
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