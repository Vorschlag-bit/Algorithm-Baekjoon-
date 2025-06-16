import java.util.*;
class Solution {
    public int[] solution(int[] arr, int m) {
        List<Integer> ans = new ArrayList<>();
        for (int a : arr) {
            if (a % m == 0) ans.add(a);
        }
        if (ans.size() > 0) {
            Collections.sort(ans);
            return ans.stream().mapToInt(Integer::intValue).toArray();
        } else {
            return new int[] {-1};
        }
    }
}