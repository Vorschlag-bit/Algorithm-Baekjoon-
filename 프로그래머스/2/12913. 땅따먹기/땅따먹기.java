class Solution {
    int solution(int[][] land) {
        int ans = 0;
        int n = land.length;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 4; j++) {
                int max = 0;
                for (int k = 0; k < 4; k++) {
                    if (k != j && max < land[i-1][k]) {
                        max = land[i-1][k];
                    }
                }
                land[i][j] += max;
            }
        }
        for (int num : land[n-1]) {
            ans = Math.max(ans,num);
        }
        return ans;
    }
}