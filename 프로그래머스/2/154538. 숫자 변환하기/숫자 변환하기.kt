import java.util.ArrayDeque
class Solution {
    fun solution(x: Int, y: Int, n: Int): Int {
        val q = ArrayDeque<Pair<Int,Int>>()
        val visit = Array(y+1) { false }
        visit[x] = true
        q.addLast(Pair(x,0))
        while (q.isNotEmpty()) {
            val (cur,cnt) = q.removeFirst()
            if (cur == y) return cnt
            if (cur + n <= y && !visit[cur+n]) {
                q.addLast(Pair(cur+n,cnt+1))   
                visit[cur+n] = true
            }
            if (cur * 2 <= y) {
                q.addLast(Pair(cur*2,cnt+1))
                visit[cur*2] = true
            }
            if (cur * 3 <= y) {
                q.addLast(Pair(cur*3,cnt+1))
                visit[cur*3] = true
            }
        }
        return -1
    }
}