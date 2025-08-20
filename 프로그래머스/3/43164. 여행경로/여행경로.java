import java.util.*;
class Solution {
    static Map<String,List<String>> map = new HashMap<>();
    static Map<String,boolean[]> used = new HashMap<>();
    static int T;
    static List<String> answer = new ArrayList<>();
    public String[] solution(String[][] tickets) {
        for (String[] t : tickets) {
            String start = t[0];
            String end = t[1];
            map.computeIfAbsent(start, k -> new ArrayList<>()).add(end);
        }
        // 공항 개수
        T = tickets.length + 1;
        for (String k : map.keySet()) {
            // 알파벳순 정렬된 리스트로 다시 넣기
            List<String> l = map.get(k);
            Collections.sort(l);
        }
        
        for (Map.Entry<String, List<String>> e : map.entrySet()) {
            used.put(e.getKey(), new boolean[e.getValue().size()]);
        }
        // 시작, visited, answer
        List<String> path = new ArrayList<>();
        path.add("ICN");
        dfs("ICN",path);
        return answer.toArray(new String[0]);
    }
    
    public static boolean dfs(String start, List<String> path) {
       if (path.size() == T) {
           // 깊은 복사 후 리턴
           answer = new ArrayList<>(path);
           return true;
       }
        boolean[] u = used.get(start);
        List<String> nexts = map.getOrDefault(start, Collections.emptyList());
        for (int i = 0; i < nexts.size(); i++) {
            if (u[i]) continue;
            u[i] = true;
            path.add(nexts.get(i));
            if (dfs(nexts.get(i), path)) return true; 
            path.remove(path.size()-1);
            u[i] = false;
        }
        return false;
    }
}