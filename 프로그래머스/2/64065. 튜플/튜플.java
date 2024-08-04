import java.util.*;
class Solution {
    public int[] solution(String s) {
        s = s.substring(2, s.length() - 2);
        String[] sets = s.split("},\\{");

        Arrays.sort(sets, (o1, o2) -> o1.length() - o2.length());
        Set<Integer> ans = new HashSet<>();
        ArrayList<Integer> list = new ArrayList<>();

        for(String str : sets) {
            for(String num : str.split(",")) {
                int n = Integer.parseInt(num);
                if(!ans.contains(n)) {
                    ans.add(n);
                    list.add(n);
                }
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}