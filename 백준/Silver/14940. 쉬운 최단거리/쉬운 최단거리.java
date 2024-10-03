import java.io.*;
import java.util.*;

class Main{
    static int n;
    static int m;
    static int map[][];
    static boolean[][] visit;
    static int newMap[][];
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        newMap = new int[n][m];
        visit = new boolean[n][m];
        int x = 0;
        int y = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int num = Integer.parseInt(st.nextToken());
                map[i][j] = num;
            }
        }
        for (int i = 0; i < n; i++) {
            Arrays.fill(newMap[i], -1);
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) newMap[i][j] = 0;
                else if (map[i][j] == 2) {
                    newMap[i][j] = 0;
                    x = i;
                    y = j;
                }
            }
        }
        bfs(x, y);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sb.append(newMap[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();

        q.offer(new int[]{x,y});
        visit[x][y] = true;
        while(!q.isEmpty()) {
            int[] arr = q.poll();
            int i = arr[0];
            int j = arr[1];
            for (int k = 0; k < 4; k++) {
                int nx = i + dx[k];
                int ny = j + dy[k];

                if(!Check(nx, ny)) continue;

                if(map[nx][ny] != 0 && !visit[nx][ny]) {
                    visit[nx][ny] = true;
                    q.offer(new int[] {nx, ny});
                    newMap[nx][ny] = newMap[i][j] + 1;
                }
            }
        }
    }

    private static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < n && 0 <= ny && ny < m;
    }
}