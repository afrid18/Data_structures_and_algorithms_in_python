# Describe a recursive function for converting a string of digits into the integer it represents. For example,   13531   represents the integer 13,531.
"""A recusive function to convert a string to an int"""


def recur_str_to_int(string):
    """Recursively convert a string into an ineger"""

    if len(string) == 1:
        return ord(string[0]) - ord('0')
    
    else:
        return (10 * len(string)) * (ord(string[0]) - ord('0')) + recur_str_to_int(string[1:])


print(recur_str_to_int('4123'))
