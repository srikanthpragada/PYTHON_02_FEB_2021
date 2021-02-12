def ispositive(n: int) -> bool:
    print('Checking ',n)
    return n > 0


def hasdigit(s: str) -> bool:
    for c in s:
        if c.isdigit():
            return True

    return False


nums = [10, -20, 0, 9, -8, -6]
names = ['abc', 'xyz123', 'bc12', 'pqr']

for n in filter(ispositive, nums):
    print(n)

# for n in filter(hasdigit, names):
#     print(n)
#
# for c in filter(str.isupper , "How DO you DO?"):
#     print(c)