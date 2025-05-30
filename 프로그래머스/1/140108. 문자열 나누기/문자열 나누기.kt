class Solution {
    fun solution(s: String): Int {
        var ans = 0
        var cnt = 0
        var prev = 'K'
        s.forEach {
            if (cnt == 0) {
                prev = it
            }
            if (it == prev) cnt++
            else cnt--
            if (cnt == 0) ans++
        }
        if (cnt > 0) ans++
        return ans
    }
}