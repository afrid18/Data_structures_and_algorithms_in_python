class Progression:
    """Iterator producing a generic Progression
    Default iterator produces the whole Numbers
    """


    def __init__(self, start = 0):
        """Initialize the current to the first value of the progression"""
        self._current = start


    def _advance(self):
        """Update self._current to new value
        This should be overridden by the subclass to customize the progression

        By convention, if current is set to None, this designates the end of the finite progression
        """

        self._current += 1

    def __next__(self):
        """Return next element, else raise StopIteration()"""

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer


    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""

        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))
