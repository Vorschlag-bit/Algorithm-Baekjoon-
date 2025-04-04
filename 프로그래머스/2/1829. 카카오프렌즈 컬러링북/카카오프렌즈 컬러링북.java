import java.util.*;

class Solution {
    int[] dx = {0, 0, 1, -1};
    int[] dy = {1, -1, 0, 0};
    boolean[][] visit;

    public int[] solution(int m, int n, int[][] picture) {
        int number = 0;
        int maxSize = 0;
        visit = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visit[i][j]) {
                    int size = bfs(i, j, picture[i][j], picture, m, n);
                    number++;
                    maxSize = Math.max(maxSize, size);
                }
            }
        }

        return new int[]{number, maxSize};
    }

    public int bfs(int x, int y, int color, int[][] picture, int m, int n) {
        int cnt = 1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visit[x][y] = true;

        while (!q.isEmpty()) {
            int[] arr = q.poll();
            int cx = arr[0];
            int cy = arr[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (!check(nx, ny, m, n)) continue;

                if (!visit[nx][ny] && picture[nx][ny] == color) {
                    q.offer(new int[]{nx, ny});
                    visit[nx][ny] = true;
                    cnt++;
                }
            }
        }

        return cnt;
    }

    public boolean check(int x, int y, int m, int n) {
        return 0 <= x && x < m && 0 <= y && y < n;
    }
}