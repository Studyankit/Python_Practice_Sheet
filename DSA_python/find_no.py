import math


def binary_search(ele_list: list, search_ele: int):
    lo = 0
    hi = len(ele_list) - 1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if search_ele == ele_list[mid]:
            return mid
        if ele_list[mid] < search_ele:
            lo = mid + 1
        if ele_list[mid] > search_ele:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    N = int(input("range: "))
    n = int(math.log(N, 2))
    num_list = [i for i in range(N)]
    print(num_list)
    user_input = int(input(f"guess a number from 0 - {N}: "))
    position = binary_search(ele_list=num_list, search_ele=user_input)
    print("not found" if position == -1 else f"found at  = {position} position")