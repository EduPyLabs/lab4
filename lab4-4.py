import doctest


def lenght(i: int) -> int:
    # looking for the length of the square of the number
    sq_len = 0
    square = i ** 2
    while square > 0:
        square = square // 10
        sq_len += 1
    return sq_len


def search_number(j: int) -> None:
    """
     Find the k-th digit in the sequence 149162536..., where consecutive squares of natural numbers are written.
     The value of k is entered from the keyboard.

     :param j: int

    >>> search_number(1)
    1
    >>> search_number(2)
    4
    >>> search_number(7)
    5
    >>> search_number(-2)
    Число k має бути більшим за 0
    """

    if j <= 0:
        print("Число k має бути більшим за 0")

    else:
        # find the number whose square contains the required number of the sequence
        i = 0
        sum_len = 0
        while j - sum_len > 0:
            i += 1
            sum_len += lenght(i)
        # find the right number
        digit = (i ** 2) % (10 ** (sum_len - j + 1))
        result = digit // 10 ** (sum_len - j)

        print(result)


k = int(input("Input number:"))

search_number(k)

doctest.testmod()
