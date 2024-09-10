import java.util.*;
import java.io.*;

class Main {
    static int[][] map;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};
    static int m;
    static int n;
    static int ans = 0;
    static Queue<int[]> q = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        map = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(map[i][j] == 1) q.offer(new int[]{i, j});
            }
        }
        bfs();
        boolean isValid = true;
        for (int i = 0; i < n; i++) {
            if(!isValid) break;
            for (int j = 0; j < m; j++) {
                if(map[i][j] == 0) {
                    isValid = false; break;
                }
                ans = Math.max(ans, map[i][j]);
            }
        }
        if(isValid)
        System.out.println(ans - 1);
        else System.out.println(-1);
    }

    private static void bfs() {
        while(!q.isEmpty()) {
            int[] arr = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = arr[0] + dx[i];
                int ny = arr[1] + dy[i];
                if(Check(nx, ny) && map[nx][ny] == 0) {
                    map[nx][ny] = 1 + map[arr[0]][arr[1]];
                    q.offer(new int[]{nx,ny});
                }
            }
        }
    }

    private static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < n && 0<= ny && ny < m;
    }
}