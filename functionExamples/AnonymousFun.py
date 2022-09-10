# Anonymous fn - lambda fn

from functools import reduce

s = lambda n: n * n
print(s(4))
k = lambda a, b: a + b
print(k(20, 40))
print("The sum {} and {} is {}".format(5, 6, k(5, 6)))
# find bigger value
d = lambda a, b: a if a > b else b
print(d(100, 200))


# 1. filter function
# function as argument
def iseven(x):
    if (x % 2 == 0):
        return True
    else:
        return False


li = [0, 10, 15, 20, 25, 30]

evlist = list(filter(iseven, li))
print(evlist)

# now using anonymous fn
ev1 = list(filter(lambda n: n % 2 == 0, li))
print(ev1)

# 2. Map function:
m1 = list(map(lambda n: n * 2, li))
print(m1)

ll1 = [1, 2, 3, 4, 500, 600]  # ' extra elements ignored'
ll2 = [10, 20, 30, 40]
ll3 = list(map(lambda x, y: x * y, ll1, ll2))  # apply map in both list
print(ll3)

# 3. Reduce fn:  (Need to import functools package)
r = [10, 20, 30, 40, 90]
r2 = reduce(lambda x, y: (x + y), r)  # find sum
print(type(r2))
print(r2)

rr2 = reduce(lambda x, y: (x + y) / len(r), r)  # find avg
print(type(rr2))
print(rr2)
