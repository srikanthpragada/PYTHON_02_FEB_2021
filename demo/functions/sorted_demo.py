nums = [1, -3, 6, -7, 9]

for n in sorted(nums, key=abs):
    print(n)

names = ['abc', 'Xy', 'pqrs', 'y', 'cdef']
for n in sorted(names, key=str.upper):
    print(n)
