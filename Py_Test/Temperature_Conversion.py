def fahrenheit_calculation():
    """
    Fahrenheit temperature calculation by user input of celsius degree
    :return: temp in celsius
    """
    F = float(input("Enter a fahrenheit to find celsius"))

    temp_celsius = (F - 32) * 5 / 9

    return temp_celsius


def celsius_calculation():
    """
    Celsius temperature calculation by user input of Fahrenheit degree
    :return: temp in fahrenheit
    """
    C = float(input("Enter a celsius to find celsius"))
    temp_fahrenheit = (C * 9 / 5) + 32

    return temp_fahrenheit



