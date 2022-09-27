from zipfile import *

f = ZipFile("files.zip", 'w', ZIP_DEFLATED)
f.write("jay.txt")
f.write("kay.txt")
f.write("pre.txt")
f.close()
print("sucessfully zipped the files")

# to unzip the file:

f = ZipFile("files.zip", 'r', ZIP_STORED)
names = f.namelist()
for n in names:
    print("File name is :", n)
    print("The content of File is :")
    f1 = open(n, 'r')
    print(f1.read())
    print()
