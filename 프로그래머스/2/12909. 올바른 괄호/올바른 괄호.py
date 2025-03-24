def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        # 괄호의 순서가 올바르지 않으면 중간에 count가 음수가 됨
        if count < 0:
            return False
    # 모든 괄호가 짝을 이루었는지 마지막에 count가 0인지 확인
    return count == 0
