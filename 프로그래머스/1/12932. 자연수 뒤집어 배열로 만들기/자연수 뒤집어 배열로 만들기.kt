class Solution {
    fun solution(n: Long): IntArray {
        return n.toString().reversed().map {
            it - '0'
        }.toIntArray()
    }
}