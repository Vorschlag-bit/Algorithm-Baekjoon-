class Solution {
    fun solution(s: String): String {
        var ans = ""
        var flag = true
        for (chr in s) {
            if (flag) {
                ans += chr.uppercase()
            } else {
                ans += chr.lowercase()
            }
            flag = chr == ' '
        }
        return ans
    }
}