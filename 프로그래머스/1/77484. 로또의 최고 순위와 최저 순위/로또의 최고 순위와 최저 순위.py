def solution(lottos, win_nums):
    answer = []
    exist = []
    non_exist = []
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            exist.append(lotto)
        elif lotto != 0:
            non_exist.append(lotto)
        else:
            zero += 1
    high = len(exist) + zero
    if high == 6:
        answer.append(1)
    elif high == 5:
        answer.append(2)
    elif high == 4:
        answer.append(3)
    elif high == 3:
        answer.append(4)
    elif high == 2:
        answer.append(5)
    else:
        answer.append(6)
    low = len(exist)
    if low == 6:
        answer.append(1)
    elif low == 5:
        answer.append(2)
    elif low == 4:
        answer.append(3)
    elif low == 3:
        answer.append(4)
    elif low == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

