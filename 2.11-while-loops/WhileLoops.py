# while loops and control statements

# while loop is a type of loop that continues to run until condition becomes false

counter = 0

while (counter < 5) :
    print(counter)
    counter = counter + 1

# control statements used in loops

# break terminates the loop

counter = 0
while counter < 5:
    print(counter)
    if counter == 3:
        break
    counter = counter + 1

# continue is used when you don't want the rest of the code in your loop to run but you want it to continue to iterate
counter = 0
while counter < 5:
    counter = counter + 1
    if counter == 3:
        continue
    print(counter)


# pass is a filler null statement when you don't know what you're going to write but you know there needs to be code there
counter = 0
while counter < 5:
    counter = counter + 1
    if counter == 3:
        pass
    print(counter)
    