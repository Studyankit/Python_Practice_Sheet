import math


def Quad_Equation(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    """num1 = a in x^2
    num2 = b in x
    num3 = c as constant"""
    a = 1
    b = 4
    c = 2
    quad_func = a * x * x + b * y * y + c
    delta = math.sqrt(math.pow(b, 2) - 4 * a * c)

    root1 = (-b + delta) // 2 * a
    root2 = (-b + delta) // 2 * a

    print(root1, root2)


print(Quad_Equation.__doc__)
