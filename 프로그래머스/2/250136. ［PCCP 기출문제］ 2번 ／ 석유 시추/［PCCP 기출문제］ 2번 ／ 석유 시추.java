import java.util.*;
class Solution {
    static int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    static int n;
    static int m;
    static int cnt = 2;
    static Map<Integer, Integer> oil = new HashMap<>();
    public int solution(int[][] land) {
        int ans = 0;
        n = land.length;
        m = land[0].length;
        boolean[][] visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && land[i][j] == 1) {
                    bfs(i,j,visit,land);
                    cnt++;
                }
            }
        }
        // col을 순회하면서 시추 시작
        for (int c = 0; c < m; c++) {
            int count = 0;
            // 방문한 시추구역 번호 저장할 set
            Set<Integer> set = new HashSet<>();
            for (int r = 0; r < n; r++) {
                // 시추구역아니면 패스
                if (land[r][c] == 0) continue;
                int num = land[r][c];
                if (set.contains(num)) continue;
                set.add(num);
                count += oil.get(num);
            }
            ans = Math.max(ans,count);
        }
        return ans;
    }
    
    public static void bfs(int x, int y, boolean[][] visit, int[][] land) {
        Queue<int []> q = new ArrayDeque<>();
        visit[x][y] = true;
        q.add(new int[] {x,y});
        int total = 1;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            land[cx][cy] = cnt;
            for (int[] d : dir) {
                int nx = cx + d[0];
                int ny = cy + d[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visit[nx][ny] && land[nx][ny] == 1) {
                        visit[nx][ny] = true;
                        q.add(new int[] {nx,ny});
                        total++;
                    }
                }
            }
        }
        // 다 순회하고 나서 map에 등록
        oil.put(cnt,total);
    }
}