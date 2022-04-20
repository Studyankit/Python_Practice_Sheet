import re

string_Year = input("Enter a year")

# validation for min 4 digits
regex_year = "(^[0-9]{4,})"

# matching the pattern with the input
match = re.match(regex_year, string_Year)
Year = int(string_Year)

if match != None:
    if (Year % 400 == 0) and (Year % 100 == 0):
        print(f"{Year} is a century leap year")
    elif (Year % 4 == 0) and (Year % 100 != 0):
        print(f"{Year} is a leap year")
    else:
        print(f"{Year} is not a leap year")
else:
    print("Enter valid no")
