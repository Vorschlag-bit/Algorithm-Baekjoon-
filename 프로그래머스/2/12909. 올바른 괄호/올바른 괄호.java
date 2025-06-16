import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean ans = true;
        Stack<Character> stack = new Stack<>();
        for (char e : s.toCharArray()) {
            if (e == '(') {
                stack.add(e);
            } else {
                if (stack.isEmpty() || stack.peek() != '(') {
                    ans = false;
                    break;
                } else {
                    stack.pop();
                }
            }
        }
        if (!stack.isEmpty()) ans = false;
        return ans;
    }
}