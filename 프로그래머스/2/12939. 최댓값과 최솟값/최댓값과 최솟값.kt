class Solution {
    fun solution(s: String): String {
        val arr = s.split(" ").map { it.toInt() }.sorted()
        return arr[0].toString() + " " + arr[arr.lastIndex].toString()
    }
}