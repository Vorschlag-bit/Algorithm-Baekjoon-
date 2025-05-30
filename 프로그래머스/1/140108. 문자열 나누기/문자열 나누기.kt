class Solution {
    fun solution(s: String): Int {
        var ans = 0
        var start = s[0]
        var same = 0
        var diff = 0
        for (idx in s.indices) {
            if (s[idx] == start) same++ else diff++
            if (same == diff) {
                same = 0
                diff = 0
                ans++
                if (idx+1 < s.length) start = s[idx+1]
            }
        }
        if (same != 0 || diff != 0) ans++
        return ans
    }
}