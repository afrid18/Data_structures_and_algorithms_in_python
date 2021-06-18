A = [1, 2, 3, 4, 5]
B = [6, 7, 8]
C = [9, 0]



def disjoint1(A, B, C): # O(n^3)
    """Return True is A intersection B intersection C has none elements else return False"""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C): # O(n^2)
    """Return True is A intersection B intersection C has none elements else return False"""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


print(disjoint1(A,B,C))
print(disjoint2(A,B,C))
