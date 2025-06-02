class Solution {
    fun solution(numbers: IntArray): IntArray {
        val ans = Array(numbers.size){ -1 }
        val stack = mutableListOf<Int>()
        for (i in numbers.indices.reversed()) {
            while (stack.size > 0 && stack[stack.lastIndex] <= numbers[i]) {
                stack.removeLast()
            }
            if (stack.size > 0) ans[i] = stack[stack.lastIndex]
            stack.add(numbers[i])
        }
        return ans.toIntArray()
    }
}