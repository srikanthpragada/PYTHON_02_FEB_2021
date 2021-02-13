def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


names = ["AbC", "abc", "ABC", "Abc"]
for s in filter(lambda st: count_upper(st) >= 2, names):
    print(s)
