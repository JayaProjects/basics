import emp,pickle

# Unpickling
f = open("emp1.dat",'rb')
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("All employess displayed")
        break
f.close()