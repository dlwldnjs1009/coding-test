class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        // 1. 영숫자만 소문자로 추가
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        // 2. 팰린드롬 체크
        int left = 0, right = sb.length() - 1;
        while (left < right) {
            if (sb.charAt(left++) != sb.charAt(right--)) return false;
        }
        return true;
    }
}
