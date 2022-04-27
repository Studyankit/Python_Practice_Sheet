def day_of_week(month, day, year):
    """
    Cal the day of the week in Gregorian calendar using the formula
    :return: day of the week
    """

    y = (year - (14 - month) / 12)
    x = y + (y / 4) - (y / 100) + (y / 400)
    m = month + 12 * (14 - month / 12) - 2

    d = (day + x + (31 * m / 12)) % 7

    day_week = int(d)+1

    if day_week == 0:
        print("Sunday")

    elif day_week == 1:
        print("Monday")

    elif day_week == 2:
        print("Tuesday")

    elif day_week == 3:
        print("Wednesday")

    elif day_week == 4:
        print("Thrusday")

    elif day_week == 5:
        print("Friday")

    else:
        print("Saturday")

    return day_week


# if __name__ == "__main__":
#     month = int(input("Enter the month"))
#     day = int(input("Enter the day"))
#     year = int(input("Enter the year"))
#
#     day_of_week(month, day, year)


def test_method():
    input1 = day_of_week(9, 4, 2022)
    output1 = 4
    assert input1 == output1

    input2 = day_of_week(3, 10, 2022)
    output2 = 4
    assert input2 == output2
