# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

############### Core Python Modules available by default ###############
import datetime
from datetime import date
import time 
from time import time

# today = datetime.date.today()
today = date.today()

timestamp = time()

print(timestamp)

############### PIP Modules ###############
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

############### Custom Module ###############
import validator

email = 'test@test.com'
if validator.validate_email(email):
    print(f'The email {email} is valid.')
else:
    print(f'The email {email} is NOT valid.')
