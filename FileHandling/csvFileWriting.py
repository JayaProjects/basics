import csv

# write data to csv file
with open("emp.csv", 'w', newline='') as f:
    w = csv.writer(f)  # returns csv object
    w.writerow(["ENO", "ENAME", "ESAL"])
    n = int(input("Enter no of employee"))
    for i in range(n):
        eno = int(input("Enter eno"))
        ename = input("Enter ename")
        esal = float(input("Enter salary"))
        w.writerow([eno, ename, esal])
print("Employye details entered sucessfully")