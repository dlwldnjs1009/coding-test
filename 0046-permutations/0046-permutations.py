class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = list(permutations(nums, len(nums)))
        print(answer)
        return answer

