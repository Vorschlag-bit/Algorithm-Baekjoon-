import java.util.*;
class Solution {
    boolean solution(String s) {
        HashMap<Character, Integer> m = new HashMap<>();
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (m.containsKey(c)) {
                m.put(c, m.get(c)+1);
            } else {
                m.put(c,1);
            }
        }
        if (m.getOrDefault('p',0) == m.getOrDefault('y',0)) {
            return true;
        } else return false;
    }
}