class Parent:
    def __init__(self):
        print("This is the parent class")

    def parentFunc(self):
        print("This is the parent function")

    def test(self):
        print("Parent")

p = Parent()
p.parentFunc()

# create child class that inherits a parent class

class Child(Parent):
    def __init__(self):
        print("This is the child class")
    
    def childFunc(self):
        print("This is the child function")

    # overriding methods
    # reinitializing function in child class will replace the function in parent class
    def test(self):
        print("Child")

c = Child()
c.childFunc()
c.parentFunc()

c.test()