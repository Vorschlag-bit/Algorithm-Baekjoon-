class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var m = n
        while (m > 0) {
            answer += m % 10
            m /= 10
        }
        return answer
    }
}