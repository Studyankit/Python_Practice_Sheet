def day_of_week():
    """
    Cal the day of the week in Gregorian calendar using the formula
    :return: day of the week
    """
    month = int(input("Enter the month"))
    day = int(input("Enter the day"))
    year = int(input("Enter the year"))

    y = int(year - (14 - month) / 12)
    x = y + (y / 4) - (y / 100) + (y / 400)
    m = month + 12 * (14 - month / 12) - 2

    d = (int(day + x + (31 * m / 12)) % 7)

    for i in range(d):
        if i == 1:
            print("Monday")
            break
        elif i == 2:
            print("Tuesday")
            break
        elif i == 3:
            print("Wednesday")
            break
        elif i == 4:
            print("Thursday")
            break
        elif i == 5:
            print("Friday")
            break
        elif i == 6:
            print("Saturday")
            break
        else:
            print("Sunday")
            break

        return i

