class Solution {
    fun solution(targets: Array<IntArray>): Int {
        var ans = 0
        targets.sortBy { it[1] }
        var l_e = -300001
        for ((s,e) in targets) {
            if (s >= l_e) {
                ans++
                l_e = e
            }
        }
        return ans
    }
}