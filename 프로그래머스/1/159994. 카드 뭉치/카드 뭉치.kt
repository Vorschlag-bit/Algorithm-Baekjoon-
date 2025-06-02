class Solution {
    fun solution(card1: Array<String>, card2: Array<String>, goal: Array<String>): String {
        val c1 = card1.toMutableList()
        val c2 = card2.toMutableList()
        for (g in goal) {
            if (c1.size > 0 && c1[0] == g) {
                c1.removeAt(0)
            }
            else if (c2.size > 0 && c2[0] == g) {
                c2.removeAt(0)
            }
            else {
                return "No"
            }
        }
        return "Yes"
    }
}