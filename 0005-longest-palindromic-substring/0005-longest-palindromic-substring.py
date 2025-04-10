class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 펠린드롬 판변 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        #해당 사항 없을 때 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        # 슬라이딩 윈도우 우측 이동
        for i in range(len(s) - 1):
            result = max(result,
                            expand(i, i + 1),
                            expand(i, i + 2),
                            key=len)
        return result
        