def string_permutation(input_string: str):
    string_list = []
    for i in input_string:
        string_list.append(i)

    for j in range(0, len(string_list)-1):
        for k in range(1, len(string_list)):

