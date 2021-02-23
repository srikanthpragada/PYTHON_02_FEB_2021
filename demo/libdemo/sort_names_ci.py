# Print names in sorted order

def isname(name):
    for c in name:
        if not (c.isalpha() or c.isspace()):
            return False
    return True


def name_exists(name, names):
    name = name.upper()
    for n in names:
        if n.upper() == name:
            return True

    return False


with open("names.txt", "rt") as f:
    names = set()
    for line in f.readlines():
        parts = line.split(",")
        for v in parts:
            v = v.strip()
            if len(v) > 0 and isname(v):
                if not name_exists(v, names):
                    names.add(v)

for n in sorted(names, key=str.upper):
    print(n)
