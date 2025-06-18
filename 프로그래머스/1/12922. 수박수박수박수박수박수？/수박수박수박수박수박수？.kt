class Solution {
    fun solution(n: Int): String {
        var ans = ""
        for (i in 0 until n) {
            if (i % 2 == 0) ans += "수"
            else ans += "박"
        }
        return ans
    }
}