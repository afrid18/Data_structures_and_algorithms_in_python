# Assuming it is possible to sort n numbers in O(nlogn) time, show that it is 
# possible to solve the three-way set disjointness problem in O(nlogn) time.
A = [1, 2, 3, 4, 8]
B = [5, 6, 7, 8]
C = [8, 9, 0]


# set disjointness in O(nlogn)


def setDisjointness(A, B, C):

    res = A + B + C
    res = sorted(res)

    for i in range(len(res) - 2):
        if res[i] == res[i + 1] == res[i + 2]:
            return True
    return False


print(setDisjointness(A, B, C))
