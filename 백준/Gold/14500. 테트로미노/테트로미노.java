import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int m;
    static int[][] map;
    static int ans = 0;
    static boolean[][] visit;
    static int[]dx = {1, -1, 0, 0};
    static int[]dy = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visit[i][j] = true;
                dfs(i , j, map[i][j], 1);
                visit[i][j] = false;
            }
        }
        System.out.println(ans);
    }

    private static void dfs(int x, int y, int sum, int cnt) {
        if(cnt == 4) {
            ans = Math.max(ans, sum);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(!Check(nx, ny)) continue;

            if(!visit[nx][ny]) {

                if(cnt == 2) {
                    // ㅗ 모양을 위한 dfs
                    visit[nx][ny] = true;
                    dfs(x, y, sum + map[nx][ny], cnt + 1);
                    visit[nx][ny] = false;
                }

                visit[nx][ny] = true;
                dfs(nx, ny, sum + map[nx][ny], cnt + 1);
                visit[nx][ny] = false;
            }
        }
    }

    private static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < n && 0 <= ny && ny < m;
    }
}