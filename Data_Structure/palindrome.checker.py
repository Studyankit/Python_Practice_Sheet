from collections import deque


def palindrome_checker(str1: str):
    str1_deque = deque(str1)

    while len(str1_deque) > 1:
        first = str1_deque.popleft()
        last = str1_deque.pop()
        if first != last:
            return False

    return True

