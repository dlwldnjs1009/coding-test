import math
import sys

# 최소공약수 문제

n = int(input())
trees = [int(sys.stdin.readline().strip()) for _ in range(n)]

gcd = trees[1] - trees[0]
for i in range(1, n-1):
    gap = trees[i+1] - trees[i]
    gcd = math.gcd(gcd, gap)

add_trees = 0
for i in range(n-1):
    gap = trees[i+1] - trees[i]
    add_trees += (gap // gcd) - 1

print(add_trees)
