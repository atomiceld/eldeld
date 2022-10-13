# class1.py
class Person:
    num_person=0
    def __init__(self):
        self.name="default name"
        Person.num_person +=1
    def print(self):
        # self.name="default name"
        print("My name is {0}".format(self.name))

p1=Person()
p2=Person()
p3=Person()
p4=Person()

print("인스턴스 갯수:{0}".format(Person.num_person))