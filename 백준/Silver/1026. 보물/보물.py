n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

temp_b = b
a = sorted(a)

sum = 0
for i in range(n):
    sum += (a[i] * temp_b[temp_b.index(max(temp_b))])
    temp_b.remove(max(temp_b))

print(sum)
