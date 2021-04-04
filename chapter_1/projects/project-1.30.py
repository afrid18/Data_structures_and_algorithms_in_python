# Project 1.30
# Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.
#
num = int(input("Please Enter an integer equal to or greater than 2:\t"))

steps = 0

while num >= 2:
    steps += 1
    num = num // 2

print(steps)
