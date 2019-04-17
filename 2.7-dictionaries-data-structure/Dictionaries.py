# dictionaries key:value

students = {"bob":12, "rachel":13, "emily":15}

# accessing value
students["rachel"]

# updating value
students["rachel"] = 14

# delete from dictionaries
del students["emily"]

# length of dictionaries
len(students)

# dictionaries should not have multiple keys that correspond to different values
wrong = {"tommy":6, "tommy":7, "samba":8}
wrong["tommy"]