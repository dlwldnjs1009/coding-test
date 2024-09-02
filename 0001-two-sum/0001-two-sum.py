# 1. 배열 index 번호 0부터 마지막까지 순회해서 하나씩 뽑기
# 2. 뽑은 index 번호를 +1씩 하여 taget이 될 수 있는지 비교
# 3. index 번호가 마지막일 경우 종료
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        answer = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
             