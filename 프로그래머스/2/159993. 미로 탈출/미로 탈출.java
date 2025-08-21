import java.util.*;
class Solution {
    int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    int n;
    int m;
    char[][] arr;
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        int sx = 0;
        int sy = 0;
        int lx = 0;
        int ly = 0;
        arr = new char[n][m];
        // arr 초기화
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) == 'S') {
                    sx = i;
                    sy = j;
                }
                if (maps[i].charAt(j) == 'L') {
                    lx = i;
                    ly = j;
                }
                arr[i][j] = maps[i].charAt(j);
            }
        }
        int tol = bfs(sx,sy,'L');
        int toe = bfs(lx,ly,'E');
        System.out.println("tol: " + tol + ", toe: " + toe);
        if (tol == -1) return -1;
        if (toe == -1) return -1;
        return tol+toe;
    }
    
    public int bfs(int x, int y, char t) {
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visit = new boolean[n][m];
        visit[x][y] = true;
        int cnt = 0;
        q.add(new int[] {x,y,cnt});
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            int step = cur[2];
            if (arr[cx][cy] == t) return step;
            for (int[] d : dir) {
                int nx = cx + d[0];
                int ny = cy + d[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visit[nx][ny] && arr[nx][ny] != 'X') {
                        visit[nx][ny] = true;
                        q.add(new int[] {nx,ny,step+1});
                    }
                }
            }
        }
        return -1;
    }
}