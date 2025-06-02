class Solution {
    fun solution(topping: IntArray): Int {
        var ans = 0
        val cnt = mutableMapOf<Int,Int>()
        topping.forEach {
            cnt[it] = cnt.getOrDefault(it,0) + 1
        }
        val s = mutableSetOf<Int>()
        for (t in topping) {
            s.add(t)
            cnt[t] = cnt[t]!! - 1
            if (cnt[t] == 0) {
                cnt.remove(t)
            }
            if (cnt.size == s.size) ans++
        }
        return ans
    }
}