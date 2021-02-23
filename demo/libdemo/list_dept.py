depts = {}
with open("employees.txt", "rt") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue

        name, employee, salary = parts
        if name in depts:
            t = depts[name]  # Get dept details
            t[0].add(employee)  # add name to set
            t[1] += int(salary)  # add salary to total
        else:
            depts[name] = [{employee}, int(salary)]  # Add list with set and total

for name, (employees, total) in sorted(depts.items()):
    print(f"{name:10} {total:10} {','.join(employees)}")
