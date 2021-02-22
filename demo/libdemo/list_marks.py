sections = {}
with open("marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(',')
        # Ignore lines that have not enough data
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = [int(m) for m in parts[1:] if m.isdigit()]
        avg = sum(marks) / len(marks)
        sections[name] = (avg, min(marks), max(marks))

for name, (avg, least, highest) in sorted(sections.items()):
    print(f"{name:3} {avg:6.2f} {least:3} {highest:3}")
