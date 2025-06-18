import java.util.*;
class Solution {
    public int[] solution(long begin, long end) {
        List<Long> ans = new ArrayList<>();
        for (long i = begin; i <= end; i++) {
            ans.add(get(i));
        }
        return ans.stream().mapToInt(Long::intValue).toArray();
    }
    public long get(long n) {
        if (n == 1) return 0;
        long max = 10000000;
        long m = 1;
        long t = (long) Math.sqrt(n) + 1;
        for (long i = 2; i <= t; i++) {
            if (n % i == 0) {
                long b = n / i;
                if (b <= max) return b;
                if (i <= max) m = Math.max(m,i);
            }
        }
        return m;
    }
}