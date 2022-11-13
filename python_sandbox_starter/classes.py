# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

##### Create class

class User:
    # Constructor
    def __init__(self, name, age):
        # self is like this in JS
        self.name = name
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.'

    def hasBirthday(self):
        self.age += 1

# customer class than extends user class
class Customer(User):
    def __init__(self, name, age):
        # self is like this in JS
        self.name = name
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}. My balance is {self.balance}'

# initialize user object
kate = User('Katelyn', 25)

#initialize customer object
moe = Customer('Mo Yousef', 27)
moe.set_balance(300)
print(moe.greeting())
print(moe.hasBirthday())
print(moe.greeting())


print(kate.greeting())
print(kate.hasBirthday())
print(kate.greeting())