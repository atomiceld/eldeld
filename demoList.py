# demoList

def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim","김유신"))

print("-----set 연습")
a= {1,2,3,3}
b={3,4,4,5}
lst =[1,2,3]
lst.append(4)
print(a)
print(b)

a=set((1,2,3))
print(a)
b=list(a)
print(a)
print(b)
b.append(4)
print(b)

for item in b:
    print(item)