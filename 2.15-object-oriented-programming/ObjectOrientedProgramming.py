# classes and objects

# classes are overall type, they're a category, it's broad
# you get objects from a class which becomes an instance of the class

class Person:
    pass

p = Person()

# self tells the class which object is performing the function
class Person:
    def getName(self):
        print("Kim")

    def getAge(self):
        print("16")

p = Person() 
p.getName()
p.getAge()

# initialization function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)

p = Person("Kim", "29")
p.getName()
p.getAge()