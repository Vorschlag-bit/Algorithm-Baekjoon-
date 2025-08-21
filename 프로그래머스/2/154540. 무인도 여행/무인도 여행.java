import java.util.*;
class Solution {
    int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    int m;
    int n;
    boolean[][] visit;
    char[][] arr;
    List<Integer> ans = new ArrayList<>();
    public int[] solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        visit = new boolean[n][m];
        arr = new char[n][m];
        // arr 초기화
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = maps[i].charAt(j);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && arr[i][j] != 'X') bfs(i,j);
            }
        }
        if (ans.size() == 0) return new int[] {-1};
        Collections.sort(ans);
        int[] answer = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) answer[i] = ans.get(i);
        return answer;
    }
    
    public void bfs(int x, int y) {
        Queue<int[]> q = new ArrayDeque<>();
        visit[x][y] = true;
        int cnt = Integer.valueOf(arr[x][y]) - '0';
        q.add(new int[] {x,y});
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            for (int[] d : dir) {
                int nx = cx + d[0];
                int ny = cy + d[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visit[nx][ny] && arr[nx][ny] != 'X') {
                        cnt += Integer.valueOf(arr[nx][ny]) - '0';
                        visit[nx][ny] = true;
                        q.add(new int[] {nx,ny});
                    }
                }
            }
        }
        ans.add(cnt);
    }
}