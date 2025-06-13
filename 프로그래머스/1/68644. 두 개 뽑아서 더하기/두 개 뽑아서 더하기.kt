class Solution {
    fun solution(numbers: IntArray): Array<Int> {
        val answer = mutableSetOf<Int>()
        val combination = combinations(numbers.toList(), 2)
        for (c in combination) {
            answer.add(c[0] + c[1])
        }
        return answer.sorted().toTypedArray()
    }
    fun <T> combinations(arr: List<T>, n: Int): List<List<T>> {
        val result = mutableListOf<List<T>>()
        fun dfs(idx: Int, path: MutableList<T>) {
            if (path.size == n) {
                result.add(path.toList())
                return
            }
            
            for (i in idx until arr.size) {
                path.add(arr[i])
                dfs(i+1,path)
                path.removeLast()
            }
        }
        dfs(0, mutableListOf())
        return result
    }
}