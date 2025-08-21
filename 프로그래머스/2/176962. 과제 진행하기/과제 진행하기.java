import java.util.*;
class Plan {
    String name;
    int start;
    int dur;
    
    public Plan(String name, int start,int dur) {
        this.name = name;
        this.start = start;
        this.dur = dur;
    }
}

class Solution {
    public String[] solution(String[][] plans) {
        List<String> ans = new ArrayList<>();
        Deque<Plan> stack = new ArrayDeque<>();
        List<Plan> planList = new ArrayList<>();
        for (String[] p : plans) {
            String name = p[0];
            int st = s2t(p[1]);
            int pt = Integer.valueOf(p[2]);
            planList.add(new Plan(name,st,pt));
        }
        // 시작시간 기준으로 정렬
        planList.sort(Comparator.comparingInt(p -> p.start));
        for (int i = 0; i < planList.size(); i++) {
            Plan cur = planList.get(i);
            int remain = 0;
            // 마지막이 아니라면 남은 시간은 다음 시작 - (현재 시작 + 요구시간)
            if (i < planList.size() - 1) 
                remain = planList.get(i+1).start - cur.start;
            // 마지막은 무제한
            else remain = Integer.MAX_VALUE;
            
            // 남은 시간이 요구시간보다 크다면 해치우고
            if (remain >= cur.dur) {
                ans.add(cur.name);
                remain -= cur.dur;
                // 남은 시간동안 stack에 있는 거 해치우기
                while(!stack.isEmpty() && remain > 0) {
                    Plan ex = stack.pollLast();
                    if (remain >= ex.dur) {
                        ans.add(ex.name);
                        remain -= ex.dur;
                    } else {
                        ex.dur -= remain;
                        remain = 0;
                        stack.add(ex);
                    }
                }
                
            } else {
                // 작다면 stack에 넣기
                cur.dur -= remain;
                stack.add(cur);
                remain = 0;
            }
        }
        
        return ans.toArray(new String[0]);
    }
    
    public int s2t(String str) {
        String[] t = str.split(":");
        return Integer.valueOf(t[0])*60 + Integer.valueOf(t[1]);
    }
}