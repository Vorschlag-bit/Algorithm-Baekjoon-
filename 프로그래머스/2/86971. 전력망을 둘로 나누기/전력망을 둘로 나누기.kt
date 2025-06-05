import java.util.ArrayDeque
class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var ans = Integer.MAX_VALUE
        val graph = mutableMapOf<Int,MutableList<Int>>()
        for ((v1,v2) in wires) {
            graph.getOrPut(v1) { mutableListOf() }.add(v2)
            graph.getOrPut(v2) { mutableListOf() }.add(v1)
        }
        for ((v1,v2) in wires) {
            graph[v1]!!.remove(v2)
            graph[v2]!!.remove(v1)
            ans = minOf(bfs(graph,1,n),ans)
            graph[v1]!!.add(v2)
            graph[v2]!!.add(v1)
        }
        return ans
    }
    fun bfs(graph: Map<Int,List<Int>>, node: Int, n: Int): Int {
        val q = ArrayDeque<Int>()
        val visit = BooleanArray(n+1) { false }
        var cnt = 1
        visit[node] = true
        q.addLast(node)
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            for (nxt in graph[cur]!!) {
                if (!visit[nxt]) {
                    visit[nxt] = true
                    cnt++
                    q.addLast(nxt)
                }
            }
        }
        val diff = Math.abs(Math.abs(n-cnt)-cnt)
        return diff
    }
}