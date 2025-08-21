import java.util.*;

class Solution {
    public int solution(String numbers) {
        char[] digits = numbers.toCharArray();
        boolean[] used = new boolean[digits.length];
        Set<Integer> seen = new HashSet<>();
        Set<Integer> primes = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        dfs(digits, used, sb, seen, primes);
        
        return primes.size();
    }
    
    private void dfs(char[] digits, boolean[] used, StringBuilder sb, Set<Integer> seen, Set<Integer> primes) {
        // 길이가 1 이상이면 현재 값 검사
        if (sb.length() > 0) {
            int val = Integer.parseInt(sb.toString());
            // 아직 본 적 없는 숫자만 소수 판별
            if (seen.add(val) && isPrime(val)) {
                primes.add(val);
            }
        }
        
        for (int i = 0; i < digits.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            sb.append(digits[i]);
            
            dfs(digits, used, sb, seen, primes);
            
            sb.deleteCharAt(sb.length() - 1);
            used[i] = false;
        }
    }
    
    private boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        int limit = (int) Math.sqrt(n);
        for (int d = 3; d <= limit; d+= 2) {
            if (n % d == 0) return false;
        }
        return true;
    }
}