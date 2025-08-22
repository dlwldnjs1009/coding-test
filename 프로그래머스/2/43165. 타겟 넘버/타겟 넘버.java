class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    
    private int dfs(int[] arr, int target, int index, int sum) {
        // 1. 종료 조건
        if (index == arr.length) {
            return sum == target ? 1: 0;
        }
        
        // 2. 선택지 탐색
        int count = 0;
        count += dfs(arr, target, index + 1, sum + arr[index]);
        count += dfs(arr, target, index + 1, sum - arr[index]);
        
        return count;
    }
}