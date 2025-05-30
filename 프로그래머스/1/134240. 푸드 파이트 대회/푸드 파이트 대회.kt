class Solution {
    fun solution(food: IntArray): String {
        val ans = StringBuilder()
        val sb = StringBuilder()
        for (idx in 1 until food.size) {
            if (food[idx] >= 2) {
                val cnt = food[idx] / 2
                repeat(cnt) { ans.append(idx) }
                repeat(cnt) { sb.append(idx) }
            }
        }
        ans.append('0').append(sb.reversed())
        return ans.toString()
    }
}