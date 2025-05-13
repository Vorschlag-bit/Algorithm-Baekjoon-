import java.util.*
class Solution {
    fun solution(n: Int, roads: Array<IntArray>, sources: IntArray, d: Int): IntArray {
        val graph = Array(n+1){ mutableListOf<Int>() }
        for (r in roads) {
            val (a,b) = r
            graph[a].add(b)
            graph[b].add(a)
        }
        val dis = IntArray(n+1){-1}
        val q: Queue<Int> = LinkedList()
        dis[d] = 0
        q.add(d)
        while (q.isNotEmpty()) {
            val cur = q.poll()
            for (next in graph[cur]) {
                if (dis[next] == -1) {
                    dis[next] = dis[cur] + 1
                    q.add(next)
                }
            }
        }
        return sources.map { dis[it] }.toIntArray()
    }
}