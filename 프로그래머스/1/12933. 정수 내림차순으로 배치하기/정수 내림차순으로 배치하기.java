import java.util.*;
class Solution {
    public long solution(long n) {
        StringBuilder sb = new StringBuilder();
        char[] cs = String.valueOf(n).toCharArray();
        Arrays.sort(cs);
        for (int i = cs.length - 1; i >= 0; i--) {
            sb.append(cs[i]);
        }
        return Long.valueOf(sb.toString());
    }
}