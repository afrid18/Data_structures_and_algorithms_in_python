num = int(input("Please Enter an integer equal to or greater than 2:\t"))

steps = 0

while num >= 2:
    steps += 1
    num = num // 2

print(steps)
