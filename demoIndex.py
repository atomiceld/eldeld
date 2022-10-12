# demoIndex.py
strA = "python is powerful"
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[-3:])
print(strA[-8:])
print(strA[:])

colors =["red","blue","green"]
print(len(colors))
print(colors[0])

colors.append("white")
print(colors)
colors.insert(1,"pink")
print(colors)
colors +=["red"]
colors +="red"
print(colors)
print(colors.count("red"))