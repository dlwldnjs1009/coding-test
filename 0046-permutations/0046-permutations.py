class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = []
        answer = []

        def recur():
            if len(pick) == len(nums):
                answer.append(pick[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in pick:
                    pick.append(nums[i])
                    recur()
                    pick.pop()
        recur()
        return answer