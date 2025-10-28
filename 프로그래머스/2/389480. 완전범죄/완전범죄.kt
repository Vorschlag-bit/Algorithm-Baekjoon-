class Solution {
    var ans = Int.MAX_VALUE
    val visit = mutableSetOf<Triple<Int,Int,Int>>()
    fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
        
        fun dfs(idx: Int, a_sum: Int, b_sum: Int) {
            if (a_sum >= ans) return
            if (a_sum >= n) return
            if (b_sum >= m) return
            if (idx == info.size) {
                ans = minOf(ans,a_sum)
                return
            }
            val k = Triple(idx,a_sum,b_sum)
            if (k in visit) return
            visit.add(k)
            
            dfs(idx+1,a_sum+info[idx][0],b_sum)
            dfs(idx+1,a_sum,b_sum+info[idx][1])
        }
        dfs(0,0,0)
        return if (ans < n) ans else -1
    }
}