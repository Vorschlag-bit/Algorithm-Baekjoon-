import java.util.*;
class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        var ans = 0
        val q = ArrayDeque<Int>()
        for ((i,p) in players.withIndex()) {
            val st = i
            val et = i+1
            while (!q.isEmpty() && q.peekFirst() < et) {
                q.pollFirst()
            }
            
            val server = q.size
            if (server * m < p) {
                var t = p / m
                t -= server
                repeat(t) {
                    q.addLast(st+k)
                }
                ans += t
            }
        }
        return ans
    }
}