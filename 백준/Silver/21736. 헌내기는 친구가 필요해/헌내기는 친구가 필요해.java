import java.io.*;
import java.util.*;

class Main {
    static char[][] map;
    static int[] dx = new int[] {1, -1, 0, 0};
    static int[] dy = new int[] {0, 0, 1, -1};
    static int n;
    static int m;
    static int cnt = 0;
    static boolean[][] visit;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new char[n][m];
        visit = new boolean[n][m];

        for(int i = 0; i < n; i++) {
            String str = br.readLine();
            for(int j = 0; j < m; j++) {
                map[i][j] = str.charAt(j);
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(map[i][j] == 'I') {
                    bfs(i, j);
                    break;
                }
            }
        }
        String ans = "TT";
        if(cnt == 0) System.out.println(ans);
        else System.out.println(cnt);
    }

    private static void bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {i, j});
        visit[i][j] = true;

        while(!q.isEmpty()) {
            int[] arr = q.poll();
            int x = arr[0];
            int y = arr[1];

            for(int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(!Check(nx, ny)) continue;
                if(!visit[nx][ny] && map[nx][ny] != 'X') {
                    visit[nx][ny] = true;
                    q.offer(new int[] {nx, ny});
                    if(map[nx][ny] == 'P') cnt++;
                }
            }
        }
    }

    private static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < n && 0 <= ny && ny < m;
    }
}