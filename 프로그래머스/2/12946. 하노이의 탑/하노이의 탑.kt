class Solution {
    fun solution(n: Int): Array<IntArray> {
        var ans = mutableListOf<IntArray>()
        fun dfs(n: Int, from: Int, to: Int, via: Int) {
            // BST를 구성하며 왼쪽 서브트리, 루트, 오른쪽 서브트리를 순회함
            // break point
            if (n == 1) {
               ans.add(intArrayOf(from,to)) 
               return
            }
            dfs(n-1, from, via, to)
            ans.add(intArrayOf(from,to))
            dfs(n-1, via, to, from)
        }
        dfs(n,1,3,2)
        return ans.toTypedArray()
    }
}