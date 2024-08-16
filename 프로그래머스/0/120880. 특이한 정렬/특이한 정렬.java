import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        return Arrays.stream(numlist).boxed().sorted(
        (o1, o2) -> {
            int diff = Math.abs(o1 - n) - Math.abs(o2 - n);
            return diff == 0 ? o2.compareTo(o1) : diff;
        }).mapToInt(Integer::intValue).toArray();
    }
}