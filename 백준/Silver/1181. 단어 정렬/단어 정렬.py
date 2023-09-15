n = int(input())


array = []
for i in range(n):
    a = input()
    if a not in array:
        array.append(a)


def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = []
    right_side = []

    for x in tail:
        if len(x) < len(pivot) or (len(x) == len(pivot) and x < pivot):
            left_side.append(x)
        else:
            right_side.append(x)

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

result = quick_sort(array)
for word in result:
    print(word)
