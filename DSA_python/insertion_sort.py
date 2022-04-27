def insertion_sort(input_string: str):
    """
    Function to sort a string using insertion sort

    :param input_string:  String containing a word
    :return: sorted string of the input
    """
    string_list = []
    for i in input_string:
        string_list.append(i)

    for j in range(1, len(string_list)):
        key = string_list[j]
        j = j - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].

        while j >= 0 and key < string_list[j]:
            string_list[j + 1] = string_list[j]
            j = j - 1

            # Place key at after the element just smaller than it.
            string_list[j + 1] = key
    print(string_list)


if __name__ == "__main__":
    input_string = "Strong"
    insertion_sort(input_string)
