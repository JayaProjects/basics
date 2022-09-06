# tuple data structure
t1 = (10)
print(type(t1)) # Int
t = (10,)
print(type(t)) # tuple
t2 = tuple([10,20])
print(type(t2))

t6 = (10,20,30,40)
#t6 = eval(input("input number tuple please="))
sum = 0
for x in t6:
    sum = sum + x
avg = sum/len(t6)
print(sum)
print(avg)

#set functions
s = {}  # dict by default
print(type(s))

s1= {10,20,30}
s1.add(40)
print(s1)
s1.update([70,20,'jay'])
print(s1)

