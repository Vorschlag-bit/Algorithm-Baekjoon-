import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int e : arr) list.add(e);
        int m = Integer.MAX_VALUE;
        for (int e : list) {
            m = Math.min(m,e);
        }
        list.remove(Integer.valueOf(m));
        if (!list.isEmpty())
            return list.stream().mapToInt(Integer::intValue).toArray();
        else return new int[] {-1};
    }
}