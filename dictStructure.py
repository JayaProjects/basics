# no vowels cooured in a given string
word = input("Enter input string:")
d = {}
v = ("a", "e", "i", "o", "u")
for x in word:
    if x in v:
        d[x] = d.get(x, 0) + 1
print(d)
for k, v in sorted(d.items()):  # to sort the output
    print("{} occurences {} times".format(k, v))

# output
# Enter input string:uuueeeiiaagjl
# {'u': 3, 'e': 3, 'i': 2, 'a': 2}
# a occurences 2 times
# e occurences 3 times
# i occurences 2 times
# u occurences 3 times

# 2. student details:

# My code:
d = {}
x = eval(input("Do you want to add student mark (y/n) ="))
while x == "y":
    c = (eval(input("Enter student name and mark =")))
    d.update(c)
    x = eval(input("Do you want to add next student mark (y/n) ="))
a = eval(input("Do u want check student mark(y/n):"))
while a == "y":
    s = eval(input("student name please for mark:"))
    print(s, "  mark is  ", d.get(s, "Student not in this class"))
    a = eval(input("Do u want check next student mark(y/n):"))

# use break to stop the while

while True:
    name = input("Entér Student Name to get Marks:")
    marks = d.get(name, -1)
    if marks == -1:
        print("Student Not Found")
    print("The marks of {} : {} ".format(name, marks))
    option = input("Do you want to find another student marks[Yes|No]:")
    if option == "No":
        break
print("Thanks for using our application")
