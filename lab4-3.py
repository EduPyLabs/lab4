import doctest


def sum_digits(i: int, e: int) -> int:
    # Find the sum of the digits of a number, where each digit is raised to the power of e
    sum_of_digits = 0
    while i > 0:
        digit = i % 10
        i = i // 10
        sum_of_digits += digit ** e
    return sum_of_digits


def search_armstrong(n: int) -> None:
    """
    A natural number with n digits is an Armstrong number if the sum of its digits raised to the power of n is equal to
    the number itself. Create a program to find all N-digit Armstrong numbers.
    The number N is entered by the user from the keyboard.

    :param n: int

    >>> search_armstrong(1)
    1, 2, 3, 4, 5, 6, 7, 8, 9

    >>> search_armstrong(2)
    Числа відсутні

    >>> search_armstrong(3)
    153, 370, 371, 407

    >>> search_armstrong(-1)
    Число N має бути більшим за 0
    """
    if n < 0:
        print("Число N має бути більшим за 0")
    else:
        counter = 0
        # Check whether the number is an Armstrong number
        for i in range(10 ** (n - 1), 10 ** n):
            number = sum_digits(i, n)
            if number == i:
                if counter != 0:
                    print(", ", end="")
                counter += 1
                print(f"{number}", end="")
        if counter == 0:
            print("Числа відсутні")


k = int(input("Input n:"))

search_armstrong(k)

doctest.testmod()
