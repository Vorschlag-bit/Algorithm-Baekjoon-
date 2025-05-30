class Solution {
    fun getDay(days: List<Int>): Int {
        return days[0]*12*28 + days[1]*28 + days[2]
    }
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        val ans = mutableListOf<Int>()
        val list = today.split(".").map { it.toInt() }
        // 모두 day로
        val condition = getDay(list)
        val map = mutableMapOf<Char,Int>()
        for (t in terms) {
            val (chr, period) = t.split(" ")
            map.put(chr[0],period.toInt())
        }
        for ((idx,p) in privacies.withIndex()) {
            val (ex, chr) = p.split(" ")
            val d = getDay(ex.split(".").map { it.toInt() }) + map[chr[0]]!!*28
            if (d <= condition) ans.add(idx+1)
        }
        return ans.toIntArray()
    }
}