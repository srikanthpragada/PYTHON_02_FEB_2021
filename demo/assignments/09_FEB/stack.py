
nums =[]

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    nums.append(num)

print("Numbers in Reverse")
while len(nums) > 0:
    print(nums.pop())

