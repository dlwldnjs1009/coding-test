class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        // nums for문으로 돌면서 더했을 때 target되면 인덱스 반환
        for (int i = 0; i < nums.length;  i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                }
                
            }
        }
        return ans;
    }
}