from collections import deque
import sys

# 입력 개선을 위해 input 대신 sys.stdin.readline 사용
t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    numArray = sys.stdin.readline().strip()

    # 배열 입력이 없는 경우 바로 에러 처리
    if n == 0:
        if 'D' in p:
            print("error")
        else:
            print("[]")
        continue

    # 문자열을 리스트로 변환 (ast.literal_eval 대신)
    array = deque(numArray[1:-1].split(",") if n > 0 else [])

    # 뒤집힘 상태 플래그
    is_reversed = False

    error_flag = False
    for cmd in p:
        if cmd == 'R':
            # 뒤집힘 상태 토글
            is_reversed = not is_reversed
        elif cmd == 'D':
            if array:
                if is_reversed:
                    array.pop()  # 뒤집힌 상태에서는 마지막 원소를 제거
                else:
                    array.popleft()  # 원래 상태에서는 첫 번째 원소를 제거
            else:
                print("error")
                error_flag = True
                break

    if error_flag:
        continue

    # 뒤집힌 상태에 따라 최종 배열을 조정
    result = list(array) if not is_reversed else list(reversed(array))
    print("[" + ",".join(result) + "]")
