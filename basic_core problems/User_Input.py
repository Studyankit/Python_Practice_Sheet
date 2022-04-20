import re

User_Name = input("Enter your name")
regex_User_Name = "(^[A-Za-z]{3,})"
match = re.match(regex_User_Name, User_Name)

if match != None:
    print(User_Name)
else:
    print("The User Name should include min 3 char between a to z")