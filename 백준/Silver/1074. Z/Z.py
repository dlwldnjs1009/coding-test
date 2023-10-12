def z_order(n, r, c):
    if n == 0:
        return 0
    half = 1 << (n - 1)
    # Z의 4등분 중 어디에 위치하는지 판단
    if r < half and c < half:
        return z_order(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + z_order(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + z_order(n - 1, r - half, c)
    else:
        return 3 * half * half + z_order(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(z_order(N, r, c))
