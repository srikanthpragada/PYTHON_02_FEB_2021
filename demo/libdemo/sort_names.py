# Print names in sorted order

def isname(name):
    for c in name:
        if not (c.isalpha() or c.isspace()):
            return False
    return True


with open("names.txt", "rt") as f:
    names = set()
    for line in f.readlines():
        parts = line.split(",")
        for v in parts:
            v = v.strip()
            if len(v) > 0 and isname(v):
                names.add(v)

for n in sorted(names):
    print(n)
