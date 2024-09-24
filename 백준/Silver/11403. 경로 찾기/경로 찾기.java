import java.io.*;
import java.util.*;

class Main {
    static int[][] map;
    static int[][] ans;
    static int n;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        map = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if(map[i][j] == 1) bfs(i,j);
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                sb.append(ans[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static void bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visit = new boolean[n+1][n+1];
        q.offer(new int[]{i, j});
        ans[i][j] = 1;
        visit[i][j] = true;
        while(!q.isEmpty()){
            int[] arr = q.poll();
            int a = arr[0];
            int b = arr[1];
            for(int k = 1; k <= n; k++) {
                if(map[b][k] == 1 && !visit[b][k]) {
                    q.offer(new int[]{a, k});
                    visit[b][k] = true;
                    ans[a][k] = 1;
                }
            }
        }
    }
}