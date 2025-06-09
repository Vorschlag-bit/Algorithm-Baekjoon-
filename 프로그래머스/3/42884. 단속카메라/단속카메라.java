import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        int ans = 0;
        Arrays.sort(routes, (x1,x2) -> Integer.compare(x1[1],x2[1]));
        int l_e = -30001;
        for (int[] r : routes) {
            int s = r[0];
            int e = r[1];
            if (s > l_e) {
                ans++;
                l_e = e;
            }
        }
        return ans;
    }
}