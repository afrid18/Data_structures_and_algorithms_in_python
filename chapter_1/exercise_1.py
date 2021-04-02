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



# R-1.6
# In our implementation of the scale function (page25),the body of the loop executes the command data[j]   = factor. We have discussed that numeric types are immutable, and that use of the   = operator in this context causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?
#

# Solution: -> This is because the parameter to the scale function was a list type and the elements of the list are just referenced to the new elements

# R-1.7
# Had we implemented the scale function (page 25) as follows, does it work properly?
"""
def scale(data, factor):
    for val in data:
        val  * = factor
Explain why or why not.
"""

# Solution ->
# This wouldn't have worked. `val` is an alias to the actual element in `data` and assigning a new object to it will only change `val`'s value.



# R-1.8
# Demonstrate how to use Python’s list comprehension syntax to produce
# The list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].


# solution: This sequence is a pronic sequence that it is the product of two consecutive numbers

a = [x * (x + 1) for x in range(10)]
print(a)



# R-1.9
# Demonstrate how to use Python’s list comprehension syntax to produce thelist[ a , b , c ,..., z ],butwithouthavingtotypeall26such characters literally.
#

b = [chr(i) for i in range(ord('a'), ord('a') + 26)]
print(b)


# R-1.20
# Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possi- ble order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.
#

from random import randint

def myshuffle(data):
    for i in range(len(data) - 1, 0, -1):
        j = randint(0, i)
        data[i] , data[j] = data[j] , data[i]


c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myshuffle(c)
print(c)



# R-1.21
# Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).
#

try:
    data = []
    temp = input()
    while temp:
        data.append(temp)
        temp = input()
except EOFError:
    while len(data) != 0:
        print(data.pop())


# R-1.22
# Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.
#

a = [1, 3, 4, 5, 6, 8, 9]
b = [2, 5, 8, 4, 6, 0, 3]
c = []
for i in range(0, len(a)):
    c.append(a[i] * b[i])
print(c)


# R-1.23
# Give an example of a Python code fragment that attempts to write an ele- ment to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message:
# “Don’t try buffer overflow attacks in Python!”


a = []
try:
    a[10] = 200
except IndexError:
    print('Don’t try buffer overflow attacks in Python!')




# R-1.24
# Write a short Python function that counts the number of vowels in a given
# character string.


def countVowels(string):
    vowels = 0
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowels += 1
    return vowels

print(countVowels('AEIOUHHGGRRWWNNBBCCEEUUI'))


# R-1.25
# Write a short Python function that takes a strings, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike"
#

def removePunc(string):
    result = ''
    for i in string:
        if i not in [',', "'", '"', '!', '.']:
            result = result + i
    return result

print(removePunc("Let's try, Mike."))



# R-1.26
# Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
#

def arithmetic_check():
    result = []
    a = int(input("Please Enter an Integer value:"))
    b = int(input("Please Enter an Integer value:"))
    c = int(input("Please Enter an Integer value:"))
    if a + b == c:
        result.append('a + b = c')
    if a == b - c:
        result.append('a = b - c')
    if a * b == c:
        result.append('a * b == c')
    if result:
        print('\n'.join(result))
    else:
        print("NO match found")

arithmetic_check()



# R-1.27
# In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. The third of those implementa- tions, from page 41, was the most efficient, but we noted that it did not yield the factors in increasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general performance ad- vantages.
#
from typing import List

def factors(n:int) -> List[int]:
    k = 1
    while k ** 2 < n:
        if n % k == 0:
            yield k
        k += 1
    k = int(n ** (1/2))
    while k > 0:
        if n % k == 0:
            yield n // k
        k -= 1

print(list(factors(100)))



