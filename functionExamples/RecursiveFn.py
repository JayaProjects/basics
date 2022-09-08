# factorial
def fact(n):
    if n == 0:
        result = 1
    else:
        result = n * fact(n - 1)
    return result


print(fact(3))


# Given number is prime or not
def prime(n):
    f = 0
    if (n in (1, 2, 3)):
        f = f + 1
        print("Given number {} is a prime number".format(n))
    else:
        for x in range(4,n):
            if n % x == 0:
                print("Given number {} is not a prime number".format(n))
                f = f+1
                break
    if f==0:
        print("Given number {} is a prime number".format(n))
prime(37)


# find finochi
