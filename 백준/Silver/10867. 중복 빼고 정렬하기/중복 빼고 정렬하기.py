from sys import stdin

n = int(input())
# set 사용한 후 정렬
arrs = set(map(int, input().split()))

list_arrs = list(arrs)
list_arrs.sort()


for arr in list_arrs:
    print(arr, end=' ')
