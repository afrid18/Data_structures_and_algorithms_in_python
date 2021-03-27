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
