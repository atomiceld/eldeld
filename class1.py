# class1.py
class Person:
    def __init__(self):
        self.name="default name"
    def print(self):
        # self.name="default name"
        print("My name is {0}".format(self.name))

p1=Person()
p2=Person()
p1.name="전우치"
p1.print()
p2.print()

Person.title="new title"
p1.title ="p1 title"
print(p1.title)
print(p2.title)
print(Person.title)