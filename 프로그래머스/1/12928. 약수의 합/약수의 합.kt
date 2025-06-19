class Solution {
    fun solution(n: Int): Int {
        return c(n).sum()
    }
    
    fun c(n: Int): Array<Int> {
        val list = mutableListOf<Int>()
        for (i in 1..n) {
            if (n % i == 0) list.add(i)
        }
        return list.toTypedArray()
    }
}