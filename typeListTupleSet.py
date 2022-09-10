# Examples for print,type,id

print("Hi Jayakumar")
s = "jayakumar"
print(type(s))
i = 10
print(type(1))
k = 10
print(id(s))
print(id(i))
print(id(k))

# slice operator
print(s[::])
print(s[0:3])
print(s[:6:2])
print(s[-6:-1])

# list/tuple/set/range

x = [10, 20, 30]
x.append(111)
print(type(x))
print(x[1])
for l in x:
    print(l)

y = (40, 50, 60)
print(y)
print(type(y))
print(y[1])

z = {400, 500, 600}
print(type(z))
# print(z[1]) - Not possible

ab = range(5)
for x in ab:
    print(x)
