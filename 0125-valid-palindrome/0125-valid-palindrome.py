class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 거꾸로 뒤집어도 똑같은 문장인지 판별
        # 맨 중간 글자 빼고 나머지가 같은지 판별하면 되잖아
        # 홀수는 (strs / 2) 짝수는 strs / 2 + 1 가 중간 글자
        # len = 21 이면 0~20까지
        # 이경우 중간글자 10임 리스트의 0~9, 11~20
        # 0은 (len-1) -0 이랑 비교 1은 (len-1) - 1 이랑 비교 ~ 9는 (len-1) - 9랑 비교
        # strs = []
        # for char in s:
        #     if char.isalnum():
        #         strs.append(char.lower())

         # 좌우를 비교하여 회문 판별
        # for i in range(len(strs) // 2):
        #     if strs[i] != strs[len(strs) - 1 - i]:
        #         return False
        # return True

        # while len(strs) > 1:
        #     if strs.pop(0) != strs.pop():
        #         return False
        # return True

        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False


        return True