class Solution {
    fun solution(arr: IntArray, d: Int): IntArray {
        val ans = mutableListOf<Int>()
        for (e in arr) {
            if (e % d == 0) ans.add(e)
        }
        if (ans.size > 0) {
            return ans.sorted().toIntArray()
        } else {
            return intArrayOf(-1)
        }
    }
}