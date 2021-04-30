import Progression
class ArithmeticProgression(Progression):
    """Iterator producing arithmetic Progression"""


    def __init__(self, increment = 1, start = 0):
        """Create a new arithmetic Progression"""
        super().__init__(self, start)
        self._increment = increment

    def _advance(self):

        self._current += self._increment


