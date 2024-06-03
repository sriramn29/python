class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello My Name is " + self.name)

p1 = Person("Sriram", 22)
p1.myfunc()