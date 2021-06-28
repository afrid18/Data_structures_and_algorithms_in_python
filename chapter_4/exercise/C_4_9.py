# Write a short recursive Python function that finds the minimum and
# maximum values in a sequence without using any loops.

def max_min_recursive(S):
    """A min and max calculator from a sequence, returns a tuple containing min and max respectively"""
    max = 0
    min = 0
    if len(S) == 1:
        max = min = S[0]
        return (min, max)
    else:
        (min1, max1) = max_min_recursive(S[:len(S) // 2])
        (min2, max2) = max_min_recursive(S[len(S) // 2:])
        if min1 < min2:
            min = min1
        else:
            min = min2
        if max1 < max2:
            max = max2
        else:
            max = max1
    return (min, max)



A = [1, 3, 90, 2, 1, 8, 0, 5, -12]


print(max_min_recursive(A))
