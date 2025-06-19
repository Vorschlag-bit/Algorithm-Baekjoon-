import java.util.*;
class Solution {
    public int solution(int n) {
        return Arrays.stream(get(n)).sum();
    }
    
    public int[] get(int n) {
        List<Integer> l = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) l.add(i);
        }
        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}