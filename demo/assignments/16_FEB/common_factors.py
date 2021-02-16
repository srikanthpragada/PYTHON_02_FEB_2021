import sys

numbers = [int(n) for n in sys.argv[1:]]
smallest = min(numbers)

for i in range(2, smallest // 2 + 1):
    for n in numbers:
        if not n % i == 0:
            break
    else:
        print(i)
