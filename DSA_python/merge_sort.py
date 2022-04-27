def merge_sort(str_list):
    if len(str_list) > 1:
        mid = len(str_list) // 2

        left = str_list[:mid]
        right = str_list[mid:]
        
        merge_sort(left)
        merge_sort(right)

        left_index = right_index = k = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                str_list[k] = left[left_index]
                left_index += 1
            else:
                str_list[k] = right[right_index]
                right_index += 1
            k += 1

        # Checking if any element was left
        while left_index < len(left):
            str_list[k] = left[left_index]
            left_index += 1
            k += 1

        while right_index < len(right):
            str_list[k] = right[right_index]
            right_index += 1
            k += 1


def merge_sort_implementation():
    str_list = [12, 11, 13, 5, 6, 7]
    print("Given list is: \n", str_list)
    merge_sort(str_list)
    print("Sorted list is: \n", str_list)