def decimal_to_binary(n):
    num = []
    str1 = ''
    count = 0
    while n > 0:
        num.append(n % 2)
        # print(n % 2, end="")
        n = n // 2
        count += 1

    for i in range(count - 1, -1, -1):
        str1 += str(num[i])
    return str1


def test_method():
    # input1 = decimal_to_binary(90)
    # output1 = "1000"
    # assert input1 == output1

    input2 = decimal_to_binary(8)
    output2 = '1000'
    assert input2 == output2
