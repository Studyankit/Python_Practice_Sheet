def bubble_sort(input_string: str):
    string_list = []
    for i in input_string:
        string_list.append(i)

    for i in range(len(string_list)):
        for j in range(0, len(string_list) - i - 1):
            if string_list[j] > string_list[j + 1]:
                temp = string_list[i]
                string_list[i] = string_list[i + 1]
                string_list[i + 1] = temp
    print(string_list)


if __name__ == "__main__":
    input_string = "Well Done"
    bubble_sort(input_string)
