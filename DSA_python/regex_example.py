import re


def regex_example(string):  # Function to replace elements in the string
    
    print("After~~~~>>")

    print("Replacing User Name at index: ", string.index('<<name>>'))
    string = (re.sub(r"<<name>>", "Ank", string))

    print("Replacing Full Name at index: ", string.index('<<full name>>'))
    string = (re.sub(r"<<full name>>", "Ankit Ghosh", string))

    print("Replacing Mobile Number at index: ", string.index('xxxxxxxxxx'))
    string = (re.sub(r"xxxxxxxxxx", "1234567890", string))

    print("Replacing Date at index: ", string.index('01/01/2016'))
    string = (re.sub(r"01/01/2016", "29/04/2022", string))

    return string


# Input String of sentence
string = """Hello <<name>>, We have your full name as <<full name>> in our system.
Your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification. 
Thank you BridgeLabz. 01/01/2016"""

print(string)

print(regex_example(string))
