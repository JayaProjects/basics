import time
import math as m
from random import *

# To print the members available in time module
for x in dir(time):
    print(x)

print(time.__loader__)
print(time.__name__)
print(time.__package__)

for x in dir(random):
    print(x)

print(m.sqrt(4))
print(m.ceil(4.5))
print(m.floor(4.5))
print(m.fabs(4.5))
print(help(m))

# To generate random numbers like OTP
for i in range(10):
    print(random())

# To send OTP
# Here is a bug. first digit never going to zero
for i in range(10):
    print(randint(100000, 999999))

for i in range(10):
    print(uniform(1, 10))
for i in range(10):
    print(randrange(1, 10, 2))

l = [10, 20, 30, 40, 50]
for i in range(10):  # From above list, selecting random numbers
    print(choice(l))

print(randint(100000, 999999))

# To get OTP
for i in range(10):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), '')

# To genrate random password as 1,3,5 are alpha and 2,4,6 are number:
num = range(0, 9)
alpha = range(65, 90)
alph = ['a', 'b', 'c', 'd']
print(choice(num), chr(choice(alpha)), choice(num), chr(choice(alpha)), choice(num), chr(choice(alpha)), '')

# Or

print(chr(randint(65, 65 + 25)), randint(0, 9), chr(randint(65, 65 + 25)), randint(0, 9), chr(randint(65, 65 + 25)),
      randint(0, 9), '')
