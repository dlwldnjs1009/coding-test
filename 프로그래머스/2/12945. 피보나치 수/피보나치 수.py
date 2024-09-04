def solution(n):
    if n == 1 or n==2:
        return 1
    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] =1
    for i in range(3, n+1):
        fib[i] = (fib[i-1]+fib[i-2]) % 1234567
    return fib[n]