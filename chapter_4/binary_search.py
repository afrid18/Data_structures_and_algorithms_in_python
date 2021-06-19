def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)



A = [1, 23, 5, 6, 534, 634, 2, 7, 36, 7453, 734, 72, 62, 72,74]
A = sorted(A)
print(A)

target = 5


print(binary_search(A, target, 0, len(A) - 1))


