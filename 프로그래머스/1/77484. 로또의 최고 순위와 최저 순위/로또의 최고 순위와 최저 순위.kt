class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        val n = intArrayOf(6,6,5,4,3,2,1)
        val cnt_0 = lottos.count { it == 0 }
        var c = 0
        for (l in lottos) {
            if (l in win_nums) c++
        }
        return intArrayOf(n[cnt_0+c],n[c])
    }
}