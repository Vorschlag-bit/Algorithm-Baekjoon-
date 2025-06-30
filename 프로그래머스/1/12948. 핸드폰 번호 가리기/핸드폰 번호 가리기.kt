class Solution {
    fun solution(pn: String): String {
        var ans = ""
        val l = pn.length - 4
        for (i in 0 until l) {
            ans += '*'
        }
        for (i in l until pn.length) {
            ans += pn[i]
        }
        return ans
    }
}