

def printname(name):
    print(name)


printname("jay")

a = 10

def sq(x):
    print("square of {} is {}".format(x, x * x))


sq(5)


def add(a, b):
    return (a + b)


print(add(110, 20))


# given number odd or even
def checknum(x):
    if (x % 2 == 0):
        print("given number {} is Even".format(x))
    else:
        print("given number {} is odd".format(x))


checknum(10.6)


# Write a function to find factorial
# Using for loop
def fact(n):
    sum = 1
    for i in range(n):
        sum = sum * (i + 1)
    print(sum)


fact(5)


# Using while loop
def fact1(n):
    sum = 1
    while n >= 1:
        sum = sum * n
        n = n - 1
    return sum


for i in range(1, 6):
    print("The factorial of {} is {}".format(i, fact1(i)))


# python fn can return more than one value.
def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return (sum, sub)


x, y = sum_sub(100, 50)
print(x)
print(y)
t = sum_sub(50, 20)  # tuple packing
for x in t:
    print(x)


# variable arg method

def sum(*n):
    res = 0
    for x in n:
        res = res + x
    print(res)


sum(10, 20)
sum(10, 20, 30)
sum(10, 20, 30, 40)


# keyword variable arguments

def dis(**n):
    for k, v in n.items():
        print(k, ".....", v)


dis(a="jay", b="kay")
dis(c="jaykum", d="vivzhi")
dis(c=10, d=20, e=230)

print(dir())