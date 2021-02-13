c = 0


def f1():
    global c
    c = c + 1
    v = 0

    def f2():
        nonlocal v
        v = v + 1

    f2()
    f2()
    print(v)


f1()
