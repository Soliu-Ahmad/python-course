import math

# String data type

# lieral assigenment
first = "Focus"
last = 'Python'

# print (type(first))

# print (type(first) == str)

# print(isinstance(first, str))

# constructor 
pizza = str ("Delicious")
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname  += "!"
print(fullname) 

# Casting a number to a string
decade = str(10)
print(type(decade))
print(decade)

statement = "i like rock music from the " + decade + "s. "
print(statement)

# Multiple lines

multiline = '''
Hey, how are you?
I am fine.
           all good?
'''

print(multiline)


# Escape special characters
sentence = "I\'m learning Python. \nIt's awesome!"
print(sentence)


# String Method
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "okay"))
print(multiline)

print(len(multiline))
multiline += ''
multiline = ''                 '' + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(15, ".") + "$1".rjust(4))
print("Muffin".ljust(15, ".") + "$2".rjust(4))
print("Cheesecake".ljust(15, ".") + "$3".rjust(4))

print("")

# String Index Value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
    

# Some methods return boolean data
print(first.startswith("F"))
print(first.endswith("S"))


# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.5
y = float(1.14)
print(type(gpa))

# Complex Value
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")