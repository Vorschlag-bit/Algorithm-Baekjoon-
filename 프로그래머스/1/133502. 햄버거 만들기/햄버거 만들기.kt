class Solution {
    fun solution(ingredient: IntArray): Int {
        var ans = 0
        // 1 - 2 - 3 - 1
        var ing = ingredient.joinToString("")
        val stack = mutableListOf<Char>()
        for (chr in ing) {
            stack.add(chr)
            if (stack.size >= 4 &&
                stack[stack.lastIndex - 3] == '1' &&
                stack[stack.lastIndex - 2] == '2' &&
                stack[stack.lastIndex - 1] == '3' &&
                stack[stack.lastIndex] == '1') {
                repeat(4) { stack.removeAt(stack.lastIndex) }
                ans++
            }
        }
        return ans
    }
}