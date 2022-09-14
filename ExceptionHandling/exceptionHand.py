# Basic try and catch
try:
    print(10 / 0)
except:
    print(10 / 2)

try:
    print(10 / 0)
except ZeroDivisionError as x:
    print("Exception raised: =",x)
    print(10 / 2)

try:
    print(10 / "ten")
except ZeroDivisionError as x:
    print("Exception raised: =",x)
    print(10 / 2)
except TypeError as y:
    print("type error is",y)
finally:
    print("finally block execute always")

