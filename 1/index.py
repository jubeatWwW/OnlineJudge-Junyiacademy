arr = [1, [12, 3, [4, [5, 16]]]]

def reverse(arr):
    reversedList = []
    for i in arr:
        if isinstance(i, list):
            i = reverse(i)
        reversedList.append(i)
    return list(reversed(reversedList))

print(reverse(arr))
