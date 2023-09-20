# 딕셔너리는 O(1)이니 시간복잡도 면에서도 좋다
n = int(input())
A = list(map(int, input().split()))
dict_A = {}
for i in A:
    dict_A[i] = True
m = int(input())
qustion_A = list(map(int, input().split()))
for j in qustion_A:
    if j in dict_A:
        print(1)
    else:
        print(0)
