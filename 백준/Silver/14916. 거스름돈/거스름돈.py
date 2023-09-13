n = int(input())

# 5원 동전으로 최대한 거슬러 줌
five_coin = n // 5

while five_coin >= 0:
    remainder = n - (five_coin * 5)
    
    # 남은 금액이 2원 동전으로 거슬러 줄 수 있는지 확인
    if remainder % 2 == 0:
        two_coin = remainder // 2
        print(five_coin + two_coin)
        exit()
    else:
        five_coin -= 1

# 거슬러 줄 수 없는 경우
print(-1)
