import csv

# write data to csv file
with open("emp.csv", 'r+', newline='') as f:
    w = csv.writer(f)  # returns csv object
    ln = 0
    for line in f:
        ln = ln + 1
        break
    if ln == 0:
        w.writerow(["ENO", "ENAME", "ESAL"])
    else:
        n = int(input("Enter no of employee"))
        for i in range(n):
            eno = int(input("Enter eno"))
            ename = input("Enter ename")
            esal = float(input("Enter salary"))
        w.writerow([eno, ename, esal])
print("Employye details entered sucessfully")
