def count_score(score):
    if score == 6:
        return 1
    elif score == 5:
        return 2
    elif score == 4:
        return 3
    elif score == 3:
        return 4
    elif score == 2:
        return 5
    else:
        return 6

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
    answer.append(count_score(high))
    low = len(exist)
    answer.append(count_score(low))
    return answer

