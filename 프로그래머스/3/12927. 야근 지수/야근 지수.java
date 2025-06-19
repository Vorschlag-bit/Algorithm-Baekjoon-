import java.util.*;
class Solution {
    public long solution(int n, int[] works) {
        if (Arrays.stream(works).sum() <= n) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int w : works) {
            pq.offer(-w);
        }
        while (n > 0) {
            int job = pq.poll();
            if (job == 0) break;
            job++;
            n--;
            pq.offer(job);
        }
        long ans = 0;
        for (int e : pq) {
            ans += e*e;
        }
        return ans;
    }
}