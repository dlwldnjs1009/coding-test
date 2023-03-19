n = int(input())

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


d = [0] * (n+1)
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]
print(fibo(n), n-2)
