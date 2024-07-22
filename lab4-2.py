import doctest

from decimal import *

getcontext().prec = 500

import math


def sin(x: float, eps: float) -> None:
    """
    Finding the value of the function sin(x).

    :param x: float
    :param eps: float

    >>> sin(30, 0.001)
    sin(30) = 0.5 with accuracy 0.001

    >>> sin(90, 0.0001)
    sin(90) = 1.0 with accuracy 0.0001

    >>> sin(36000, 0.0001)
    sin(36000) = 0.0 with accuracy 0.0001

    """
    # We convert gshradus to radians
    p = x
    while p >= 360:
        p = p - 360
    p = p * math.pi / 180

    # We look for the value of sin according to Taylor's formula
    S = p
    a = p
    n = 0
    while True:
        a = -Decimal(p ** 2) / Decimal((2 * n + 2) * (2 * n + 3)) * Decimal(a)
        S = Decimal(S) + a
        n += 1
        if abs(a) < eps:
            break
    print(f"sin({round(x)}) = {round(S, 1)} with accuracy {eps}")


x = float(input("Input x: "))
eps = float(input("Input epsilon: "))
sin(x, eps)
doctest.testmod()
