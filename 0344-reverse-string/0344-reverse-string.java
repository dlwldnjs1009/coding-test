class Solution {
    public void reverseString(char[] s) {
        char temp = '0';
        int end = s.length -1;
        for (int i = 0; i < s.length / 2; i++) {
            temp = s[i];
            s[i] = s[end - i];
            s[end - i] = temp;
        }
    }
}