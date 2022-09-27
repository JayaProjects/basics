import csv

# Read csv file:

f = open("emp.csv", 'r')
r = csv.reader(f)  # Returns reader object
data = list(r)
print(type(data))
print(data)
for i in data:
    print(i)

