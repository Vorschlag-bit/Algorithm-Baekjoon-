class Solution {
    fun solution(s: String): Int {
        var str = s;
        if (s[0] == '+') str = s.substring(1);
        val answer = Integer.valueOf(str)
        return answer
    }
}