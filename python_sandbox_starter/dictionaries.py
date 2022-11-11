# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Similar to object literals in JavaScript

#### create
person = {
    'first_name': 'Katelyn',
    'last_name': 'Miller',
    'age': 25
}


#### create using a constructor
person2 = dict(first_name='Logan', last_name='Miller')

#### get value
print(person['first_name'])
print(person.get('last_name')) # using get method

#### add key/value
person['phone'] = '111-111-1111'

#### get dict keys
#print(person.keys())

#### get dict items
#print(person.items())

#### copy a dict
person3 = person.copy()
person3['city'] = 'New York'
#print(person3)

#### remove an item
del(person['age'])
person.pop('phone')

#### clear
person.clear()

#### get length
print(len(person3))

#### In javascript, you can have an array of objects. We can also have a list of dictionaries. 
people = [
    {'name': 'Jackie', 'age': 50},
    {'name': 'Eddy', 'age': 54}
]

print(people)