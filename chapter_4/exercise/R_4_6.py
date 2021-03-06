# Describe a recursive function for computing the nth Harmonic number, Hn = ∑ni=1 1/i.

""" Recursive function to compute nth Harmonic number """

def harmonic_recursive(n):
    """Return the nth recursive number"""
    if n == 1:
        return 1 / n
    else:
        return (1 / n) + harmonic_recursive(n-1)


print(harmonic_recursive(10))
