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
        int end = 0;
        int minStart = 0;
        int minLength = gems.length;
        
        while(true) {
            // 모든 종류의 보석을 포함할 때까지
            if(map.size() < set.size()) {
                if(end == gems.length) break;
                map.put(gems[end], map.getOrDefault(gems[end], 0) + 1);
                end++;
            }
            else {
                // 모든 종류를 다 포함한다면 최소 구간 찾기
                if(end - start < minLength) {
                    minLength = end - start;
                    minStart = start;
                }
                
                map.put(gems[start], map.get(gems[start]) - 1);
                if(map.get(gems[start]) == 0)
                    map.remove(gems[start]);
                start++;
            }
        }
        
        int[] answer = {minStart + 1, minStart + minLength};
        return answer;
    }
}