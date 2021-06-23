# Describe a recursive algorithm for finding the maximum element in a se- quence, S, of n elements. What is your running time and space usage?
""" A recursive algorithm for computing max element in a list """

def max_recursive(S):
    """Returns the max element in the list using recursive algorithm"""
    if len(S) == 0:
        return None
    elif len(S) == 1:
        return S[0]
    else:
        max_ele1 = max_recursive(S[:len(S) // 2])
        max_ele2 = max_recursive(S[len(S) // 2 :])
        if max_ele1 > max_ele2:
            return max_ele1
        else:
            return max_ele2

a = [1, 43, 62, 2, 990, 2, 643, 32, 88, 33]

print(max_recursive(a))

""" Running time :  O(n)
    Storage usage:  O(n)
"""

""" Correction would be appreciated : ) """
"""             THANKS !!!              """
