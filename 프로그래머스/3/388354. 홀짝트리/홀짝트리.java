import java.util.*;
class Solution {
    public int[] solution(int[] nodes, int[][] edges) {
        int[] ans = new int[2];
        
        Map<Integer,List<Integer>> graph = new HashMap<>();
        // 그래프 연결
        for (int i = 0; i < edges.length; i++) {
            int s = edges[i][0];
            int n = edges[i][1];
            List<Integer> l = graph.getOrDefault(s, new ArrayList<Integer>());
            List<Integer> l2 = graph.getOrDefault(n, new ArrayList<Integer>());
            l2.add(s);
            l.add(n);
            graph.put(s,l);
            graph.put(n,l2);
        }
        
        // 부모로서 홀짝트리 -> 자식으로서 역홀짝
        // 부모로서 역홀짝 -> 자식으로서 홀짝
        Set<Integer> visit = new HashSet<>();
        for (int node : nodes) {
            // 방문한 트리라면 패스
            if (visit.contains(node)) continue;
            // 홀짝 노드 수
            int cnt = 0;
            // 역홀짝 노드 수
            int reversecnt = 0;
            Queue<Integer> q = new ArrayDeque<Integer>();
            q.add(node);
            visit.add(node);
            
            while(!q.isEmpty()) {
                int cur = q.poll();
                List<Integer> nxt_nodes = graph.getOrDefault(cur, new ArrayList<Integer>());
                if (nxt_nodes.size() % 2 == cur % 2) cnt++;
                else reversecnt++;
                for (int nxt : nxt_nodes) {
                    if (!visit.contains(nxt)) {
                        q.add(nxt);
                        visit.add(nxt);
                    }
                }
            }
            if (cnt == 1) ans[0]++;
            if (reversecnt == 1) ans[1]++;
        }
        return ans;
    }
}