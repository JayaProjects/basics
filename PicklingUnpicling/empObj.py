import emp,pickle

# Pickling of multiple employees
f = open("emp1.dat",'wb')
n=int(input("Enter no of employee"))
for i in range(n):
    eno=int(input("Enter emp no"))
    ename=input("Enter ename")
    e=emp.Employee(eno,ename)
    pickle.dump(e,f)

