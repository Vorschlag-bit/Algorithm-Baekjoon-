class Solution {
    fun solution(ingredient: IntArray): Int {
        var ans = 0
        // 1 - 2 - 3 - 1
        var ing = ingredient.joinToString("")
        val stack = mutableListOf<Char>()
        for (chr in ing) {
            stack.add(chr)
            if (stack.size >= 4 &&
                stack[stack.size - 4] == '1' &&
                stack[stack.size - 3] == '2' &&
                stack[stack.size - 2] == '3' &&
                stack[stack.size - 1] == '1') {
                repeat(4) { stack.removeAt(stack.size-1) }
                ans++
            }
        }
        return ans
    }
}