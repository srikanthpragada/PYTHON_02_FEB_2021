def isodd(n):
    return n % 2 == 1


def isnegative(n):
    return n < 0


def factors():
    pass


def check(fun, num, type):
    if fun(num):
        print(type)
    else:
        print("Not", type)


check(isodd, 20, "Odd")
check(isnegative, -20, "Negative")
#check(factors, 20, "Factors")
