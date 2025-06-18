import java.util.*;
class Solution {
    class Pair {
        int x;
        int y;
        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int n;
    static int m;
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        int[][] arr = new int[n][m];
        Deque<Pair> q = new ArrayDeque<>();
        q.offer(new Pair(0,0));
        while (!q.isEmpty()) {
            Pair cur = q.poll();
            int cx = cur.x;
            int cy = cur.y;
            if (cx == n-1 && cy == m-1) break;
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (check(nx,ny) && arr[nx][ny] == 0 && maps[nx][ny] == 1) {
                    arr[nx][ny] = arr[cx][cy] + 1;
                    q.offer(new Pair(nx,ny));
                }
            }
        }
        if (arr[n-1][m-1] != 0) return arr[n-1][m-1]+1;
        else return -1;
    }
    public boolean check(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}