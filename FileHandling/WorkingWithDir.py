import os

print(os.getcwd()) # current working dir
os.mkdir("jt1") # to create dir

# to create multiple dir
os.makedirs("a/b/c/d")

# to remove dir
os.rmdir("jt1")

#to remove all sub dir
os.removedirs("a/b/c")

#To display all contents of dir:
os.listdir("jay")

#To display all contents of current working dir
os.listdir('.')

#To display all contents of sub dir
os.walk("",topdown=True,onerror=None,followlinks=False)
