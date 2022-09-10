# Decorator - Adding additional functionality to existing fn
def decor(func):
    def inner(name):
        if name == 'raj':
            print("Bad morning Raj")
        else:
            func(name)

    return inner


# Automattically execute decor
@decor  # linking decorator fn(calling with decor)
def wish(name):
    print("hello ", name, " good morning")


wish("jay")
wish("raj")


def wish1(name):
    print("hello ", name, " good morning")


# To call explecitly(Linikng another way)
decorfunction = decor(wish1)

wish1("raj")  # hello  raj  good morning
decorfunction("raj")  # Bad morning Raj


# Example 2:
def dec(func):
    def indev(a, b):
        if b == 0:
            print("Invalid Div number 0")
        else:
            return func(a, b)

    return indev


@dec
def div(a, b):
    return a / b


print(div(10, 2))
print(div(10, 0))


# Decorator chaining(Multiple decors)

def dec1(func):
    def inn():
        x = func()
        return x * x

    return inn


def dec2(func):
    def inn():
        x = func()
        return 2 * x

    return inn


@dec1
@dec2
def mainfn():
    return 10


print(mainfn())
