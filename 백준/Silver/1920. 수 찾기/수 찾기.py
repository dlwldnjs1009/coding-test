# 이진 탐색(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
A = list(map(int, input().split()))
m = int(input())
qustion_A = list(map(int, input().split()))
sorted_A = sorted(A)

for i in qustion_A:
    if binary_search(sorted_A, i, 0, n-1) == None:
        print(0)
    else:
        print(1)
