# project 1.31

# Write a Python program that can “make change.” Your program should take two numbers as input, one that is a monetary amount charged
#and the other that is a monetary amount given. It should then return the number of each kind of
#bill and coin to give back as change for the difference between the amount given and the amount charged.
#The values assigned to the bills and coins can be based on the monetary system of any current or former
#government. Try to design your program so that it returns as few bills and coins as possible.

# Monetary system being used is of Indian Government

# currencies used in the current context are as follows
# BRUTEFORCE IMPLEMENTATION
# Any efficient code is welcomed....

# 1 rupee coin -> rupee_1
# 2 rupee coin -> rupee_2
# 5 rupee coin -> rupee_5
# 10 rupee coin or Note -> rupee_10
# 20 Rupee note -> rupee_20
# 50 Rupee note -> rupee_50
# 100 Rupee note -> rupee_100
# 200 rupee note -> rupee_200
# 500 rupee note -> rupee_500
# 2000 rupee note -> rupee_2000

rupee_1 = 1

rupee_2 = 2

rupee_5 = 5

rupee_10 = 10

rupee_20 = 20

rupee_50 = 50

rupee_100 = 100

rupee_200 = 200

rupee_500 = 500

rupee_2000 = 2000


amount_charged = float(input("Enter the amount charged: "))

amount_given = float(input("Enter the amount given: "))

if amount_charged >= amount_given:
    print(f"{amount_charged - amount_given} more has to be paid")

if amount_charged == amount_given:
    print("Correct Amount has be paid")

extra_amount = amount_given - amount_charged

if extra_amount >= rupee_2000:
    print(f"{extra_amount // rupee_2000} X 2000")
    extra_amount %= rupee_2000

if extra_amount >= rupee_500:
    print(f"{extra_amount // rupee_500} X 500")
    extra_amount %= rupee_500

if extra_amount >= rupee_200:
    print(f"{extra_amount // rupee_200} X 200")
    extra_amount %= rupee_200

if extra_amount >= rupee_100:
    print(f"{extra_amount // rupee_100} X 100")
    extra_amount %= rupee_100

if extra_amount >= rupee_50:
    print(f"{extra_amount // rupee_50} X 50")
    extra_amount %= rupee_50


if extra_amount >= rupee_20:
    print(f"{extra_amount // rupee_20} X 20")
    extra_amount %= rupee_20

if extra_amount >= rupee_10:
    print(f"{extra_amount // rupee_10} X 10")
    extra_amount %= rupee_10

if extra_amount >= rupee_5:
    print(f"{extra_amount // rupee_5} X 5")
    extra_amount %= rupee_5


if extra_amount >= rupee_2:
    print(f"{extra_amount // rupee_2} X 2")
    extra_amount %= rupee_2


if extra_amount >= rupee_1:
    print(f"{extra_amount // rupee_1} X 1")
    extra_amount %= rupee_1
