class Solution {
    var temp1 = 0
    var temp2 = 0
    var tp = 0
    fun solution(temp: Int, t1: Int, t2: Int, a: Int, b: Int, board: IntArray): Int {
        temp1 = t1 + 10
        temp2 = t2 + 10
        tp = temp + 10
        val n = board.size
        val m = 51
        // 항상 실내온도는 t1 ~ t2 사이 유지
        // 0분의 실내온도는 실외온도와 같다
        // 실내온도가 희망온도와 다르다면 1분 뒤 희망온도와 같아지는 방향으로 1도 상승/하강(같다면 에어컨 켜진 동안 온도변화 x)
        // 희망온도와 실내온도가 다르다면 매 분 a만큼 소비 같다면 b만큼 소비 꺼져있으면 소비 x
        // 승객 탑승 중에만 실내온도를 t1~t2로 유지하되 소비전력 최소화
        
        // dp[i][j] = i시간 j온도일 때 최소의 소비 전력
        // 에어컨을 키거나 끌 수 있음
        // 끄는 경우 현재 온도에 따라서 다음 온도가 결정됌
        // 키는 경우 현재 온도에 따라서 다음 온도 결정 + 전력이 소비
        val dp = Array(n) { IntArray(m) { Integer.MAX_VALUE } }
        dp[0][tp] = 0
        for (i in 0 until n-1) {
            for (j in 0 until m) {
                if (dp[i][j] == Integer.MAX_VALUE) continue
                
                // off
                val nxtTemp = when {
                    // 실외보다 따듯하면 내려감
                    j > tp -> j - 1
                    // 실외보다 추우면 올라감
                    j < tp -> j + 1
                    // 같다면 그대로
                    else -> j
                }
                
                // 다음 시간에 해당 온도가 유효한지 판별
                if (check(board,i+1,nxtTemp)) dp[i+1][nxtTemp] = minOf(dp[i+1][nxtTemp], dp[i][j])
                
                // on(온도 상승, 하강, 유지 to cost)
                val pair = listOf(
                    j + 1 to a,
                    j - 1 to a,
                    j to b
                )
                
                for ((nxtTemp,cost) in pair) {
                    // 최대 최소를 벗어나면 pass
                    if (nxtTemp !in 0..50) continue
                    // 유효성 검사 실패 시 pass
                    if (!check(board,i+1,nxtTemp)) continue
                    
                    // 기존 값과 cur + cost 비교
                    dp[i+1][nxtTemp] = minOf(dp[i+1][nxtTemp], cost + dp[i][j])
                }
            }
        }
        return dp[n-1].minOrNull() ?: 0
    }
    
    fun check(board: IntArray, time: Int, temp: Int): Boolean {
        // 탑승 중이 아니라면 온도 상관 x
        if (board[time] == 0) return true
        
        // 온도가 t1, t2 사이가 아니라면 false
        return temp in temp1..temp2
    }
}