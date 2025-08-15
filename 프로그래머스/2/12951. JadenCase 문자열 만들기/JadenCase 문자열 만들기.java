class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder(s.length());
        boolean isWordStart = true;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {
                // 공백은 그대로 추가 + 다음 문자는 단어 시작이 됨
                sb.append(' ');
                isWordStart = true;
            } else {
                // 단어의 시작이면: 알파벳은 대문자, 숫자는 그대로
                // 단어의 중간이면: 알파벳은 소문자, 숫자는 그대로
                if (isWordStart) {
                    sb.append(Character.toUpperCase(c));
                    isWordStart = false;
                } else {
                    sb.append(Character.toLowerCase(c));
                }
            }
        }

        return sb.toString();
    }
}