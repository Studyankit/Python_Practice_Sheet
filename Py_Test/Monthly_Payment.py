def monthly_payment(p, n, R):
    """
    Calculate the payment compounded annually using principal, rate and month from user

    :return: payment for a year
    """

    r = R / (12 * 100)

    payment = p * r / (1 - (1 + r)) ** (-n)

    return payment


# if __name__ == "__main__":
#     p = int(input("Enter the principal amount"))
#     n = int(input("Enter the no of month"))
#     R = int(input("Enter the rate percentage"))

#     monthly_payment(p, n, R)

def test_method():
    input1 = monthly_payment(100, 12, 10)
    output1 = 100
    assert input1 == output1
