# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#### Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')

#### creating a tuple using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#### if you only have one value, you want to leave a trailing comma otherwise, it will looks at it as a string
fruits3 = ('Apples',)
#print(fruits3, type(fruits3))

#### get a value
print(fruits[1])

#### you cannot change the value of an item in a tuple
#fruits[0] = 'Pears' #cannot do this

#### delete
del fruits2

#### get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

#### create a set
veggies = {'Broccoli', 'Carrot', 'Asparagus'}

#### Check if something is in a set
print('Broccoli' in veggies)

#### add to set
veggies.add('Squash')

#### remove from set
veggies.remove('Carrot')

#### clear set - you still have the veggies set, but nothing is in it.
veggies.clear()

#### if you want to delete the set entirely:
del veggies