# lists are comma separated value that allows us to access any item based on the index

list = ["apples", "oranges", "bananas", "cheese"]

# first item
list[0]

# third item
list[2]

# splice array (does not count end )
list[0:2]

# add items to list
list.append("blueberries")

# change first item of list
list[0] = "cherries"

# delete items in list at index
del list[1]

# count number of items in list
len(list)

list2 = ["Bread", "Jam", "Peanut butter"]

# add lists together
list + list2

# repeat list
list * 2

# max/min
listNum = [1, 4, 5, 7, 23, 6]
max(listNum)
min(listNum)