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


note = [1, 2, 5, 10, 50, 100, 200, 500, 2000]
change = []

find_min_change(note, 90, change)

print(change)