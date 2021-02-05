# Take marks until -1 is given and display average
total = 0
count = 0
while True:
    marks = int(input("Enter marks [-1 to stop] :"))
    if marks == -1:
        break
    total += marks
    count += 1


print(f"Average = {total/count}")


