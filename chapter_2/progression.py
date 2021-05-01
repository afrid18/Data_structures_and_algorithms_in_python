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



class ArithmeticProgression(Progression):
    """Iterator producing arithmetic Progression"""


    def __init__(self, increment = 1, start = 0):
        """Create a new arithmetic Progression"""
        super().__init__(start)
        self._increment = increment

    def _advance(self):

        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""

    def __init__(self, base = 2, start = 1):


        super().__init__(start)
        self._base = base


    def _advance(self):

        self._current *= self._base



class FibonacciProgression(Progression):

    def __init__(self, first = 0, second = 1):

        super().__init__(first)
        self._prev = second - first


    def _advance(self):

        self._prev , self._current = self._current , self._prev + self._current



if __name__ == '__main__':
    Progression().print_progression(10)

    ArithmeticProgression(5).print_progression(10)
    ArithmeticProgression(5, 2).print_progression(10)
    GeometricProgression().print_progression(10)
    GeometricProgression(3).print_progression(10)
    FibonacciProgression().print_progression(10)
    FibonacciProgression(4, 6).print_progression(10)