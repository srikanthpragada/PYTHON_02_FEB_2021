def zero(n):
    print('Before change', id(n))
    n = 0
    print('After change', id(n))


def prepend(lst,num):
    lst.insert(0,num)

a = 100
print(id(a))
zero(a)
print(a)
l = [1,2,3]
prepend(l,100)
print(l)

