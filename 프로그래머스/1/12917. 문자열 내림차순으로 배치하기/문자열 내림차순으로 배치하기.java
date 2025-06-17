import java.util.*;
class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        Character[] chrs = s.chars().mapToObj(c -> (char)c).toArray(Character[]::new);
        Arrays.sort(chrs, Comparator.reverseOrder());
        for (char c : chrs) sb.append(c);
        return sb.toString();
    }
}