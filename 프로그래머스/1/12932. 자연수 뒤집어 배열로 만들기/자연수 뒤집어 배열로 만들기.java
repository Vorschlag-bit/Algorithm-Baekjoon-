import java.util.*;
class Solution {
    public int[] solution(long n) {
        String m = String.valueOf(n);
        List<Integer> ans = new ArrayList<>();
        for (int i = m.length() - 1; i >= 0; i--) {
            System.out.println(m.charAt(i));
            ans.add(m.charAt(i) - '0');
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}