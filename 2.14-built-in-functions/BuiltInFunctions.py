# built-in functions

# absolute function called on any positive or negative number
abs(29)
abs(-29)

# bool function takes in any number if it is 0 then false otherwise true
bool(0)
bool(None)
bool(20)
bool(-19)

# dir function gives a list of things you can do to the data type
dir("hello")

# help function tells you what a function does
hello = "hello"
help(hello.upper)
help(hello.splitlines)

# eval takes string and runs it as python code
print1 = 'print("Hi")'
eval(print1)

# execute for multiline code 
exec(print1)

# convert from one data type to another
a = 1
str(a)
float(a)
int(a)