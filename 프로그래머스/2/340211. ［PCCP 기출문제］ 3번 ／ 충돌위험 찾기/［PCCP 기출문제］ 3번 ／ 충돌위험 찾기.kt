import java.util.*;
import kotlin.math.*;
data class Robot(
    var x: Int,
    var y: Int,
    val path: ArrayDeque<Pair<Int,Int>>,
    var goal: Boolean
)

class Solution {
    val directions = listOf(Pair(1,0),Pair(-1,0),Pair(0,1),Pair(0,-1))
    fun solution(points: Array<IntArray>, routes: Array<IntArray>): Int {
        var ans: Int = 0
        val n = points.size
        val x = routes.size
        val m = routes[0].size
        // 로봇은 이동 시 항상 최단 경로, r -> c 순으로 이동
        // 남은 로봇
        val Robots = mutableListOf<Robot>()
        // 시작부터 겹치는 거 판단
        val start = mutableMapOf<Pair<Int,Int>,Int>()
        for ((i,r) in routes.withIndex()) {
            val num = i+1
            val start_point = r[0] - 1
            val (sx,sy) = points[start_point]
            val q = ArrayDeque<Pair<Int,Int>>()
            for (j in 1 until m) {
                val p = r[j] - 1
                val (x,y) = points[p]
                q.addLast(Pair(x-1,y-1))
            }
            start[Pair(sx-1,sy-1)] = start.getOrDefault(Pair(sx-1,sy-1),0) + 1
            val robot = Robot(sx-1,sy-1,q,false)
            Robots.add(robot)
        }
        for (v in start.values) {
            if (v > 1) ans += 1
        }
        
        while (true) {
            var flag = true
            for (r in Robots) {
                if (!r.goal) {
                    flag = false
                    break
                }
            }
            if (flag) break
            
            // 이동한 로봇만 충돌 감지
            val moved = mutableListOf<Robot>()
            for (robot in Robots) {
                if (robot.goal) continue
                val (cx,cy,path,goal) = robot
                val (tx,ty) = path.peekFirst()
                val curD = abs(cx - tx) + abs(cy - ty)
                for ((dx,dy) in directions) {
                    val nx = cx + dx
                    val ny = cy + dy
                    // 거리가 줄어들어야 함
                    val nd = abs(nx - tx) + abs(ny - ty)
                    if (0 <= nx && 0 <= ny && nd < curD) {
                        robot.x = nx
                        robot.y = ny
                        moved.add(robot)
                        break
                    }
                }
            } 
            // 이동한 로봇에 대해서 체크
            // 새로 이동한 곳 충돌 체크 및 도착 체크
            val v = mutableMapOf<Pair<Int,Int>,Int>()
            for (robot in moved) {
                val (cx,cy,path,goal) = robot
                val (tx,ty) = path.peekFirst()
                if (cx == tx && cy == ty) {
                    path.pollFirst()
                    if (path.isEmpty()) {
                        robot.goal = true
                    }
                }
                val p = Pair(cx,cy)
                v[p] = v.getOrDefault(p,0) + 1
            }
            
            for (cnt in v.values) {
                if (cnt > 1) ans++
            }
        }
        
        return ans
    }
}