class Solution {
    fun solution(seoul: Array<String>): String {
        var answer = "김서방은 "
        answer += seoul.indexOf("Kim")
        return answer + "에 있다"
    }
}