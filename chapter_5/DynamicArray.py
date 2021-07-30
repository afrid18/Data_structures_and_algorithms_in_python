import ctypes                               # A low level array implementations

class DynamicArray:
    """A Dynamic Array implementation just like a python list"""

    def __init__(self):
        """Create an empty Array"""
        self._n = 0                                     # count of actual number of elements
        self._capacity = 1                              # capacity of array
        self._A = self._make_array(self._capacity)      # low level array

    def __getitem__(self, k):
        """Return the element at index k"""
        if not 0 <= k < n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to the end of the array"""

        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()



