def my_round(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)


n = int(input())
if n == 0:  # 의견이 없는 경우
    print(0)
else:
    difficulty_lev = [int(input()) for _ in range(n)]
    sorted_levels = sorted(difficulty_lev)
    
    exclude_count = my_round(n * 0.15)
    
    # 30% 절사평균을 위해 양쪽 끝을 제외
    trimmed_levels = sorted_levels[exclude_count:n - exclude_count]
    
    if len(trimmed_levels) == 0:  # 절사평균이 계산되지 않는 경우
        print(0)
    
    average = sum(trimmed_levels) / len(trimmed_levels)
    
    print(my_round(average))
