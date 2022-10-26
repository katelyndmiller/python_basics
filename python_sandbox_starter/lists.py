# A List is a collection which is ordered and changeable. Allows duplicate members.
# Similar to an array in javascript

######## Create List ########
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor (like using new Array() in javascript)
numbers2 = list((1, 2, 3, 4, 5))


######## Get a value from a list ########
print(fruits[1]) #prints Oranges

######## Get the length of a list ########
print(len(fruits)) # prints 4

######## Append to a list ########
fruits.append('Bananas')

######## Remove from a list ########
fruits.remove('Grapes')

######## Remove by position with pop method ########
fruits.pop(2)

######## Insert a value into a specific position ########
fruits.insert(2, 'Mangos') # pass in the position we want to insert and then the item we want to insert

######## Reverse a list ########
fruits.reverse()

######## Sort alphabetically ########
fruits.sort()

######## Reverse Sort ########
fruits.sort(reverse=True)

######## Change a value ########
fruits[0] = 'Blueberries'

print(fruits)