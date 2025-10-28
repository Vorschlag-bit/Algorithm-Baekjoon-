class Solution {
    fun solution(dice: Array<IntArray>): List<Int> {
        var max_win = 0
        var ans = listOf(1,2)
        val n = dice.size
        // 주사위 n / 2개 선택
        val arr = mutableListOf<Int>()
        for (i in 0 until n) arr.add(i)
        // 조합(n/2)
        val comb = combination(arr,n/2)
        for (c in comb) {
            val mine = mutableListOf<IntArray>()
            for (idx in c) {
                mine.add(dice[idx])
            }
            val your = mutableListOf<IntArray>()
            for (idx in 0 until dice.size) {
                if (idx in c) continue
                your.add(dice[idx])
            }
            var win = duel(mine,your)
            if (win > max_win) {
                max_win = win
                ans = c.toList()
            }
        }
        val answer = mutableListOf<Int>()
        ans.forEach { answer.add(it+1) }
        return answer.toList()
    }
    
    fun duel(mine: MutableList<IntArray>, your: MutableList<IntArray>): Int {
        val d = listOf(0,1,2,3,4,5)
        var cnt = 0
        // 어떤 주사위 눈이 나오게 할 건지
        // 상대 주사위로 만들 수 있는 모든 점수(중복 순열)
        val your_score = mutableListOf<Int>()
        val prods = product(d,your.size)
        for (p in prods) {
            // 0,1
            var s = 0
            for (i in 0 until your.size) {
                s += your[i][p[i]]
            }
            your_score.add(s)
        }
        // 오름차순 정렬
        val ys = your_score.sortedBy { it }
        val prod = product(d,mine.size)
        for (p in prod) {
            var s = 0
            for (i in 0 until mine.size) {
                s += mine[i][p[i]]
            }
            cnt += bisect_left(ys,s)
        }
        return cnt
    }
    
    fun bisect_left(arr: List<Int>, r: Int): Int {
        var left = 0
        var right = arr.size
        while (left < right) {
            val mid = (left+right) / 2
            if (arr[mid] < r) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
    
    fun combination(arr: MutableList<Int>, r: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        
        fun dfs(idx: Int, cur: MutableList<Int>) {
            if (cur.size == r) {
                result.add(cur.toList())
                return
            }
            
            for (i in idx until arr.size) {
                cur.add(arr[i])
                dfs(i+1,cur)
                cur.removeAt(cur.size - 1)
            }
        }
        
        dfs(0,mutableListOf())
        return result
    }
    
    fun product(arr: List<Int>, r: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        fun dfs(idx: Int, cur: MutableList<Int>) {
            if (idx == r) {
                result.add(cur.toList())
                return
            }
            
            for (num in arr) {
                cur.add(num)
                dfs(idx+1,cur)
                cur.removeAt(cur.size-1)
            }
        }
        dfs(0,mutableListOf())
        return result
    }
}