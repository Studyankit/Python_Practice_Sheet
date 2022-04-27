def anagram(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    # Check the list size and characters are same or not
    if len(list1) == len(list2):
        return True if list1 == list2 else False
    return False


print(anagram('heart', 'earth'))
