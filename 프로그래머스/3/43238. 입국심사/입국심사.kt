class Solution {
    fun solution(n: Int, times: IntArray): Long {
        var l: Long = 0
        val s = times.sorted()
        var r: Long = n.toLong()*s[s.size - 1]
        while (l <= r) {
            val m: Long = (l+r) / 2
            var cnt: Long = 0
            for (t in s) {
                cnt += m / t
                if (cnt >= n) break
            }
            if (cnt >= n) r = m -1
            else l = m + 1
        }
        return l
    }
}