# R-1.1
# is_multiple function

def is_multiple(n,m):
    if(n % m == 0):
        return True
    else:
        return False


# R-1.2
# is_even function

def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False


# R-1.3
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
# sum_of_squares1 function in just one line

def sum_of_squares1(n):
    return sum(i * i for i in range(n))

# R-1.6
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


