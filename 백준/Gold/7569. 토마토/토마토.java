import java.util.*;
import java.io.*;

class Main{
    static Queue<int[]> q = new LinkedList<>();
    static int[] dx = {0, 0, 1, -1, 0, 0};
    static int[] dy = {1, -1, 0, 0, 0, 0};
    static int[] dz = {0, 0, 0, 0, 1, -1};
    static int[][][] map;
    static int m;
    static int n;
    static int h;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        map = new int[h][n][m];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    map[i][j][k] = Integer.parseInt(st.nextToken());
                }
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if(map[i][j][k] == 1) {
                        q.offer(new int[]{i, j, k});
                    }
                }
            }
        }
        bfs();
        int ans = 0;
        boolean isValid = true;
        for (int i = 0; i < h; i++) {
            if(!isValid) break;
            for (int j = 0; j < n; j++) {
                if(!isValid) break;
                for (int k = 0; k < m; k++) {
                    if(map[i][j][k] == 0) {
                        isValid = false;
                        ans = -1;
                        break;
                    }
                    ans = Math.max(ans, map[i][j][k]);
                }
            }
        }
        if(isValid) System.out.println(ans - 1);
        else System.out.println(ans);
    }

    private static void bfs() {
        while(!q.isEmpty()) {
            int[] arr = q.poll();
            int z = arr[0];
            int x = arr[1];
            int y = arr[2];
            for(int i = 0; i < 6; i++) {
                int nz = z + dz[i];
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(Check(nz, nx, ny) && map[nz][nx][ny] == 0) {
                    map[nz][nx][ny] = map[z][x][y] + 1;
                    q.offer(new int[]{nz, nx, ny});
                }
            }
        }
    }

    private static boolean Check(int nz, int nx, int ny) {
        return 0 <= nz && nz < h && 0 <= nx && nx < n && 0 <= ny && ny < m;
    }
}