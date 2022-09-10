# Genarator concepts
import time

l = [x * x for x in range(10)]  # list
print(l)
print(l[1])
print(type(l))  # list

l1 = (x * x for x in range(10))  # Not tuple its Genarator
print(next(l1))
print(next(l1))
print(next(l1))
print(type(l1))  # Genarator

t1 = time.ctime()
print(t1)
'''t3 = time.clock()
t2 = time.clock()
print(t2-t3)'''


def mygen():
    yield 'a'
    yield 'b'
    yield 'c'


g = mygen()
print(next(g))
print(next(g))
# or
for x in g:
    print(x)


def countdown(num):
    print("start countdown")
    while (num > 0):
        yield num  # Creates generator.
        num = num - 1


values = countdown(5)
for x in values:
    print(x)


# TO generate fibonacchi number

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


v = fib()
for x in v:
    if x > 10:
        break
    print(x)
