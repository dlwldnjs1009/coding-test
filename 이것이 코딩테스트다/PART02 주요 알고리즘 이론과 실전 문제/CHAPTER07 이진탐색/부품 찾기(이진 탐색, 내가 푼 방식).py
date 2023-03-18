# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
array_stock = list(map(int, input().split()))
array_stock.sort()
m = int(input())
array_request = list(map(int, input().split()))

for array_requests in array_request:
    result = binary_search(array_stock, array_requests, 0, n - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")


