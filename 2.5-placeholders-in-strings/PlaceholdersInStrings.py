# string placeholder

name = "Kim"

# use % sign to signify that it is a placeholder and s is the placeholder string type
sent = "%s has a job!"
sent%name
sent%("Everyone")

# multiple placeholders
fact = "%s %s is the President of the United States"
fact%("Barack", "Obama")

# placeholder for different types %s = string ; %d = integer
age = "%s is %d years old"
age%("Tommy", 7)