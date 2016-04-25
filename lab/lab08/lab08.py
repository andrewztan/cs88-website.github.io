#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"



##############
# Generators #
##############

def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"

