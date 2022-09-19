class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age= int(input("Enter age = "))
if age>60:
    raise TooOldException("Too old")
elif age<18:
    raise TooYoungException("Too young")
else:
    print("Thanks for registration")