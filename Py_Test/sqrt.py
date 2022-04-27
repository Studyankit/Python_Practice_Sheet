def sqrt(c, n):
    """
    Calculate square root of a no using Newtons method to desired accuracy

    :return: the value of root
    """

    epsilon = 1e-15

    t = c  # // estimate of the square root of c
    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    return t


# if __name__ == "__main__":
#     c = abs(int(input("Enter a non negative integer")))
#     n = float(input("Enter the desired accuracy"))
#
#     sqrt(c, n)


def test_method():
    input1 = sqrt(9, 0.001)
    output1 = 3
    assert input1 == output1

    input2 = sqrt(8, 0.001)
    output2 = 4
    assert input2 == output2

