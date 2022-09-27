# File properties
f=open('jay.txt','w')
print(f.name)
print(f.mode)
print(f.closed)
print(f.readable())

# Write from string
f.write('Good Morning')
f.write(' Jay,Kayal,sri')
f.close()

# write from list
f=open('kay.txt', 'w')
l=['preethi\n', 'pranov']
f.writelines(l)
f.close()
f=open('kay.txt', 'r')
data = f.read()
print(data)
f.close()

# With Statement

with open('pre.txt','w') as f:
    f.write('pranov \n')
    f.write('sri \n')
    f.write('kayal \n')
    print("is file closed? ", f.closed)
print("is file closed? ", f.closed)

# tell() - Gives current cursor position
f=open('pre.txt','r')
print(f.tell())
print(f.read(4))
print(f.tell())
print(f.read(5))
print(f.tell())

# seek() - To move the cursor particular position
data = "All students are bad"
f=open('pr1.txt','w')
f.write(data)
with open('pr1.txt','r+') as f:
    text = f.read()
    print(text)
    print("the current cursor position : ",f.tell())
    f.seek(17)
    print("the current cursor position : ", f.tell())
    f.write("Good")
    f.seek(0)
    text=f.read()
    print("After modification")
    print(text)

# file exists or not
import os
fname = input("Enter file name :")
if os.path.isfile(fname):
    print("File exists",fname)
    f=open(fname,'r')
    text = f.read()
    print(text)
else:
    print("file not exists:",fname)



