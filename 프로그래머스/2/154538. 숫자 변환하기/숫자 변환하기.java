import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int[] dp = new int[y+1];
        for (int i = 0 ; i <= y; i++) dp[i] = -1;
        dp[x] = 0;
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{x,0});
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int value = cur[0];
            int step = cur[1];
            if (value * 3 <= y && dp[value*3] == -1) {
                q.add(new int[] {value*3,step+1});
                dp[value*3] = step+1;
            }
            if (value * 2 <= y && dp[value*2] == -1) {
                q.add(new int[]{value*2,step+1});
                dp[value*2] = step+1;
            }
            if (value + n <= y && dp[value+n] == -1) {
                q.add(new int[]{value+n,step+1});
                dp[value+n] = step+1;
            }
        }
        return dp[y];
    }
}