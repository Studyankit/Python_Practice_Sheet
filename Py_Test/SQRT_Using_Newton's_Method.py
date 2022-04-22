import math


def sqrt():
    """
    Calculate square root of a no using Newtons method to desired accuracy

    :return: the value of root
    """
    c = abs(int(input("Enter a non negative integer")))
    n = float(input("Enter the desired accuracy"))

    epsilon = 1e-15

    t = c  # // estimate of the square root of c
    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    print(t)


sqrt()
