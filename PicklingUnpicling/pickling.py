import pickle


# class
class Employee:
    def __init__(self, eno, ename): # constructor
        self.eno = eno
        self.ename = ename
    def display(self):
        print(self.eno, "\t", self.ename)
# Pickling:
with open("emp.dat","wb") as f:
    e2 = Employee(100, 'jay')
    pickle.dump(e2, f) # For pickling
    print("pickling of empl object completed")

# Unpickling
with open("emp.dat", "rb") as f:
    obj = pickle.load(f) # For unpickling
    print("Employee information after unpickling")
    obj.display()


# object
e = Employee(100, 'jay')
e1 = Employee(200, 'kay')
print(e.eno, e.ename)
print(e1.eno, e1.ename)

