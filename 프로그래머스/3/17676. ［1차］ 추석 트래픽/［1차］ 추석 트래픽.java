import java.util.*;
class Solution {
    class Pair {
        int a;
        int b;
        public Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }
    
    public int solution(String[] lines) {
        int ans = 0;
        Pair[] arr = new Pair[lines.length];
        for (int i = 0; i < lines.length; i++) {
            arr[i] = s2ms(lines[i]);
        }
        List<Integer> timestamp = new ArrayList<>();
        for (Pair p : arr) {
            int a = p.a;
            int b = p.b;
            timestamp.add(a);
            timestamp.add(b);
        }
        for (int t : timestamp) {
            int cnt = 0;
            for (Pair p : arr) {
                int start = p.a;
                int end = p.b;
                if (t <= end && t + 1000 > start) cnt++;
            }
            ans = Math.max(ans, cnt);
        }
        return ans;
    }
    
    public Pair s2ms(String str) {
        String[] split = str.split(" ");
        String[] t = split[1].split(":");
        int h = Integer.valueOf(t[0])*60*60*1000;
        int m = Integer.valueOf(t[1])*60*1000;
        String[] s = t[2].split("\\.");
        int sec = Integer.valueOf(s[0])*1000;
        int ms = Integer.valueOf(s[1]);
        float duration = Float.valueOf(split[2].substring(0,split[2].length()-1))*1000;
        int end = h+m+sec+ms;
        int start = end - (int) duration + 1;
        return new Pair(start,end);
    }
}