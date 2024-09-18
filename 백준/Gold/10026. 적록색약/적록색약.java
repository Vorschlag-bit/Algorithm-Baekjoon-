import java.io.*;
import java.util.*;

class Main{
    static int n;
    static char[][] map;
    static boolean[][] visit;
    static int dx[] = {1, -1, 0 , 0};
    static int dy[] = {0, 0, 1 , -1};
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map  = new char[n][n];
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < n; i++) {
            String str = br.readLine();
            for(int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j);
            }
        }

        // 일반인 시야
        int sec1 = 0;
        visit = new boolean[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                char color = map[i][j];
                if(!visit[i][j]) sec1 += bfs(i, j, color);
            }
        }
        sb.append(sec1 + " ");
        // 적록색약 시야
        int sec2 = 0;
        visit = new boolean[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                char color = map[i][j];
                if(!visit[i][j]) {
                    if (color == 'R' || color == 'G')
                        sec2 += bfsRG(i, j);
                    if (color == 'B')
                        sec2 += bfs(i, j, color);
                }
            }
        }
        sb.append(sec2);
        System.out.println(sb);
    }

    private static int bfs(int x, int y, char color) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visit[x][y] = true;

        while(!q.isEmpty()){
            int[] arr = q.poll();
            int cx = arr[0];
            int cy = arr[1];

            for(int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if(Check(nx, ny) && map[nx][ny] == color && !visit[nx][ny]) {
                    visit[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return 1;
    }

    private static int bfsRG(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visit[x][y] = true;

        while(!q.isEmpty()){
            int[] arr = q.poll();
            int cx = arr[0];
            int cy = arr[1];

            for(int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if(Check(nx, ny) && (map[nx][ny] == 'R' || map[nx][ny] == 'G') && !visit[nx][ny]) {
                    visit[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return 1;
    }

    private static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < n && 0 <= ny && ny < n;
    }
}