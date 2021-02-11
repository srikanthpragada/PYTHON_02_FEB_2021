def table(number, length=10):
    for i in range(1, length + 1):
        print(f"{number:3} * {i:2} = {number * i :5}")


table(15, 5)
table(23)
