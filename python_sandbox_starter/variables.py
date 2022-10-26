# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can NOT start with one
"""

x = 1           # int
x = 2.5         # float
name = 'John'   # string
is_cool = True  # bool (make sure to capitalize the T for true or F for false)

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# print(x, y, name, is_cool)

# Basic Math
a = x + y
# print(a) # 3.5

# Check type of
print(type(x)) # prints int

# Casting
x = str(x) # turns x (an int) into a string data type
y = int(y) # turns 2.5 (a float) into an int, making it = to 2. If we change it back to a float, it will then be 2.0
print(type(y), y) 
