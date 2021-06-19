S = [1, 2, 3, 4, 5, 6, 7, 8]

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

# From chapter 4 using recursion the following function was implemented
# This implementation is very unuseful because of it's efficiency


def unique3(S, start, stop):
    """Return True is there are no duplicate elements in slice S[start:stop]"""
    if stop - start <= 1:return True
    elif not unique3(S, start,stop-1):return False
    elif not unique3(S, start+1, stop): return False
    else: return S[start] != S[stop - 1]


print(unique1(S))
print(unique2(S))
print(unique3(S, 0, len(S)))
