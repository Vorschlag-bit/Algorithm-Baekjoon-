class Solution {
    fun solution(num: Int): Int {
        var answer = 0
        var n = num.toLong()
        while (n != 1L) {
            if (n % 2 == 0L) n /= 2
            else n = n*3 + 1
            answer += 1
            if (answer > 500) {
                answer = -1
                break
            }
        }
        return answer
    }
}