class Solution {
    fun solution(bab: Array<String>): Int {
        var ans = 0
        // 연속발음할 순 없다.
        for (i in bab.indices) {
            bab[i] = bab[i]
             .replace("aya","2")
             .replace("ye","3")
             .replace("woo","4")
             .replace("ma","1")
        }
        for (b in bab) {
            var flag = true
            var prev = '.'
            for (chr in b) {
                if (!chr.isDigit() || chr == prev) {
                    flag = false
                    break
                }
                prev = chr
            }
            if (flag) ans ++
        }
        return ans
    }
}