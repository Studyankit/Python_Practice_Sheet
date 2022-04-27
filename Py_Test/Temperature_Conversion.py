def fahrenheit_calculation(F):
    """
    Fahrenheit temperature calculation by user input of celsius degree
    :return: temp in celsius
    """

    temp_celsius = (F - 32) * 5 / 9
    return temp_celsius


def celsius_calculation(C):
    """
    Celsius temperature calculation by user input of Fahrenheit degree
    :return: temp in fahrenheit
    """
    temp_fahrenheit = (C * 9 / 5) + 32

    return temp_fahrenheit


# if __name__ == "__main__":
#     F = float(input("Enter a fahrenheit to find celsius"))
#     fahrenheit_calculation(F)
#     C = float(input("Enter a celsius to find celsius"))
#     celsius_calculation(C)


def test_method():
    # input1 = fahrenheit_calculation(32)
    # output1 = 80
    # assert input1 == output1

    input2 = fahrenheit_calculation(32)
    output2 = 0
    assert input2 == output2

    input3 = celsius_calculation(90)
    output3 = 45
    assert input3 == output3