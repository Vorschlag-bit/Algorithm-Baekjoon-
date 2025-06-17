class Solution {
    fun solution(n: Int): Int {
        val dp = IntArray(n+1) {0}
        if (n == 1) return 1
        if (n == 2) return 2
        dp[1] = 1
        dp[2] = 2
        for (i in 3..n) {
            dp[i] = (dp[i-1]+dp[i-2])%1234567
        }
        return dp[n]
    }
}