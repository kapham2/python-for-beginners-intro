# functions allow you to reuse your code more efficiently

# create function
def HelloWorld():
    print("Hello World")

# call function
HelloWorld()

# create function that takes in name and prints out hi, [name]
def Greeting(name):
    print("Hi " + name + "!")

Greeting("Kim")

# create function that takes in two numbers and prints out the sum of the two numbers
def Sum(num1, num2):
    print(num1 + num2)

Sum(2, 5)

# return statement in function allows us to send back value to where the function was called
def returnSum(num1, num2):
    return num1 + num2

sum = returnSum(12, 13)

print(sum)