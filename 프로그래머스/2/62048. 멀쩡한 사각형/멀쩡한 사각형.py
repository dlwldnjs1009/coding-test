def solution(w, h):
    # 최대공약수를 구하는 함수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 전체 정사각형의 수
    total = w * h
    # 대각선에 의해 잘리는 정사각형의 수
    cut = w + h - gcd(w, h)
    
    # 사용할 수 있는 정사각형의 수
    answer = total - cut
    return answer

# 테스트
print(solution(8, 12))  # 80을 반환해야 함

