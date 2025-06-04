class Solution {
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        var ans = -1
        var cnt = 0
        val arr = List(dungeons.size) { cnt++ }
        val perms = perm(arr, dungeons.size)
        for (p in perms) {
            var hp = k
            var c = 0
            for (idx in p) {
                val d = dungeons[idx]
                if (d[0] > hp) break
                hp -= d[1]
                c += 1
            }
            ans = Math.max(ans,c)
        }
        return ans
    }
    fun perm(arr: List<Int>, n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val cur = arr.toMutableList()
        fun bt(idx: Int) {
            if (idx == cur.size-1) {
                result.add(cur.toList())
            } else {
                for (i in idx until cur.size) {
                    val tmp = cur[idx]
                    cur[idx] = cur[i]
                    cur[i] = tmp
                    bt(idx+1)
                    cur[i] = cur[idx]
                    cur[idx] = tmp
                }
            }
        }
        bt(0)
        return result
    }
}