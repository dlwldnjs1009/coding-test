class Solution {
    fun isPalindrome(s: String): Boolean {
        var start = 0
        var end = s.length - 1

        // 서로 중앙으로 이동해 나가다 겹치는 지점에 도달하면 종료
        while (start < end) {
            when {
                !Character.isLetterOrDigit(s[start]) -> start++
                !Character.isLetterOrDigit(s[end]) -> end--
                else -> {
                    if (Character.toLowerCase(s[start]) != Character.toLowerCase(s[end])) {
                        return false
                    }
                    start++
                    end--
                }
            }
        }
        return true
    }
}