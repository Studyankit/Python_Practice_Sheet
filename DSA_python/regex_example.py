# import re
#
#
# def regex_ex(str1: str):
#     first_name = "^[A-Z]{1}[a-z]{2,}$"
#     full_name = "^[A-Z]{1}[a-z]{2,}$"
#
#     new_str = str1.split()
#     print(new_str)
#     for i in new_str:
#         if i == "name":
#             name = new_str.match(first_name, i)
#             return name
#         elif i == "full_name":
#             full_name_match = new_str.match(full_name, i)
#             return full_name_match
#         else:
#             return 0
#
#
# 
#     # for name in str1:
#     #     if name == "<< name >>":
#     #         str1.replace(first_name, name)
#     #     elif name == "<< full name >>":
#     #         str1.replace(full_name, name)
#     #     else:
#     #         return str1
#
#
# str1 = "Hello name , We have your full name as full_name in our system. Your " \
#        "contact number . Please, let us know in case of any clarification Thank you BridgeLabz date"
# regex_ex(str1)
