import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        Set<String> set = new HashSet<>();
        Map<String, Integer> map = new HashMap<>();
        for(String gem : gems) {
            set.add(gem);
        }
        // 보석의 종류 수
        int start = 0;
        int minStart = 0;
        int minLength = gems.length;
        
        for(int end = 0; end < gems.length; end++) {
            map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);
            
            while(map.size() == set.size()) {
                if(end - start < minLength) {
                    minLength = end - start;
                    minStart = start;
                }
                
                map.put(gems[start], map.get(gems[start]) - 1);
                if(map.get(gems[start]) == 0) map.remove(gems[start]);
                start++;
            }
        }
        
        int[] answer = {minStart + 1, minStart + minLength + 1};
        return answer;
    }
}