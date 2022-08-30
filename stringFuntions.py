# 1. Remove duplicates from the string
#Input = "jayakumar"
#output = "jaykumr"
s = "jayakumar"
op = ''
for x in s:
    if x not in op:
        op = op + x
print(op)

# 2. Reverse the string
#Input = "jayakumar"
#output = "ramukayaj"
op1 = ''
for x in reversed(s):
    op1 = op1 +x
print(op1)
# or
print(''.join(reversed(s)))
# or
for k in reversed(s):
    print(k, end='')
print()
#By using slice operator:
print(s[::-1])

# 3. Reverse the sentence
#Input = "jayakumar is good boy"
#output = "boy good is jayakumar"
s1 = "jayakumar is good boy"
s2 = s1.split(' ')
op2 = ''
for x in reversed(s2):
    op2 = op2 + x + " "
print(op2)
op3 = ''
# 4 .Each word level reverse
for x in s2:
    for y in reversed(x):
        op3 = op3+y
    op3 = op3 + " "
print(op3)

