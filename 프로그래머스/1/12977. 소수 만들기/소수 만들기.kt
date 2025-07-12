import kotlin.math.sqrt
class Solution {
    fun solution(nums: IntArray): Int {
        var ans = 0
        val combs = comb(nums)
        for (c in combs) {
            if (minor(c.sum())) ans++
        }

        return ans
    }
    
    fun minor(n: Int): Boolean {
        val m = sqrt(n.toDouble()).toInt() + 1
        for (i in 2..m) {
            if (n % i == 0) return false
        }
        return true
    }
    
    fun comb(arr: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val l = arr.size
        fun dfs(idx: Int, path: MutableList<Int>) {
            if (path.size == 3) {
                result.add(path.toList())
                return
            }
            for (i in idx until l) {
                path.add(arr[i])
                dfs(i+1,path)
                path.remove(arr[i])
            }
        }
        dfs(0,mutableListOf())
        return result
    }
}