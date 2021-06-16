S = [1, 2, 3, 4, 5, 6, 7, 8, 1]

def unique1(S):
    """Return True if there are no duplicates else return False"""
    num = len(S)
    for i in range(num):
        for j in range(i):
            if S[j] == S[i]:
                return False
    return True


def unique2(S):
    """Return True if there are no duplicates else return False"""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if temp[j - 1] == temp[j]:
            return False
    return True

print(unique1(S))
print(unique2(S))
