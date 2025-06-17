import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long l = 0;
        Arrays.sort(times);
        long r = (long) n*times[times.length - 1];
        while (l <= r) {
            long m = (l+r) / 2;
            long cnt = 0;
            for (int t : times) {
                cnt += m / t;
                if (cnt >= n) break;
            }
            if (cnt >= n) r = m-1;
            else l = m+1;
        }
        return l;
    }
}