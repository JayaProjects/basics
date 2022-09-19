# Comprehension way
l = [x * x for x in range(1, 11)]
print(l)
# with expression
l2 = [x for x in l if x % 2 == 0]
print(l2)

l3 = [x ** 2 for x in range(1, 11)
      if (x ** 2) % 2 == 0]
print(l3)

w = ['jay', 'kumar', 'kayal']
l4 = [x[0] for x in w]
print(l4)
l5 = [x for x in w if len(x) > 3]
print(l5)

k1 = [10, 20, 30, 40]
k2 = [30, 120, 130, 40]

k3 = [x for x in k1 if x not in k2]
print(k3)

w2 = "the quick brown fox jumps over the lazy dog"
w3 = w2.split(' ')
w4 = [(x.upper(), len(x)) for x in w3]
print(w4)
print(type(w4))
w5 = [[x.upper(), len(x)] for x in w3]
print(w5)
print(type(w5))

w12 = 'aabcdioO'
wo = ['a', 'e', 'i', 'o', 'u']
w6 = []
for x in w12:
    if x.lower() in wo and x not in w6:
        w6.append(x)
print(w6)
