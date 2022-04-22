def monthly_payment():
    """
    Calculate the payment compounded annually using principal, rate and month from user

    :return: payment for a year
    """
    p = int(input("Enter the principal amount"))
    n = int(input("Enter the no of month"))
    R = int(input("Enter the rate percentage"))

    r = R / (12 * 100)

    payment = p * r / (1 - (1 + r)) ** (-n)

    return payment
