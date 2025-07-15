class Solution {
    fun reverseString(s: CharArray): Unit {
        var start = 0
        var end = s.size -1

        while (start < end) {
        // also를 이용해 우아하게 스왑
        s[start] = s[end].also {s[end] = s[start]}

        // 앞쪽 문자는 한 칸 뒤로, 뒤쪽 문자는 한 칸 앞으로 이동
        start++
        end--
        }
    }
}