class Employee:
    def __init__(self, eno, ename): # constructor
        self.eno = eno
        self.ename = ename
    def display(self):
        print(self.eno, "\t", self.ename)