import java.util.*;
class Solution {
    public long solution(int[] weights) {
        long ans = 0;
        // 2,3,4
        int[][] ratio = {{2,3},{2,4},{3,4}};
        Map<Long,Long> w = new HashMap<>();
        for (int weight : weights) {
            long we = (long) weight;
            w.put(we, w.getOrDefault(we,0L)+1);
        }
        for (long weight : w.keySet()) {
            long v = w.get(weight);
            // combination
            if (v > 1) {
                ans += (v*(v-1)) / 2;
            }
        }
        List<Long> keys = new ArrayList<>(w.keySet());
        Collections.sort(keys);
        for (long weight : keys) {
            // 해당 몸무게에 ratio가 있다면 그만큼 더하기
            for (int[] r : ratio) {
                int a = r[0];
                int b = r[1];
                // a * weight == b * x를 만족하면 한 쌍
                long num = (long) a * weight;
                if (num % b == 0) {
                    long t = num / b;
                    ans += w.get(weight) * w.getOrDefault(t,0L);
                }
            }
        }
        return ans;
    }
}