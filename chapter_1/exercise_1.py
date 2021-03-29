# R-1.1
# Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
# is_multiple function

def is_multiple(n,m):
    if(n % m == 0):
        return True
    else:
        return False


# R-1.2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
# is_even function

def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False


# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
# minmax function

def minmax(data):
    n = 0
    len_of_data = len(data)
    smallest = data[0]
    largest = data[0]
    while(n < len_of_data):
        if(data[n] < smallest):
            smallest = data[n]
        elif ( data[n] > largest):
            largest = data[n]
        n += 1
    return smallest, largest

# R-1.4
# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
# sum_of_squares function


def sum_of_squares(n):
    total = 0
    if(n < 0):
        print("Negative number")
        return
    elif (n == 0):
        return 0
    else:
        i = 0
        while(i < n):
            total = i * i + total
            i += 1
        return total



# R-1.5
# Give a single command that computes the sum from Exercise R-1.4, rely- ing on Python’s comprehension syntax and the built-in sum function
# sum_of_squares1 function in just one line

def sum_of_squares1(n):
    return sum(i * i for i in range(n))

# R-1.6
# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
# sum_of_odd_positive_intergers

def sum_of_odd(n):
    if(n < 1):
        print("Enter number greater than 1")
        return
    else:
        i = 1
        total = 0
        while(i <= n):
            total = i * i + total
            i += 2
        return total

# R-1.7
# Give a single command that computes the sum from Exercise R-1.6, rely- ing on Python’s comprehension syntax and the built-in sum function.
# sum_of_odd1 funtion in just one line


def sum_of_odd(n):
    return sum(i * i for i in range(1, n, 2))



# R-1.8
# Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for in- dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
# negative_index_equivalent function that gives the equivalent positive index of the given negative index

def negative_index_equivalent(index, string):
    if index > 0:
        print("Non negative index is given")
    else:
        return len(string) + index


# R-1.9
# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
#

for i in range(50, 90, 10):
    print(i)


# R-1.10
# What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
#

for i in range(8, -9, -2):
    print(i)


# R-1.11
# Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
#

a = [2 ** i for i in range(9)]
print(a)



# R-1.12
#Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module in- cludes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
#


import random

# custom function to implement random.choice() function

def choice1(data):
    size = len(data)
    return data[random.randrange(size)]

a = [11,12,13,14,15,16]
print(choice1(a))


# R-1.13
# Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

# pseudo-code of a function to reverse the list


data = [13, 15, 18, 33, 67, 98, 192, 234, 500, 789, 900]

# pseudo-code as follows

# 1 -> Loop
    # 1.1 -> for ith element of the data swap ith and the size-i-1 th element
    # 1.2 -> End loop
# 2 -> Done


# Python's built in function to implement the same using a single function is
# data.reverse()
# reverse() is a function that changes the contents of the actual values in the data sequence

data.reverse()
print(data)


# R-1.14
# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
#

def odd_product(data):
    size = len(data)
    for i in range(size):
        for j in range(size):
            if(i == j):
                continue
            elif (data[i] * data[j]) % 2 == 1:
                return i , j
    print("None Found!")


oddList = [2, 3, 4, 5]
print(odd_product(oddList))                 # returns a tuple of (1,3) meaning oddList[1] multiplied by oddList[3] gives a odd number
                                            #                       3 * 5 = 15 which is an odd number







# R-1.5
# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
#

def uniqueElements(data):
    size = len(data)
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            elif(data[i] == data[j]):
                return False
    return True

uniqueEle = [1, 2, 4, 5, 6 ,7, 9]
notUniEle = [1, 3, 5, 7, 9, 1, 2, 5, 8]

print(uniqueElements(uniqueEle))
print(uniqueElements(notUniEle))
