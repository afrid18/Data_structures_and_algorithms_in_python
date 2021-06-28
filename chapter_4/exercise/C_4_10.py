# Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division.

"""A recursive algorithm to compute the integral part of a logarithm of n to base 2"""


def integral_of_log(n):
    """Returns the integral part of a log with base 2"""

    if n // 2 <= 1:
        return 1
    else:
        return 1 + integral_of_log(n // 2)


print(integral_of_log(7))
