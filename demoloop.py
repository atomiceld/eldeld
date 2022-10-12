#  demoloop.py
value =5
while value > 0:
    print(value)
    value-=1
print("--------for in---------:")
d= {100:"apple",200:"kiwi"}
for q,w in d.items():
    print(q,w)

lst=[100,"apple",3.14]
for item in lst:
    print(item,type(item))

for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i,j,i*j))


lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i>5:
        break
    print("item:{0}".format(i))
    
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i%2 ==0:
        continue
    print("item:{0}".format(i))

print(list(range(10)))
print(list(range(2000,2022)))

lst =list(range(1,11))
print([i**2 for i in lst if i>5])
tp=("apple","orange","kiwi")
print([len(i) for i in tp])
