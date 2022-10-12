#function1.py
#1) 함수를 정의
def setValue(newValue):
    x= newValue
    print("함수내부:{0}".format(x))

retValue=setValue(5)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))

