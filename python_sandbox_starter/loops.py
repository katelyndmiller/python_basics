# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['John', 'Kate', 'Mo', 'Kyle']

#### simple for loop
# for person in people:
#     print(f'current person is {person}')

#### using a break

# for person in people:
#     if person == 'Kate':
#         break
#     print(f'current person is {person}')

#### using a continue

for person in people:
    if person == 'Kate':
        continue
    print(f'current person is {person}')

#### range

for i in range(len(people)):
    print(people[i], i)
    
for i in range(0, 11): # exclusive of 11
    print(f'number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'count: {count}')
    count += 1