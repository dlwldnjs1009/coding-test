n = int(input())
data = list(map(int, input().split()))
data.sort()
sum_array = []
sum = 0
for i in range(n):
    sum +=  data[i]
    sum_array.append(sum)
sum_minute = 0
for j in sum_array:
    sum_minute += j

print(sum_minute)
