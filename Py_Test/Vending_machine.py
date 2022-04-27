def find_min_change(note: list, n, change: list):
    note.sort(reverse=True)
    for i in range(len(note)):
        if note[i] < n:
            change.append(note[i])
            n -= note[i]
            find_min_change(note, n, change)
            break

        if note[i] == n:
            change.append(note[i])
            break
    return change


note = [1, 2, 5, 10, 50, 100, 200, 500, 2000]
change = []


# find_min_change(note, 90, change)
#
# print(change)

def test_method():
    # input1 = find_min_change(note, 90, change)
    # output1 = [50, 20, 20]
    # assert input1 == output1

    input2 = find_min_change(note, 100, change)
    output2 = [100]
    assert input2 == output2
