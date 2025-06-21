class Solution {
    fun solution(n: Long): Long {
        var m = n.toString().toCharArray().sortedDescending().joinToString("")
        return m.toLong()
    }
}