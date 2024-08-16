import java.io.*;
import java.util.*;

class Main{
    static boolean[] visit;
    static int[][] map;
    static int ans = 0;
    static int n;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        map = new int[n + 1][n + 1];
        visit = new boolean[n + 1];

        for(int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            map[x][y] = 1;
            map[y][x] = 1;
        }
        bfs(1);
        System.out.print(ans);
    }
    private static void bfs(int i) {
        Queue<Integer> q = new LinkedList<>();
        visit[i] = true;
        q.offer(i);

        while(!q.isEmpty()) {
            int a = q.poll();
            for(int j = 1; j <= n; j++) {
                if(map[a][j] == 1 && !visit[j]) {
                    visit[j] = true;
                    ans++;
                    q.offer(j);
                }
            }
        }
    }
}