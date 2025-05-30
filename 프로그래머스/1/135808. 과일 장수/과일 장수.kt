class Solution {
    fun solution(k: Int, m: Int, score: IntArray): Int {
        var ans = 0
        val sorted = score.sortedDescending()
        var cnt = 0
        var min = k+1
        for (s in sorted) {
            min = Math.min(min,s)
            cnt++
            if (cnt == m) {
                ans += min*m
                cnt = 0
                min = k+1
            }
        }
        return ans
    }
}