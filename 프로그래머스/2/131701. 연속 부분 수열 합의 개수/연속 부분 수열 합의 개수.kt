class Solution {
    fun solution(elements: IntArray): Int {
        val ans = mutableSetOf<Int>()
        val n = elements.size
        for (i in 0 until n) {
            var e = elements[i]
            ans.add(e)
            for (j in i+1 until i+n) {
                e += elements[j%n]
                ans.add(e)
            }
        }
        return ans.size
    }
}