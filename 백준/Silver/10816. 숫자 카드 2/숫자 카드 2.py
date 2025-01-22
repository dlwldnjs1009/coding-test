import sys

n = int(input())
num_arr = list(map(int, sys.stdin.readline().split()))

# 양수 음수 리스트 따로 만들면 되지 않을까
positive_list = ([0] * 10000001)
negative_list = ([0] * 10000001)

for num in num_arr:
    if num > 0:
        positive_list[num] += 1
    elif num == 0:
        positive_list[0] += 1
        negative_list[0] += 1
    else:
        num *= -1
        negative_list[num] += 1
m = int(input())
ans_nums = list(map(int, sys.stdin.readline().split()))
for ans_num in ans_nums:
    if ans_num > 0:
        print(positive_list[ans_num], end=' ')
    elif ans_num == 0:
        print((positive_list[0]), end=' ')
    else:
        ans_num *= -1
        print(negative_list[ans_num], end=' ')

