from bisect import bisect_left, bisect_right
def count(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split())
data = list(map(int, input().split()))

if count(data, x, x) != 0:
    print(count(data, x, x))
else:
    print(-1)