s = [10, 40, 20, 90, 60, 10, 30]

a = []

def prefix_averages1(s):
    """Return a list such that, for all j, A[j] equals averages of s[0] , s[1],... and so on s[j]"""
    n = len(s);
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total / (j + 1)
    return a

def prefix_averages2(s):
    """Return a list such that, for all j, A[j] equals averages of s[0], s[1],....so on s[j]"""
    n = len(s)
    A = [0] * n
    for j in range(n):
        A[j] = sum(s[0:j + 1]) / (j + 1)

    return A

def prefix_averages3(s):
    n = len(s)
    A = [0] * n
    total = 0
    for j in range(n):
        A[j] = (total + s[j] ) / (j + 1)
        total += s[j]
    return A


a = prefix_averages1(s)
b = prefix_averages2(s)
c = prefix_averages3(s)

print(a)
print(b)
print(c)
