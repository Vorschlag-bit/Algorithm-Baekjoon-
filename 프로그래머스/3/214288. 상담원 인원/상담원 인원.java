import java.util.*;
class Solution {
    public int solution(int k, int n, int[][] reqs) {
        int ans = Integer.MAX_VALUE;
        List<List<Integer>> sp = split(n,k);
        for (List<Integer> s : sp) {
            HashMap<Integer,PriorityQueue<Integer>> cousling = new HashMap<>();
            for (int idx = 1; idx <= k; idx++) {
                // 각 상담 유형(k-1)마다 우선순위 큐 생성 후 미리 배치된 상담사만큼 초기화
                PriorityQueue<Integer> pq = new PriorityQueue<>();
                int cmp = s.get(idx-1);
                for (int i = 0; i < cmp; i++) {
                    pq.offer(0);
                }
                cousling.put(idx,pq);
            }
            int wait = 0;
            for (int[] r : reqs) {
                int a = r[0];
                int b = r[1];
                int c = r[2];
                Integer end = cousling.get(c).poll();
                if (end > a) {
                    wait += end - a;
                    a = end;
                }
                cousling.get(c).offer(a+b);
            }
            ans = Math.min(ans,wait);
        }
        return ans;
    }
    
    public List<List<Integer>> split(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(new ArrayList<Integer>(),n,k,result);
        return result;
    }
    
    public void dfs(List<Integer> path, int rest_sum, int rest_k, List<List<Integer>> result) {
        if (rest_k == 0) {
            if (rest_sum == 0) result.add(new ArrayList<>(path));
            return;
        }
        
        Integer min = 1;
        Integer max = rest_sum - (rest_k-1);
        if (min > max) return;
        for (int value = min; value <= max; value++) {
            path.add(value);
            dfs(path,rest_sum-value,rest_k-1,result);
            path.remove(path.size() - 1);
        }
    }
}