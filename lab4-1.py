import doctest


# Function to find the factorial
def find_fact(m: int):
    fact = 1
    for q in range(1, m + 1):
        fact = fact * q
    return fact


def solve_x_S_P(n: int, x: float) -> None:
    """
    The user enters a natural value n and a real value x. Need to display
    the value of expressions.

    :param n: int
    :param x: float

    >>> solve_x_S_P(1, 1)
    x_1 = -0.5; S_1 = -2; P_1 = 0.5

    >>> solve_x_S_P(2, 1)
    x_2 = 0.001; S_2 = 0; P_2 = 0.333

    >>> solve_x_S_P(-1, 5)
    Число n має бути натуральним
    """
    if n < 0:
        print("Число n має бути натуральним")

    else:
        # We are looking for the nth term of the sequence
        prod1 = 1
        p = 0
        while p < n:
            prod1 = prod1 * (-1) * (x ** 2)
            p += 1
        x_n = prod1 / find_fact(n ** 2 + n)

        # We are looking for the sum of the elements
        prod2 = 1
        S = 0
        for j in range(1, n + 1):
            prod2 = prod2 * (-2 * x)
            S += prod2 / find_fact(j)

        # We are looking for a product
        P = 1
        for k in range(1, n + 1):
            u = 1 + x / find_fact(k)
            P = P * u ** (-1)

        print(f"x_{n} = {round(x_n, 3)}; S_{n} = {round(S)}; P_{n} = {round(P, 3)}")


n = int(input("Input n:"))
x = float(input("Input x:"))
solve_x_S_P(n, x)
doctest.testmod()
