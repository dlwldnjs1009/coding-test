n = int(input())  # 원하는 채널 N
m = int(input())  # 고장난 버튼의 수 M
broken = set(input().split()) if m else set()

# 현재 채널 100에서 +나 -만 눌러서 이동하는 경우의 수
min_press = abs(100 - n)

# 채널을 직접 입력할 수 있는 경우의 수를 계산
for channel in range(1000000):
    for ch in str(channel):
        if ch in broken:
            break
    else:  # for-else 구문, break 없이 for 루프를 끝까지 돌면 else가 실행됨
        # 직접 채널 입력 후 + 또는 - 버튼으로 조정하는 경우의 수
        min_press = min(min_press, abs(channel - n) + len(str(channel)))

print(min_press)
