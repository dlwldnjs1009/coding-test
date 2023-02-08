n, k = map(int, input().split())
count=0
while True: # n>=k로 조건을 줬다면 더 좋았을 것
    if n%k ==0:
        n //= k
        count += 1
    elif n%k != 0:
        n -= 1
        count += 1
    if n == 1:
        break
print(count)