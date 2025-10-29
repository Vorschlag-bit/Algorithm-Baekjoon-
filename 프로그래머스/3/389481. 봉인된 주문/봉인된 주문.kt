class Solution {
    // 26진수를 10진수로
    fun n2dec(str: String): Long {
        var num = 0L
        for (chr in str) {
            // 1-based
            val n = (chr - 'a' + 1)
            num = num * 26 + n
        }
        return num
    }
    
    // 10진수를 26진수로
    fun dec2n(num: Long): String {
        if (num == 0L) return "0"
        var digit = ""
        var n = num
        while (n > 0) {
            n -= 1
            val r = (n%26).toInt()
            digit = ('a' + r) + digit
            n /= 26
        }
        return digit
    }
    
    fun solution(n: Long, bans: Array<String>): String {
        val bansN = bans.map { n2dec(it) }.sorted()
        var left = 0L
        var right = n + bansN.size
        while (left < right) {
            // n의 실제 순서
            val mid = (right + left) / 2
            var l = 0
            var r = bansN.size
            // mid 이하의 밴 개수
            while (l < r) {
                val m = (l+r) / 2
                if (bansN[m] <= mid) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            // mid 이하의 벤 개수를 뺀 것이 n 이상이면 만족
            if (mid - l >= n) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return dec2n(left)
    }
}