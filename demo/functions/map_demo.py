def ispositive(n):
    return n > 0


nums = [1, -3, 6, -7, 9]
marks = "90,88,67,55"

for n in map(abs, nums):
    print(n)

for n in map(ispositive, nums):
    print(n)

# l = map(int, marks.split(","))
l = [int(v) for v in marks.split(",")]
print(sum(l))
