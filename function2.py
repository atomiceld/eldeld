# function2.py
def intersect(prelist,postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))
