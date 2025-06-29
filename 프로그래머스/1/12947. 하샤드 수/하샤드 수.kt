class Solution {
    fun solution(x: Int): Boolean {
        var n = 0
        var m = x
        while (m > 0) {
            n += (m%10)
            m /= 10
        }
        return x % n == 0
    }
}