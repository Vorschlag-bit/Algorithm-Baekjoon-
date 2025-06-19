import java.util.*;
class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        List<Character> small = new ArrayList<>();
        List<Character> big = new ArrayList<>();
        for (int i=0; i < 26; i++) {
            big.add((char) (65+i)); 
            small.add((char) (97+i));
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLowerCase(c)) {
                int idx = (small.indexOf(c) + n) % 26;
                sb.append(small.get(idx));
            } else if (Character.isUpperCase(c)) {
                int idx = (big.indexOf(c) + n) % 26;
                sb.append(big.get(idx));
            } else sb.append(c);
        }
        return sb.toString();
    }
}