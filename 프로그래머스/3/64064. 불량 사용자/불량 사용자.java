import java.util.*;
class Solution {
    HashSet<String> answer = new HashSet<>();
    ArrayList<ArrayList<String>> bannedList = new ArrayList<>();
    public int solution(String[] user_id, String[] banned_id) {
        
        for(String banId : banned_id) {
            // 특정 아이디에 대한 조합리스트
            ArrayList<String> matched = new ArrayList<>();
            for(String userId : user_id) {
                if(match(userId, banId)) matched.add(userId);
            }
            bannedList.add(matched);
        }
        
        backtrack(new HashSet<>(), 0);
        
        return answer.size();
    }
    public boolean match(String ui, String bi) {
        if(bi.length() != ui.length()) return false;
        
        for(int i = 0; i < bi.length(); i++) {
            if(bi.charAt(i) != '*' && bi.charAt(i) != ui.charAt(i))
                return false;
        }
        return true;
    }
    
    private void backtrack(HashSet<String> cSet, int idx) {
        if(idx == bannedList.size()) {
            ArrayList<String> cList = new ArrayList<>(cSet);
            Collections.sort(cList);
            answer.add(String.join(",", cList));
            return;
        }
        
        for(String user : bannedList.get(idx)) {
            if(!cSet.contains(user)) {
                cSet.add(user);
                backtrack(cSet, idx + 1);
                cSet.remove(user);
            }
        }
    }
}