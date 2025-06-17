class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        return strings.sortedWith(
            compareBy<String> {it[n]}
            .thenBy{it}
        ).toTypedArray()
    }
}