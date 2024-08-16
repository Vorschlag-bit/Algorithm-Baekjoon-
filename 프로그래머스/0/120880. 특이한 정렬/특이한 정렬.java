import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        Integer[] arr = Arrays.stream(numlist).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, (o1, o2) -> {
            int diff = Math.abs(o1 - n) - Math.abs(o2 - n);
            if(diff == 0) return o2.compareTo(o1);
            return diff;
        });
    int[] solution = Arrays.stream(arr).mapToInt(Integer::intValue).toArray();
    return solution;
    }
}