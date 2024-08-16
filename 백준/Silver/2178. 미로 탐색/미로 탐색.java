import java.io.*;
import java.util.*;

class Main{
    static int[][] map;
    static boolean[][] visit;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int n;
    static int m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n + 1][m + 1];
        visit = new boolean[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            String str = br.readLine();
            for(int j = 0; j < m; j++) {
                map[i][j + 1] = str.charAt(j) - '0';
            }
        }
        bfs(1, 1);
        System.out.println(map[n][m]);
    }

    private static void bfs(int n, int m) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {n, m});
        visit[n][m] = true;

        while(!q.isEmpty()) {
            int[] nums = q.poll();
            int px = nums[0];
            int py = nums[1];
            for (int i = 0; i < 4; i++) {
                int nx = px + dx[i];
                int ny = py + dy[i];
                if(Check(nx, ny) && !visit[nx][ny]) {
                    visit[nx][ny] = true;
                    map[nx][ny] += map[px][py];
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }

    private static boolean Check(int nx, int ny) {
        return (nx > 0 && nx <= n && ny > 0 && ny <= m && map[nx][ny] != 0);
    }
}