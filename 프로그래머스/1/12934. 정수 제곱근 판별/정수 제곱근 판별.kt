import kotlin.math.*
class Solution {
    fun solution(n: Long): Long {
        var answer: Long = -1
        val m: Long = sqrt(n.toDouble()).toLong()
        if (m*m == n) answer = (m+1)*(m+1)
        return answer
    }
}