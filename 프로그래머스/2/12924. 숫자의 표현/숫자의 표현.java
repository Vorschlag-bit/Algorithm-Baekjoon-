import java.util.*;
class Solution {
    public int solution(int n) {
        List<Integer> arr = new ArrayList<>();
        arr.add(0);
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            arr.add(arr.get(arr.size() - 1) + i);
        }
        int l = 0;
        int r = 0;
        while (r < arr.size()) {
            int sum = arr.get(r) - arr.get(l);
            if (sum == n) {
                answer++;
                r++;
            }
            else if (sum > n) {
                l++;
            } else {
                r++;
            }
        }
        return answer;
    }
}