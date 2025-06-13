import java.util.*
class Solution {
    fun solution(n: Int, results: Array<IntArray>): Int {
        var ans = 0
        val p_graph = mutableMapOf<Int,MutableList<Int>>()
        for (i in 1..n) {
            p_graph.put(i,mutableListOf<Int>())
        }
        val c_graph = mutableMapOf<Int,MutableList<Int>>()
        for (i in 1..n) {
            c_graph.put(i,mutableListOf<Int>())
        }
        for (r in results) {
            val a = r[0]
            val b = r[1]
            p_graph[b]!!.add(a)
            c_graph[a]!!.add(b)
        }
        fun p_bfs(idx: Int): Int {
            var cnt = 0
            val q = ArrayDeque<Int>()
            var visit = BooleanArray(n+1) {false}
            visit[idx] = true
            q.offer(idx)
            while (q.isNotEmpty()) {
                val cur = q.poll()
                for (nxt in p_graph[cur]!!) {
                    if (!visit[nxt]) {
                        visit[nxt] = true
                        cnt++
                        q.offer(nxt)
                    }
                }
            }
            return cnt
        }
        fun c_bfs(idx: Int): Int {
            var cnt = 0
            val q = ArrayDeque<Int>()
            var visit = BooleanArray(n+1) {false}
            visit[idx] = true
            q.offer(idx)
            while (q.isNotEmpty()) {
                val cur = q.poll()
                for (nxt in c_graph[cur]!!) {
                    if (!visit[nxt]) {
                        visit[nxt] = true
                        cnt++
                        q.offer(nxt)
                    }
                }
            }
            return cnt
        }
        
        for (idx in 1..n) {
            var cnt = 1
            cnt += p_bfs(idx)
            cnt += c_bfs(idx)
            if (cnt == n) ans++
        }
        return ans
    }
}