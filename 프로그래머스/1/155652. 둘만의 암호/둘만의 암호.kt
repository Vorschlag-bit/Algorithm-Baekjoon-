class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        var ans = StringBuilder()
        val arr = mutableListOf<Char>()
        for (i in 0 .. 25) {
            if (('a' + i) !in skip) arr.add('a' + i)
        }
        val l = arr.size
        for (c in s) {
            val cur_i = arr.indexOf(c)
            val nxt_i = (cur_i + index) % l
            ans.append(arr[nxt_i])
        }
        return ans.toString()
    }
}