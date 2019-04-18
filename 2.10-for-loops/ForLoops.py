# for loop for iterating over a data structure or over numbers

# iterate over data structure: get each item and do something with each item
list = ["apples", "bananas", "cherries"]
tup = (1, 2, 3)

for item in list:
    print(item)

for item in tup:
    print(item)

# iterate over numbers using range function 
# range function gives series of numbers from one index to another index
# range function goes to one less than the second index specified
for i in range(0, 10):
    print(i)

# range skip function
# print odd numbers by specifying increment factor
for i in range(1, 10, 2):
    print(i)

# print out first 10 multiples of 5
for i in range(5, 5 * 11, 5):
    print(i)

# nested for loop
for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)

