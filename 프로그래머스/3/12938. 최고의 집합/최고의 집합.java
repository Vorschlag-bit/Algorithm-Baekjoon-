import java.util.*;
class Solution {
    public int[] solution(int n, int s) {
        int[] ans = new int[n];
        if (n > s) {return new int[] {-1};}
        int q = s / n;
        int r = s % n;
        for (int i = 0; i < n-r; i++) {
            ans[i] = q;
        }
        for (int i = n-r; i < n; i++) {
            ans[i] = q+1;
        }
        return ans;
    }
}