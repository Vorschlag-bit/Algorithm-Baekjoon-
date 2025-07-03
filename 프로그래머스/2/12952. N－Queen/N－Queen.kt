class Solution {
    private var m = 0
    private var ans = 0
    fun dfs(i: Int, col: MutableSet<Int>, d1: MutableSet<Int>, d2: MutableSet<Int>) {
        if (i == m) {
            ans++
            return
        }
        
        for (j in 0 until m) {
            if (j !in col && (i-j) !in d1 && (i+j) !in d2) {
                col.add(j)
                d1.add(i-j)
                d2.add(i+j)
                dfs(i+1,col,d1,d2)
                col.remove(j)
                d1.remove(i-j)
                d2.remove(i+j)
            }
        }
        return
    }
    
    fun solution(n: Int): Int {
        m = n
        dfs(0,mutableSetOf(),mutableSetOf(),mutableSetOf())
        return ans
    }
}